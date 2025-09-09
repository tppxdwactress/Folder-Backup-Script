# Folder Backup Script

This repository contains a simple Python script to back up a specific folder by zipping it and adding a timestamp to the filename.

## Features

- Backs up any directory you specify
- Output is a ZIP file with the current date and time in its name
- Optionally choose an output directory for backups

## Usage

```bash
python backup_folder_with_timestamp.py /path/to/folder [optional/output/folder]
```

- `/path/to/folder`: The folder you want to back up.
- `[optional/output/folder]`: (Optional) Directory where the ZIP file will be saved. If not provided, the ZIP is created next to the original folder.

## Example

```bash
python backup_folder_with_timestamp.py ~/Documents/important_files ~/Backups
```

This will create a ZIP file like `important_files_backup_20250909_193808.zip` inside the `~/Backups` directory.

## Requirements

- Python 3.x

No external dependencies are required.

## License

This project is licensed under the MIT License.
