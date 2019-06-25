import os
from sys import argv
from collections import defaultdict


def get_files_info(folder_path):
    files_info = defaultdict(list)
    for direction, _, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(direction, filename)
            size = os.path.getsize(filepath)
            files_info[filename, size].append(filepath)
    return files_info


def get_duplicates(files_info):
    duplicates = []
    for (_, _), path in files_info.items():
        if len(path) > 1:
            duplicates.append(path)
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

    files_info = get_files_info(folder_path)
    duplicates = get_duplicates(files_info)
    show_duplicates(duplicates)
