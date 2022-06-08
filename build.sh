#!/bin/bash

sudo apt-get update
sudo apt-get -y install upx-ucl python3 python3-pip

rm -rf dist build src/__pycache__

python3.8 -m pip install --upgrade pip
python3.8 -m pip install pyinstaller

pyinstaller ./src/__main__.py \
    --onefile --nowindow \
    --name=linuxos

cp dist/linuxos .
