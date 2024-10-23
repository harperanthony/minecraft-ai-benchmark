#!/bin/bash

# Update package list
sudo apt update

# Install Java
sudo apt install -y openjdk-11-jdk

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install system dependencies for MineRL
sudo apt install -y xvfb ffmpeg

# Upgrade pip
pip3 install --upgrade pip

# Install Python dependencies
pip3 install -r requirements.txt

# Install MineRL
pip3 install git+https://github.com/minerllabs/minerl

# Set up virtual display for headless mode
echo "export DISPLAY=:0" >> ~/.bashrc
source ~/.bashrc

