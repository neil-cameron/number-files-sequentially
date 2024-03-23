import os
import argparse
from pathlib import Path


def get_creation_time(path):
    return path.stat().st_ctime


def prepend_number_to_filename(path, number, digits):
    parent_dir = path.parent
    prefix = str(number).zfill(digits)
    new_name = f"{prefix} {path.name}"
    return parent_dir / new_name


def process_files(files):
    # Sort files by creation time
    sorted_files = sorted(files, key=get_creation_time)

    # Prepend numbers to file names
    for i, file_path in enumerate(sorted_files, start=1):
        new_file_path = prepend_number_to_filename(file_path, i, digits)
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_path}' to '{new_file_path}'")


# Argparse stuff
parser = argparse.ArgumentParser(
    prog="Number Files Sequentially",
    description="This program takes the path to several files (or a directory of files) and prepends a sequential number to the file name",
)

parser.add_argument(
    "-n",
    "--number_of_digits",
    type=int,
    help="The number of digits to prepend",
    default=2,
)
parser.add_argument(
    "file_path",
    nargs="+",
    help="A full or relative path to a media file, several media files or a directory of media files to transcribe",
)
args = parser.parse_args()

# Parse arguments
digits = args.number_of_digits

argparse_list_of_paths = []
if args.file_path:
    [
        argparse_list_of_paths.append(Path(individual_path))
        for individual_path in args.file_path
    ]

full_file_path_list = []
for individual_path in argparse_list_of_paths:
    if os.path.isdir(individual_path):  # Directory
        for dir_path, dir_names, file_names in os.walk(individual_path):
            for file_name in file_names:
                if not file_name.startswith("."):
                    file_path_found = os.path.join(dir_path, file_name)
                    full_file_path_list.append(Path(file_path_found))
    else:  # File
        full_file_path_list.append(individual_path)


# Perform the renaming
process_files(full_file_path_list)
