from functions import get_file_path

file_path = get_file_path()  # getting file path

with open(file_path) as f:  # reading data from source file
    lines = [line.rstrip() for line in f]

disk_data = []  # list to be populated with data

for line in lines:
    splitted_line = line.split(';')
    disk_data.append(splitted_line)  # populating disk_data list with data

print('Total number of disks: ', len(disk_data))  # counts and print total number on disks


