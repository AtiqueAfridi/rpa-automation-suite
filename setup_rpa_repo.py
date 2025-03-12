import os

# Define the folder structure
FOLDER_STRUCTURE = {
    "automation": ["web", "desktop", "ocr"],
    "tests": [],
    "locators": [],
    "configs": [],
    "logs": [],
    "docs": [],
    "downloads": [],
    "uploads": [],
}

# Define files to be created
FILES = {
    "automation/__init__.py": "",
    "automation/common.py": "# Common utility functions\n",
    "automation/config.py": "# Configuration settings\n",
    "automation/main.py": "# Entry point to execute workflows\n",
    "automation/runner.py": "# CLI runner for automation tasks\n",
    
    "tests/__init__.py": "",
    "tests/test_web.py": "# Web automation tests\n",
    "tests/test_desktop.py": "# Desktop automation tests\n",
    "tests/test_ocr.py": "# OCR automation tests\n",
    
    "locators/__init__.py": "",
    "locators/web_locators.py": "# Web element locators\n",
    "locators/desktop_locators.py": "# Desktop element locators\n",
    
    "configs/settings.yaml": "# Configuration settings\n",
    "configs/credentials.env": "# Store sensitive data securely\n",
    "configs/logging.conf": "# Logging configuration\n",
    
    "logs/README.md": "# Logging guidelines\n",
    
    "docs/architecture.md": "# System architecture documentation\n",
    "docs/setup.md": "# How to set up the project\n",
    "docs/best_practices.md": "# Coding & automation guidelines\n",
    
    ".gitignore": """# Ignore unnecessary files
logs/
*.log
*.env
__pycache__/
""",
    "requirements.txt": "# List of dependencies\n",
    "Dockerfile": "# Docker container setup\n",
    "README.md": "# RPA Practice Repository\n",
    "setup.py": "# Package setup (if needed)\n",
}

def create_structure():
    """Create folder structure and files for the RPA practice repository."""
    base_dir = os.getcwd()  # Create everything in the current directory

    for folder, subfolders in FOLDER_STRUCTURE.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Add .gitkeep to empty folders
        if not subfolders:
            with open(os.path.join(folder_path, ".gitkeep"), "w", encoding="utf-8") as f:
                f.write("")

        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            with open(os.path.join(subfolder_path, ".gitkeep"), "w", encoding="utf-8") as f:
                f.write("")

    for file_path, content in FILES.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ RPA Repository structure has been created successfully!")

if __name__ == "__main__":
    create_structure()
