import os
import subprocess


def initialize_dvc():
    """
    Initializes DVC in the project directory.
    """
    try:
        subprocess.run(["dvc", "init"], check=True)
        print("DVC initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing DVC: {e}")


def configure_remote(remote_name: str, remote_path: str):
    """
    Configures a DVC remote storage.
    Args:
        remote_name (str): The name of the remote (e.g., 'localstorage').
        remote_path (str): The path to the remote storage directory.
    """
    try:
        subprocess.run(["mkdir", "-p", remote_path], check=True)
        subprocess.run(["dvc", "remote", "add", "-d", remote_name, remote_path], check=True)
        print(f"DVC remote '{remote_name}' configured at '{remote_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring DVC remote: {e}")


def track_data(file_path: str):
    """
    Adds a data file to DVC tracking.
    Args:
        file_path (str): Path to the file to track.
    """
    try:
        subprocess.run(["dvc", "add", file_path], check=True)
        print(f"File '{file_path}' added to DVC tracking.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding file '{file_path}' to DVC: {e}")


def push_to_remote():
    """
    Pushes tracked data to the configured DVC remote.
    """
    try:
        subprocess.run(["dvc", "push"], check=True)
        print("Data pushed to DVC remote successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing data to remote: {e}")
