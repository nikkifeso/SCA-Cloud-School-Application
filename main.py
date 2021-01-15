#!/usr/bin/env python3

import os
import platform

software = ['wget', 'curl', 'node']


def install_os():
    if platform.system() == 'Darwin':
        os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        for item in software:
            check_version = os.system(f"{item} --version")
            if check_version != 0:
                os.system(f"brew install {item}")

    elif platform.system() == 'Linux':
        os.system(f"sudo apt-get update")
        for item in software:
            if item == 'node':
                check_node_version = os.system(f"node -version")
                if check_node_version != 0:
                    os.system(f"sudo apt-get install nodejs")
            check_version = os.system(f"{item} --version")
            if check_version != 0:
                os.system(f"sudo apt-get install {item}")

    elif platform.system() == 'Windows':
        os.system("powershell.exe Set-ExecutionPolicy RemoteSigned -scope CurrentUser")
        os.system("powershell.exe Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')")
        for item in software:
            if item == "node":
                os.system(f"start /wait cmd /c scoop install nodejs")
            os.system(f"start /wait cmd /c scoop install {item}")
    else:
        print("Operating System Not Found")

    status = "Process completed!"
    print(status)


if __name__ == '__main__':
    install_os()
