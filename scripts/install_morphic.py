import os
import shutil
import json

# Configuration
VERSION = "0.10.6"
MANIFEST_NAME = "morphic_manifest.json"
BUNDLE_DIR = "bundle"
MERGE_REPORT = "MERGE_REQUIRED.md"

def install():
    print(f"Morphic Framework {VERSION} Installer")
    print("------------------------------------------")

    # The installer is assumed to be in the Master Folder root
    # We target the PARENT directory (the user project)
    target_project_root = os.getcwd()
    
    # Check if we are running in the right place
    if not os.path.exists(MANIFEST_NAME) or not os.path.exists(BUNDLE_DIR):
        print("  [!] Error: Manifest or bundle directory not found.")
        print("  [!] Please run this script from inside the 'Morphic-Framework' folder.")
        return

    with open(MANIFEST_NAME, "r"):
        pass # Just verifying it exists and is readable

    # All files inside the bundle/ directory should be deployed to the project root
    bundle_path = os.path.abspath(BUNDLE_DIR)
    conflicts = []

    print(f"📦 Deploying framework components to: {target_project_root}")

    for item in os.listdir(bundle_path):
        src_path = os.path.join(bundle_path, item)
        dst_path = os.path.join(target_project_root, item)
        
        if os.path.exists(dst_path):
            # Collision detected
            if os.path.isdir(src_path):
                # For directories, we merge recursively
                merge_directories(src_path, dst_path, conflicts)
            else:
                conflicts.append(item)
        else:
            # Safe to copy
            deploy_item(src_path, dst_path)

    if conflicts:
        generate_report(conflicts)
        print(f"\nINSTALLATION PARTIAL: {len(conflicts)} files have conflicts.")
        print(f"Please review {MERGE_REPORT} in your project root for merge instructions.")
    else:
        print("\nINSTALLATION COMPLETE: Framework successfully deployed.")

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
        
        f.write("\n---\n\n")
        f.write("## AI Resolution Prompt\n")
        f.write("Copy and paste this prompt to your AI assistant to resolve the conflicts:\n\n")
        f.write("```markdown\n")
        f.write("I am integrating the Morphic AI Engineering Framework v0.10.6. ")
        f.write("I have existing configurations that conflict with the framework mandates. ")
        f.write("Please perform a surgical merge of the following files. ")
        f.write("Preserve my project-specific identity (name, specific rules) but ensure ")
        f.write("the new framework mandates and Multi-Layer Memory protocols are integrated.\n\n")
        f.write("Conflicts to resolve:\n")
        for c in sorted(set(conflicts)):
            f.write(f"- {c}\n")
        f.write("\n```\n")

if __name__ == "__main__":
    install()
