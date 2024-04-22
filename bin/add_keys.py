#!/usr/bin/env python3

import os
import subprocess

def add_ssh_keys_to_agent(directory):
    # Get a list of all files in the specified directory
    files = os.listdir(directory)

    # Filter out non-SSH key files
    ssh_keys = [file for file in files if file.endswith('.pub')]

    # Add each SSH key to the SSH agent
    for pub_key_file in ssh_keys:
        private_key_file = pub_key_file[:-4]  # Remove the '.pub' extension
        private_key_path = os.path.join(directory, private_key_file)

        if os.path.exists(private_key_path):
            subprocess.run(['ssh-add','-c',private_key_path])
        else:
            print(f"private key file '{private_key_file}' not found for '{pub_key_file}'")

if __name__ == "__main__":
    # Get the user's home directory
    home_directory = os.path.expanduser('~')

    # Set the SSH keys directory to the .ssh directory in the home directory
    ssh_keys_directory = os.path.join(home_directory, '.ssh')

    add_ssh_keys_to_agent(ssh_keys_directory)

