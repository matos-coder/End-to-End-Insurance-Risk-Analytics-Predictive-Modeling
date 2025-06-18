import os
import subprocess


def initialize_dvc():
    """
    Initializes DVC in the project directory.
    """
    try:
        # Check if .dvc folder already exists
        if os.path.exists(".dvc"):
            print("DVC is already initialized in this directory. Skipping initialization.")
            return

        # Run DVC init command
        subprocess.run(["dvc", "init"], check=True)
        print("DVC initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing DVC: {e}")
    except Exception as ex:
        print(f"Unexpected error during DVC initialization: {ex}")


def configure_remote(remote_name: str, remote_path: str):
    """
    Configures a DVC remote storage.
    Args:
        remote_name (str): The name of the remote (e.g., 'localstorage').
        remote_path (str): The path to the remote storage directory.
    """
    try:
        # Use os.makedirs for cross-platform directory creation
        os.makedirs(remote_path, exist_ok=True)
        print(f"Directory '{remote_path}' created or already exists.")

        # Configure the DVC remote
        subprocess.run(["dvc", "remote", "add", "-d", remote_name, remote_path], check=True)
        print(f"DVC remote '{remote_name}' configured at '{remote_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring DVC remote: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


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


def dvc_initialized():
    return os.path.isdir(os.path.join(os.getcwd(), ".dvc"))


def dvc_remote_exists(remote_name):
    try:
        result = subprocess.run(["dvc", "remote", "list"], capture_output=True, text=True, check=True)
        return remote_name in result.stdout
    except Exception as e:
        print("Error checking DVC remotes:", e)
        return False


def dvc_file_exists(data_path):
    dvc_file = data_path + ".dvc"
    return os.path.isfile(dvc_file)


# Step 1: Initialize DVC (if not already)
print("Checking DVC initialization...")
if dvc_initialized():
    print("DVC is already initialized.")
else:
    print("Initializing DVC...")
    try:
        initialize_dvc()
        print("DVC initialized successfully.")
    except Exception as e:
        print("Error initializing DVC:", e)

# Step 2: Configure DVC Remote (if not already)
REMOTE_NAME = "localstorage"
REMOTE_PATH = r"C:\Users\hp\Desktop\matos\tenx 10academy\week 3\End-to-End Insurance Risk Analytics & Predictive Modeling\data\remote_storage"
print(f"Checking if DVC remote '{REMOTE_NAME}' exists...")
if dvc_remote_exists(REMOTE_NAME):
    print(f"DVC remote '{REMOTE_NAME}' already exists.")
else:
    print(f"Configuring DVC remote '{REMOTE_NAME}' at '{REMOTE_PATH}'...")
    try:
        configure_remote(REMOTE_NAME, REMOTE_PATH)
        print("DVC remote configured successfully.")
    except Exception as e:
        print("Error configuring DVC remote:", e)

# Step 3: Add and Track Data
DATASET_PATH = "../data/raw/MachineLearningRating_v3.txt"
print(f"Checking if dataset exists at '{DATASET_PATH}'...")
if not os.path.isfile(DATASET_PATH):
    print(f"Dataset file '{DATASET_PATH}' does not exist. Please check the path.")
else:
    if dvc_file_exists(DATASET_PATH):
        print(f"File '{DATASET_PATH}' is already tracked by DVC.")
    else:
        print(f"Tracking dataset '{DATASET_PATH}' with DVC...")
        try:
            track_data(DATASET_PATH)
            print("Dataset tracked successfully.")
        except Exception as e:
            print("Error adding file to DVC:", e)

# Step 4: Commit Changes to Git (if .dvc file exists)
dvc_file = DATASET_PATH + ".dvc"
if os.path.isfile(dvc_file):
    print("Committing DVC tracking file to Git...")
    try:
        subprocess.run(["git", "add", dvc_file, "data/raw/.gitignore"], check=True)
        subprocess.run(["git", "commit", "-m", "Tracked dataset with DVC"], check=True)
        print("Changes committed to Git.")
    except Exception as e:
        print("Error committing to Git:", e)
else:
    print(f"No DVC file found at '{dvc_file}'. Skipping Git commit.")

# Step 5: Push Data to DVC Remote
print("Pushing data to DVC remote...")
try:
    push_to_remote()
    print("Data pushed to DVC remote successfully.")
except Exception as e:
    print("Error pushing data to DVC remote:", e)

# Step 6: Verify DVC Pipeline
print("Verifying DVC pipeline (listing DVC-tracked files)...")
try:
    result = subprocess.run(["dvc", "status"], capture_output=True, text=True, check=True)
    print(result.stdout)
except Exception as e:
    print("Error verifying DVC pipeline:", e)
