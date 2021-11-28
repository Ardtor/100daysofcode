# File and File path handling
import os

# Absolute vs Relative File paths.
# D:\Python\100daysofcode\Day 24\day_24_file_path_handling.py is my Absolute file path
# ./day_24_file_path_handling.py would be my relative file path as my Current Working directory (CWD) is currently D:\Python\100daysofcode\Day 24\

#relative file opening for a test file two folders down from this folder
with open (".\File_path_test\File_path_test_2\my_file.txt", "r") as nf:
    print(nf.read())

