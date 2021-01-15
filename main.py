#!/usr/bin/env python3

import os
import platform
import requests

software = ['wget', 'curl', 'node']
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


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
        wget = requests.get("http://ftp.gnu.org/gnu/wget/wget-1.11.4.tar.gz")
        with open(ROOT_DIR +"wget-1.11.4.tar.gz", "wb") as f:
            f.write(wget.content)

        curl = requests.get("https://curl.se/windows/dl-7.74.0_2/curl-7.74.0_2-win32-mingw.zip")
        with open(ROOT_DIR + "curl-7.74.0_2-win32-mingw.zip", "wb") as f:
            f.write(curl.content)

        node = requests.get("https://nodejs.org/dist/v14.15.4/node-v14.15.4.tar.gz")
        with open(ROOT_DIR + "node-v14.15.4.tar.gz", "wb") as f:
            f.write(node.content)
    else:
        print("Operating System Not Found")

    status = "Process completed!"
    print(status)


if __name__ == '__main__':
    install_os()
