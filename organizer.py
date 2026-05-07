import os
import shutil

downloads_folder = os.path.expanduser("~/Downloads")

file_types = {

    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".svg",
        ".webp", ".bmp", ".tiff"
    ],

    "Documents": [
        ".pdf", ".docx", ".doc", ".txt",
        ".ppt", ".pptx", ".xls", ".xlsx",
        ".odt", ".csv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm"
    ],

    "Audio": [
        ".mp3", ".wav", ".ogg", ".flac",
        ".aac", ".m4a"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    ],

    "Code": [
        ".py", ".js", ".html", ".css",
        ".cpp", ".c", ".java", ".php",
        ".ts", ".jsx", ".json", ".xml",
        ".sh", ".go", ".rs"
    ],

    "Applications": [
        ".deb", ".AppImage", ".exe",
        ".msi"
    ],

    "Fonts": [
        ".ttf", ".otf", ".woff"
    ]
}

print("\n==============================")
print(" AI File Organizer Started")
print("==============================\n")

moved_files = 0

for filename in os.listdir(downloads_folder):

    file_path = os.path.join(downloads_folder, filename)

    if os.path.isfile(file_path):

        moved = False

        for folder, extensions in file_types.items():

            if filename.lower().endswith(tuple(ext.lower() for ext in extensions)):

                folder_path = os.path.join(downloads_folder, folder)

                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))

                print(f"Moved: {filename}  -->  {folder}")

                moved = True
                moved_files += 1
                break

        if not moved:

            other_folder = os.path.join(downloads_folder, "Others")

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(other_folder, filename))

            print(f"Moved: {filename}  -->  Others")

            moved_files += 1

print("\n==============================")
print(f" Organization Complete!")
print(f" Total Files Organized: {moved_files}")
print("==============================")
