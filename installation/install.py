# install.py
# Version: 1.0.0
# Installs dependences needed for CS530 Project
# Author: Diego De La Toba, Ian Sanchez

import os
from shutil import copy2


def install_dependencies():
    print("================== Start Installing PIP ==================")
    os.system("sudo apt install python3-pip -y")
    print("================== Completed Installing PIP ==================")

    print("================== Start Updating PIP ==================")
    os.system("sudo pip3 install --upgrade pip")
    print("================== Completed Updating PIP ==================")

    print("================== Start Installing Numpy, Scipy, PyAudio, PyQtgraph ==================")
    os.system("sudo apt install python-numpy python-scipy python-pyaudio python-pyqtgraph -y")
    os.system("sudo pip3 install numpy scipy==1.4.1 pyaudio pyqtgraph")
    print("================== Completed Installing Numpy, Scipy, PyAudio, PyQtgraph ==================")

    print("================== Start Installing rpi_ws281x ==================")
    os.system("sudo pip3 install rpi_ws281x")
    print("================== Completed Installing rpi_ws281x ==================")

install_dependencies()
