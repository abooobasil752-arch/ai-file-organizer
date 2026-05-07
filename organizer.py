import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".html"]
}

for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(downloads_folder, folder)

                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))

                print(f"Moved: {filename} -> {folder}")
