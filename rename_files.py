import os


def rename_files():
    # 1. Find the images directory and get into it
    cwd = os.getcwd()
    files_dir = cwd + "/images"
    os.chdir(files_dir)

    # 2. Get file names from images/ folder
    file_list = os.listdir(".")
    # print file_list

    # 3. For each file name, delete the numbers from it
    rename_count = 0

    for file_name in file_list:
        old_name = file_name
        new_name = file_name.translate(None, "0123456789")

        print "Renaming file \"" + old_name + "\" to \"" + new_name + "\""

        os.rename(old_name, new_name)

        rename_count += 1

    print ""
    print "Finished: " + rename_count.__str__() + " files renamed"


rename_files()
