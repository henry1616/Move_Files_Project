import os
import shutil

def copy_folders_from_list(file_path, source_folder, destination_folder):
    with open(file_path, 'r') as file:
        folders = file.readlines()
    
    for folder in folders:
        folder = folder.strip()  # Remove leading/trailing whitespaces and newlines
        source_path = os.path.join(source_folder, folder)  # Get the full source path
        destination_path = os.path.join(destination_folder, folder)  # Get the full destination path
        
        copy_folder(source_path, destination_path)

def copy_folder(source_folder, destination_folder):
    try:
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' copied successfully.")
    except shutil.Error as e:
        print(f"Folder copy failed: {e}")
    except OSError as e:
        print(f"Folder copy failed: {e}")

# Example usage
file_path = 'file_names.txt'
source_folder = input('Source folder: ')
destination_folder = input('Destination folder: ')

copy_folders_from_list(file_path, source_folder, destination_folder)
