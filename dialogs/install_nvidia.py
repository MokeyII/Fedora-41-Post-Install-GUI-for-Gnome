import subprocess
from utils.dialog_helper import show_selection_dialog

def install_nvidia_packages():
    nvidia_packages = {
        "AKMOD NVIDIA Driver": "akmod-nvidia",
        "NVIDIA CUDA Driver": "xorg-x11-drv-nvidia-cuda",
        "NVIDIA CUDA Libraries": "xorg-x11-drv-nvidia-cuda-libs",
    }
    selected_packages = show_selection_dialog("NVIDIA Packages", nvidia_packages)
    if selected_packages:
        subprocess.run(["sudo", "dnf", "install", "-y"] + selected_packages)
