from functions import get_file_path

file_path = get_file_path()  # getting file path

with open(file_path) as f:  # reading data from source file
    lines = [line.rstrip() for line in f]

labels = ['DC', 'host', 'serial', 'age', 'reads', 'writes', 'latency', 'read_err', 'write_err']  # list of label for creating dictionary
disk_data = []  # list to be populated with data

for line in lines:
    splitted_line = line.split(';')
    zipped = zip(labels, splitted_line)  # dictionary zipped represents one row of disk_data list
    disk_data.append(zipped)  # populating disk_data list with data

print('Total number of disks: ', len(disk_data))