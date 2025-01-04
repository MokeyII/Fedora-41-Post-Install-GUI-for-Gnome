import subprocess
from utils.dialog_helper import show_selection_dialog

def install_flatpak_packages():
    flatpaks = {
        "GNOME Platform": "org.gnome.Platform",
        "GNOME SDK": "org.gnome.Sdk",
    }
    selected_flatpaks = show_selection_dialog("Flatpaks", flatpaks)
    if selected_flatpaks:
        subprocess.run(["flatpak", "install", "-y"] + selected_flatpaks)
