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
    "CLAUDE.md",
    "README.md",
    "agents.yaml",
    "GEMINI.md",
    "lefthook.yml",
    "skills-lock.json",
]

# Special rename map: source_filename -> bundle_filename
# DESIGN.md → template so consumers can customize without overwriting source.
# install scripts → root level with clear platform labels.
RENAME_MAP = {
    "DESIGN.md":        "DESIGN.template.md",
    "scripts/install.ps1": "install-windows.ps1",
    "scripts/install.sh":  "install-linux.sh",
}

def setup_build_dir():
    """Create temp build structure"""
    build_path = os.path.join(DIST_DIR, "temp_build")
    master_path = os.path.join(build_path, MASTER_FOLDER)
    bundle_path = os.path.join(master_path, BUNDLE_SUBDIR)
    
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
    
    os.makedirs(bundle_path)
    print(f"  [+] Created Master structure: {MASTER_FOLDER}/{BUNDLE_SUBDIR}")
    return build_path, master_path, bundle_path

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

def package_framework(bundle_path):
    """Copy framework files to /bundle, honouring the RENAME_MAP."""
    all_items = list(INCLUSION_LIST) + list(RENAME_MAP.keys())
    for item in all_items:
        if not os.path.exists(item):
            print(f"  [!] Missing {item}")
            continue

        # Determine destination name (apply rename if mapped)
        dest_name = RENAME_MAP.get(item, item)
        target_path = os.path.join(bundle_path, dest_name)
        label = f"{item} -> {dest_name}" if dest_name != item else item
        print(f"  [+] Packaging {label} -> {BUNDLE_SUBDIR}/")

        if os.path.isdir(item):
            shutil.copytree(item, target_path, ignore=get_ignore_list)
        else:
            # Ensure parent dirs exist (e.g. nested renames)
            os.makedirs(os.path.dirname(target_path), exist_ok=True) if os.path.dirname(target_path) else None
            shutil.copy2(item, target_path)

def package_installer(master_path):
    """Copy installer to Master Root"""
    installer_src = "scripts/install_morphic.py"
    if os.path.exists(installer_src):
        shutil.copy2(installer_src, os.path.join(master_path, "install.py"))
        print("  [+] Added installer: install.py")

def create_manifest(master_path):
    """Create Manifest"""
    manifest = {
        "version": VERSION,
        "build_date": datetime.now().isoformat(),
        "master_folder": MASTER_FOLDER,
        "bundle_subdir": BUNDLE_SUBDIR
    }
    with open(os.path.join(master_path, "morphic_manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)

def create_archive(master_path):
    """Tar it up"""
    archive_final_path = os.path.join(DIST_DIR, ARCHIVE_NAME)
    with tarfile.open(archive_final_path, "w:gz") as tar:
        tar.add(master_path, arcname=MASTER_FOLDER)
    return archive_final_path

def build():
    print(f"Building Morphic Master Bundle {VERSION}...")
    
    build_path, master_path, bundle_path = setup_build_dir()
    
    package_framework(bundle_path)
    package_installer(master_path)
    create_manifest(master_path)
    
    archive_path = create_archive(master_path)

    # Cleanup temp
    shutil.rmtree(build_path)
    print(f"\nBuild complete: {archive_path}")

if __name__ == "__main__":
    build()
