#!/usr/bin/env python3
"""
SuperDuper Project Setup Script

This script helps set up the development environment for the SuperDuper project.
Run this script to create a virtual environment and install all dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}:")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        return None

def main():
    """Main setup function."""
    print("🚀 Setting up SuperDuper Project Environment")
    print("=" * 50)
    
    # Get the project directory
    project_dir = Path(__file__).parent.absolute()
    print(f"📁 Project directory: {project_dir}")
    
    # Change to project directory
    os.chdir(project_dir)
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"   Current version: {python_version.major}.{python_version.minor}")
        sys.exit(1)
    
    print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Create virtual environment
    venv_path = project_dir / "venv"
    if not venv_path.exists():
        if not run_command("python3 -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists!")
    
    # Determine activation script based on OS
    if sys.platform == "win32":
        activate_script = venv_path / "Scripts" / "activate"
        pip_path = venv_path / "Scripts" / "pip"
    else:
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    # Install requirements
    if not run_command(f"{pip_path} install --upgrade pip", "Upgrading pip"):
        sys.exit(1)
    
    if not run_command(f"{pip_path} install -r requirements.txt", "Installing project dependencies"):
        sys.exit(1)
    
    # Verify installation
    print("\n🔍 Verifying installation...")
    verification_commands = [
        ("python3 --version", "Python version"),
        ("pip list | grep pandas", "Pandas installation"),
        ("pip list | grep matplotlib", "Matplotlib installation"),
        ("pip list | grep jupyter", "Jupyter installation")
    ]
    
    for cmd, desc in verification_commands:
        full_cmd = f"source {activate_script} && {cmd}" if sys.platform != "win32" else f"{activate_script} && {cmd}"
        run_command(full_cmd, f"Checking {desc}")
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    
    if sys.platform == "win32":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Start Jupyter Notebook:")
    print("   jupyter notebook")
    print("3. Open SuperDuper.ipynb and start learning!")
    print("\n📚 Check README.md for detailed documentation.")

if __name__ == "__main__":
    main()
