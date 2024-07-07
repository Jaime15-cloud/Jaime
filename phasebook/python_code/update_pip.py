# File: update_pip.py

import subprocess

def update_pip():
    try:
        subprocess.check_call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
        print("pip updated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error updating pip: {e}")
