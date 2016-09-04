import os


def rename_files():
    # 1. Get file names from images/ folder
    file_names = os.listdir(r"images/")
    print file_names

    # 2. For each file name, delete the numbers from the string


rename_files()
