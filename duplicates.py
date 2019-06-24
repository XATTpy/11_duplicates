import os
from sys import argv
from collections import Counter


def get_file_names(folder_path):
    file_names = []
    for _, _, filenames in os.walk(folder_path):
        file_names.extend(filenames)
    return file_names


def get_file_names_count(file_names):
    file_names_count = Counter(file_names)
    return file_names_count


def get_same_file_names(file_names_count):
    same_file_names = []
    for filename, filecount in file_names_count.most_common():
        if filecount > 1:
            same_file_names.append(filename)
    return same_file_names


def get_files_info(folder_path, same_file_names):
    files_info = {}
    for direction, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename in same_file_names:
                size = os.path.getsize(direction + "/" + filename)
                filepath = direction + "/" + filename
                files_info.update({filepath: [filename, size]})
    return files_info


def get_duplicates(files_info):
    duplicates = []
    for filepath, fileinfo in files_info.items():
        flag = 0
        for otherpath, otherinfo in files_info.items():
            if filepath != otherpath and fileinfo == otherinfo:
                flag += 1
        if flag > 0:
            duplicates.append(filepath)
    return duplicates


def show_duplicates(duplicates):
    print("These files have duplicat-e/es:")
    for filepath in duplicates:
        print(filepath)


if __name__ == "__main__":
    try:
        folder_path = argv[1]
    except IndexError:
        quit("Enter the path to the folder.")
    if not os.path.isdir(folder_path):
        quit("This folder does not exist.")

    file_names = get_file_names(folder_path)
    file_names_count = get_file_names_count(file_names)
    same_file_names = get_same_file_names(file_names_count)
    files_info = get_files_info(folder_path, same_file_names)
    duplicates = get_duplicates(files_info)
    show_duplicates(duplicates)
