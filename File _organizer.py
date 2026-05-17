import os
import shutil

path = input("Enter folder path: ")

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    extension = extension.lower()

    if extension in [".jpg", ".png", ".jpeg"]:
        folder = "Images"

    elif extension in [".pdf", ".docx", ".txt"]:
        folder = "Documents"

    elif extension in [".mp4", ".mkv"]:
        folder = "Videos"

    else:
        folder = "Others"

    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    source = os.path.join(path, file)
    destination = os.path.join(folder_path, file)

    if os.path.isfile(source):
        shutil.move(source, destination)

print("Files organized successfully!")
