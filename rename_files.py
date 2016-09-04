import os


def rename_files():
    # 1. Find the images directory and get into it
    cwd = os.getcwd()
    files_dir = cwd + "/images"
    os.chdir(files_dir)

    # 2. Get file names from images/ folder
    file_list = os.listdir(".")
    print file_list

    # 3. For each file name, delete the numbers from it
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))


rename_files()
