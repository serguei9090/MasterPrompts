import os
import tarfile
import json
import shutil
from datetime import datetime

# Configuration
VERSION = "0.10.7"
DIST_DIR = "dist"
MASTER_FOLDER = "Morphic-Framework"
BUNDLE_SUBDIR = "bundle"
ARCHIVE_NAME = f"morphic_v{VERSION}.tar.gz"

# Files/Folders to be explicitly excluded from the build
EXCLUSION_LIST = [
    "docs/track/audits",
    ".vscode",
    ".ps_history",
    "dist",
    "temp_build",
    "**/.git",
    "**/__pycache__"
]

# Files to be placed in the /bundle directory
INCLUSION_LIST = [
    ".agents",
    ".gemini",
    "docs",
    "scripts",
    ".cogneeignore",
    ".env.example",
    ".gitignore",
    "AGENTS.md",
    "agents.yaml",
    "GEMINI.md",
    "lefthook.yml",
    "skills-lock.json"
]

def build():
    print(f"Building Morphic Master Bundle {VERSION}...")
    
    # Create temp build structure
    build_path = os.path.join(DIST_DIR, "temp_build")
    master_path = os.path.join(build_path, MASTER_FOLDER)
    bundle_path = os.path.join(master_path, BUNDLE_SUBDIR)
    
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    
    os.makedirs(bundle_path)
    print(f"  [+] Created Master structure: {MASTER_FOLDER}/{BUNDLE_SUBDIR}")

    # 1. Copy framework files to /bundle
    def get_ignore_list(path, names):
        ignored = []
        for name in names:
            full_path = os.path.join(path, name)
            rel_path = os.path.relpath(full_path, ".")
            
            # Check against exclusion list
            for pattern in EXCLUSION_LIST:
                if pattern in rel_path.replace("\\", "/"):
                    ignored.append(name)
                    break
        return ignored

    for item in INCLUSION_LIST:
        if os.path.exists(item):
            print(f"  [+] Packaging {item} -> {BUNDLE_SUBDIR}/")
            target_path = os.path.join(bundle_path, item)
            if os.path.isdir(item):
                shutil.copytree(item, target_path, ignore=get_ignore_list)
            else:
                shutil.copy2(item, target_path)
        else:
            print(f"  [!] Missing {item}")

    # 2. Copy installer to Master Root
    installer_src = "scripts/install_morphic.py"
    if os.path.exists(installer_src):
        shutil.copy2(installer_src, os.path.join(master_path, "install.py"))
        print(f"  [+] Added installer: install.py")

    # 3. Create Manifest
    manifest = {
        "version": VERSION,
        "build_date": datetime.now().isoformat(),
        "master_folder": MASTER_FOLDER,
        "bundle_subdir": BUNDLE_SUBDIR
    }
    with open(os.path.join(master_path, "morphic_manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

    # 4. Tar it up
    archive_final_path = os.path.join(DIST_DIR, ARCHIVE_NAME)
    with tarfile.open(archive_final_path, "w:gz") as tar:
        tar.add(master_path, arcname=MASTER_FOLDER)

    # Cleanup temp
    shutil.rmtree(build_path)
    print(f"\nBuild complete: {archive_final_path}")

if __name__ == "__main__":
    build()
