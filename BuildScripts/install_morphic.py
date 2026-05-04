import os
import shutil
import json
import subprocess
import sys
import platform

# Configuration
VERSION = "0.11.0"
MANIFEST_NAME = "morphic_manifest.json"
BUNDLE_DIR = "bundle"
MERGE_REPORT = "MERGE_REQUIRED.md"

def print_step(msg):
    print(f"\n  [STEP] {msg}")

def print_ok(msg):
    print(f"    [OK]  {msg}")

def print_warn(msg):
    print(f"    [WARN]  {msg}")

def print_fail(msg):
    print(f"    [FAIL]  {msg}")

def check_command(cmd):
    if platform.system() == "Windows":
        return subprocess.call(f"where {cmd}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    else:
        return subprocess.call(f"command -v {cmd}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def run_command(cmd, input_str=None):
    print(f"    [EXEC] {cmd}")
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, input=input_str)

def run_command_stream(cmd):
    # Use os.system on Windows/Linux to more reliably pass the TTY/Console handle 
    # to child processes so they can render interactive UIs like progress bars.
    print(f"    [EXEC] {cmd}")
    return os.system(cmd)

def install():
    print(f"Morphic Framework {VERSION} Installer")
    print("------------------------------------------")

    target_project_root = os.getcwd()
    
    if not os.path.exists(MANIFEST_NAME) or not os.path.exists(BUNDLE_DIR):
        print("  [!] Error: Manifest or bundle directory not found.")
        print("  [!] Please run this script from inside the 'Morphic-Framework' folder.")
        return

    bundle_path = os.path.abspath(BUNDLE_DIR)
    conflicts = []

    print(f"Phase 1: Deploying framework components to: {target_project_root}")

    for item in os.listdir(bundle_path):
        src_path = os.path.join(bundle_path, item)
        dst_path = os.path.join(target_project_root, item)
        
        if os.path.exists(dst_path):
            if os.path.isdir(src_path):
                merge_directories(src_path, dst_path, conflicts)
            else:
                conflicts.append(item)
        else:
            deploy_item(src_path, dst_path)

    if conflicts:
        generate_report(conflicts)
    else:
        print("\nPhase 1 Complete: Framework files successfully deployed.")

    print(f"\nPhase 2: Bootstrapping Environment")
    bootstrap_environment(conflicts)

def merge_directories(src_dir, dst_dir, conflicts):
    for root, dirs, files in os.walk(src_dir):
        relative_path = os.path.relpath(root, src_dir)
        target_dir = os.path.join(dst_dir, relative_path)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)
            
            if os.path.exists(dst_file):
                conflicts.append(os.path.join(relative_path, file))
            else:
                shutil.copy2(src_file, dst_file)
                print(f"  [+] Installed {os.path.join(relative_path, file)}")

def deploy_item(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)
    print(f"  [+] Installed {os.path.basename(src)}")

def generate_report(conflicts):
    with open(MERGE_REPORT, "w") as f:
        f.write(f"# Morphic v{VERSION}: Merge Required\n\n")
        f.write("The following files already exist in your project and were NOT overwritten.\n")
        f.write("Please merge them manually or use the AI prompt below.\n\n")
        
        f.write("## Conflict List\n")
        for c in sorted(set(conflicts)):
            f.write(f"- [ ] `{c}`\n")

def detect_stack_and_seed_beads():
    if not check_command("bd"):
        return
    
    print_step("Scanning codebase for tech stack...")
    stack_identified = False
    
    if os.path.exists("package.json") or os.path.exists("bun.lockb"):
        run_command('bd remember "STACK: JavaScript/TypeScript"')
        run_command('bd remember "RUNTIME: npm/bun"')
        stack_identified = True
        
    if os.path.exists("pyproject.toml") or os.path.exists("uv.lock"):
        run_command('bd remember "STACK: Python"')
        run_command('bd remember "RUNTIME: uv"')
        stack_identified = True
        
    if os.path.exists("pubspec.yaml"):
        run_command('bd remember "STACK: Flutter/Dart"')
        stack_identified = True
        
    if os.path.exists("src-tauri"):
        run_command('bd remember "STACK: Tauri"')
        stack_identified = True
        
    if stack_identified:
        run_command('bd remember "PROTOCOL: Use \'codanna mcp <tool> --args \\"<json>\\" --json\' for all codebase analysis."')
        print_ok("Stack detected and seeded to Beads memory")
    else:
        print_ok("No existing stack detected (clean project)")

