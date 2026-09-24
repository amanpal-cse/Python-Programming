import os
import shutil

folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt"],
    "PDF": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Programs": [".py", ".c", ".cpp", ".java"]
}

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                new_folder = os.path.join(folder, folder_name)

                if not os.path.exists(new_folder):
                    os.mkdir(new_folder)

                shutil.move(file_path,
                            os.path.join(new_folder, file))

                print(file, "->", folder_name)
                break

print("File organization completed!")