import subprocess
from utils.dialog_helper import show_selection_dialog

def install_gaming_flatpak_packages():
    gaming_flatpaks = {
        "Steam": "com.valvesoftware.Steam",
        "Lutris": "net.lutris.Lutris",
        "Heroic Games Launcher": "com.heroicgameslauncher.hgl",
    }
    selected_gaming_flatpaks = show_selection_dialog(
        "Gaming Flatpaks", gaming_flatpaks, disable_on_select_all=True
    )
    if selected_gaming_flatpaks:
        subprocess.run(["flatpak", "install", "-y"] + selected_gaming_flatpaks)