def bootstrap_environment(conflicts):
    print_step("Checking Git Repository...")
    if not os.path.isdir(".git"):
        print_step("Initializing Git repository...")
        run_command("git init")
    else:
        print_ok("Git repository already initialized")

    print_step("Checking Node.js and NPM...")
    if check_command("npm"):
        print_ok("npm is available")
        
        print_step("Checking Bun (JS runtime)...")
        if not check_command("bun"):
            print_step("Installing Bun via npm...")
            run_command("npm install -g bun")
        
        if check_command("bun"):
            print_ok("Bun is available")
            
            # Global JS tools
            if not check_command("bd"):
                print_step("Installing @beads/bd globally via Bun...")
                run_command("bun add -g @beads/bd")
            else:
                print_ok("Beads (bd) already installed")

            if not check_command("lefthook"):
                print_step("Installing lefthook globally via Bun...")
                run_command("bun add -g @arkweid/lefthook")
            else:
                print_ok("Lefthook already installed")

            if check_command("lefthook"):
                run_command("lefthook install")
        else:
            print_warn("Bun installation failed. Falling back to npm...")
            if not check_command("bd"):
                run_command("npm install -g @beads/bd")
            if not check_command("lefthook"):
                run_command("npm install -g @arkweid/lefthook")
            
            if check_command("lefthook"):
                run_command("lefthook install")
    else:
        print_warn("npm not found! Please install Node.js manually to use Bun, Beads, and Lefthook.")

    # uv and Python dependencies
    print_step("Checking Python uv...")
    if not check_command("uv"):
        print_step("Installing uv via pip...")
        run_command("pip install uv --quiet")
    
    if check_command("uv"):
        print_ok("uv is available")
        print_step("Setting up Python virtual environment...")
        if not os.path.exists(".venv"):
            run_command("uv venv")
            print_ok("Created .venv")
        
        print_step("Installing Core Intelligence Stack (Cognee, pathspec, tqdm)...")
        if os.path.exists("pyproject.toml"):
            run_command("uv add cognee pathspec tqdm")
        else:
            # If no pyproject.toml, we ensure they are in the venv
            run_command("uv pip install cognee pathspec tqdm")
        print_ok("Intelligence Stack dependencies added to uv environment")
    else:
        print_warn("uv installation failed. Please install it manually.")

    # Dolt Check
    print_step("Checking Dolt (Beads database engine)...")
    if check_command("dolt"):
        print_ok("Dolt is available")
    else:
        print_warn("Dolt not found! Please install it manually from https://docs.dolthub.com/introduction/installation")

    print_step("Checking .env file...")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy2(".env.example", ".env")
            
            # Dynamically set absolute paths for Cognee to prevent sub-directory creation issues
            with open(".env", "r") as f:
                env_content = f.read()
            
            project_root = os.getcwd().replace("\\", "/")
            env_content = env_content.replace('SYSTEM_ROOT_DIRECTORY="./.cognee/system"', f'SYSTEM_ROOT_DIRECTORY="{project_root}/.cognee/system"')
            env_content = env_content.replace('DATA_ROOT_DIRECTORY="./.cognee/data"', f'DATA_ROOT_DIRECTORY="{project_root}/.cognee/data"')
            
            with open(".env", "w") as f:
                f.write(env_content)
                
            print_ok("Created .env from .env.example with absolute paths - please fill in your API keys!")
    else:
        print_ok(".env already exists")

    # Directory Structure
    print_step("Ensuring framework directory structure...")
    dirs = [
        ".agents/rules", ".agents/workflows", ".agents/skills",
        ".gemini/agents", ".gemini/commands", "docs/track/specs",
        "docs/memory/specs", "docs/memory/architecture",
        "docs/memory/lessons", "docs/architecture"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print_ok("Directory structure verified")

    # Gitignore Guards
    print_step("Verifying .gitignore entries...")
    ignores = [".cognee/", ".env", ".venv/", "__pycache__/", "dist/", "*.pyc"]
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            content = f.read()
        with open(".gitignore", "a") as f:
            for entry in ignores:
                if entry not in content:
                    f.write(f"\n{entry}")
    print_ok(".gitignore verified")

    print_step("Initializing Intelligence Stack...")
    
    if check_command("bd"):
        run_command("bd init", input_str="n\ny\n")
        detect_stack_and_seed_beads()
    
    if check_command("codanna"):
        print_step("Initializing Codanna...")
        run_command("codanna init")
        
        # Guard: Hardening .codannaignore (Ignore skills, media, and logs)
        if os.path.exists(".codannaignore"):
            with open(".codannaignore", "a") as f:
                f.write("\n# AI\n**/skills/**\n")
                f.write("\n# Media\n*.png\n*.jpg\n*.jpeg\n*.gif\n*.svg\n*.ico\n*.webp\n")
                f.write("\n# Logs\n*.log\n")
            print_ok("Hardened .codannaignore with AI skills, media, and log patterns")

        print_step("Indexing Codebase with Codanna (This may take a moment)...")
        run_command_stream("codanna index .")
        print_step("Adding Docs collection...")
        run_command("codanna documents add-collection docs docs/")
        print_step("Indexing Documents with Codanna (This may take a moment)...")
        run_command_stream("codanna documents index")
    else:
        print_warn("Codanna CLI not found! It is required for physical code analysis.")
        print("    [INFO] Install it manually: https://docs.codanna.sh/installation#native")
        print("    [INFO] After installation, run: codanna init; codanna index .")

    # Cleanup: Rename bundle to deleteBundle to signal it's safe to remove
    if os.path.exists(BUNDLE_DIR):
        try:
            if os.path.exists("deleteBundle"):
                shutil.rmtree("deleteBundle") # Clear old one if it exists
            os.rename(BUNDLE_DIR, "deleteBundle")
            print_ok("Renamed 'bundle' to 'deleteBundle' (deployment source ready for cleanup)")
        except Exception as e:
            print_warn(f"Could not rename 'bundle' to 'deleteBundle': {e}")

    print_next_steps(conflicts)

def print_next_steps(conflicts):
    print("\n" + "-" * 50)
    if conflicts:
        print(f"Morphic Framework PARTIALLY Deployed ({len(conflicts)} conflicts)")
    else:
        print("Morphic Framework Bootstrapped Successfully!")
    print("-" * 50)
    print("Next steps:")
    print("  1. Configure your API keys in .env (Copy vars from .env.example for Beads, Codanna, Cognee)")
    
    if conflicts:
        print(f"  2. RESOLVE CONFLICTS: Review {MERGE_REPORT} and merge files manually")
        step_idx = 3
    else:
        step_idx = 2

    print(f"  {step_idx}. Run: uv run scripts/cognee/indexer.py --full")
    print(f"  {step_idx+1}. Open your AI assistant and run the /init workflow")
    
    if conflicts:
        print("\n[!] IMPORTANT: Do not run the /init workflow until conflicts are resolved.")
    
    print("-" * 50)

if __name__ == "__main__":
    install()
