import subprocess
from utils.dialog_helper import show_selection_dialog

def install_dnf_packages():
    packages = {
        "Vim": "vim",
        "Git": "git",
        "Curl": "curl",
        "Htop": "htop",
    }
    selected_packages = show_selection_dialog("DNF Packages", packages)
    if selected_packages:
        subprocess.run(["sudo", "dnf", "install", "-y"] + selected_packages)
