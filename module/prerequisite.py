import os
import subprocess

def install_requirements():
    # Download library
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,check=True)

def download_data():
    # Download data from Google Drive
    if not os.path.exists('open.zip'):
        subprocess.run(['pip', 'install', 'gdown'], check=True)
        subprocess.run(['gdown', 'https://drive.google.com/uc?id=13WixS0gfcsb7NkKGje6QZA1phPlVhKQm'], check=True)

    # Unzip to the 'data' directory
    if not os.path.exists('./data'):
        subprocess.run(['unzip', 'open.zip', '-d', 'data'], check=True)