#!bin/bash

# download conda
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

# Cryptographic hash verification
sha256sum Anaconda3-2023.09-0-Linux-x86_64.sh

# install conda
bash Anaconda3-2023.09-0-Linux-x86_64.sh

conda update conda
conda create --name line_bot python=3.10

source activate line_bot

# install line-bot-sdk
pip install --upgrade pip
pip install Flask
pip install line-bot-sdk

# install ngrok
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok