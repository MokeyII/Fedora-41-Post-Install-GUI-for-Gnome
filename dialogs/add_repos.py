import subprocess
from utils.dialog_helper import show_selection_dialog

def add_repositories():
    # Define available repositories
    repos = {
        "RPM Fusion Free": "https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
        "RPM Fusion Non-Free": "https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
        "Flathub": "https://flathub.org/repo/flathub.flatpakrepo",
        "Flathub Beta": "https://flathub.org/beta-repo/flathub-beta.flatpakrepo",
    }

    # Show selection dialog to the user
    selected_repos = show_selection_dialog("Repositories to Add", repos, disable_on_select_all=True)

    # Install selected repositories
    if selected_repos:
        for repo in selected_repos:
            if repo.startswith("http"):  # DNF repositories
                subprocess.run(["sudo", "dnf", "install", "-y", repo])
            else:  # Flatpak repositories
                subprocess.run(["flatpak", "remote-add", "--if-not-exists", repo.split('/')[-1], repo])
