import os

folder = "Aman_C"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")
else:
    print("Folder already exists")