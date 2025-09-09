import os
import sys
import zipfile
from datetime import datetime

def zip_folder(folder_path, output_folder=None):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Prepare output zip filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.basename(os.path.normpath(folder_path))
    zip_filename = f"{folder_name}_backup_{timestamp}.zip"
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)
        zip_filepath = os.path.join(output_folder, zip_filename)
    else:
        zip_filepath = os.path.join(os.path.dirname(folder_path), zip_filename)

    # Create the zip file
    with zipfile.ZipFile(zip_filepath, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_file = os.path.join(root, file)
                rel_path = os.path.relpath(abs_file, folder_path)
                zipf.write(abs_file, arcname=os.path.join(folder_name, rel_path))
    print(f"Backup created: {zip_filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup_folder_with_timestamp.py <folder_path> [output_folder]")
        sys.exit(1)
    folder_to_backup = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    zip_folder(folder_to_backup, output_dir)
