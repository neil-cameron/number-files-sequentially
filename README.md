# Number Files Sequentially

A script that takes the path to several files (or a directory of files) and prepends a serial number to the start of each file name. The number of digits to prepend can be specified at runtime and the oldest file is given the first serial number.

## Usage:

number_files_sequentially.py [-h] [-n NUMBER_OF_DIGITS] file_path [file_path ...]

## Positional Arguments:

file_path

A full or relative path to a file, several files or a directory of files to sequentially number.


## Optional Arguments:

-n NUMBER_DIGITS, --number_digits NUMBER_DIGITS

The number of digits in the serial number to prepend. Default = 2

-h, --help

Show this help message and exit