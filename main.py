from functions import get_file_path, unique_values_from_list

file_path = get_file_path()  # getting file path

with open(file_path) as f:  # reading data from source file
    lines = [line.rstrip() for line in f]

disk_data = []  # list to be populated with data

for line in lines:
    splitted_line = line.split(';')
    raw_row_of_data = []
    for item in splitted_line:  # converting convertible strings into integers
        if item.isdigit():
            raw_row_of_data.append(int(item))
        else:
            raw_row_of_data.append(item)
    disk_data.append(raw_row_of_data)  # populating disk_data list with data

''' 1. How many disks are in total'''
print('Total number of disks: ', len(disk_data), '\n')  # counts and print total number on disks

'''2. How many disks are there in each DC'''
DC_list = [disk[0] for disk in disk_data]  # extracting all dc names from disk_data list
DC_unique = unique_values_from_list(DC_list)  # getting only unique values from DC_list
Disks_in_DC = {}  # empty dict for storing number of disk in each DC

for dc in DC_unique:  # block of code counting number of appearances of dc name in disk data list
    counter = 0

    for entry in disk_data:
        if entry[0] == dc:
            counter += 1
    Disks_in_DC[dc] = counter

'''5. What's the average disk age per DC (in days)'''
avg_age_per_DC = {}
for dc in DC_unique:
    total_age = 0
    single_DC_data = [item for item in disk_data if item[0] == dc]

    for entry in single_DC_data:
        total_age += entry[3]
    avg_age_per_DC[dc] = round((total_age / len(single_DC_data)) / 86400, 2)

print('Disk statistics for each Data Center:')  # presenting results of disk count in each Data Center
print('| DC Name', '| No of disks |', 'Avg age in days |')
for keys, values in Disks_in_DC.items():
    print(keys, ': ', values, '\t', avg_age_per_DC[keys])
print()


'''3. Which disk is the oldest one and what is its age (in days)
   4. Which disk is the youngest one and what is its age (in days)'''
sorted_disk_data = sorted(disk_data, key=lambda value: value[3])  # sort disk_data by disk age
newest = sorted_disk_data[0]  # row of data containing newest disk
oldest = sorted_disk_data[-1]  # row of data containing oldest disk
print('The oldest disk is disk with serial number:', oldest[2], 'from', oldest[0], 'Data Center.',
      'It is', round(oldest[3] / 86400, 2), 'days old.')
print('The newest disk is disk with serial number:', newest[2], 'from', newest[0], 'Data Center.',
      'It is', round(newest[3] / 86400, 2), 'days old.\n')


'''6. How many read IO/s disks processes on average
   7. How many write IO/s disks processes on average
   8. Find top 5 disks with highest average IO/s (reads+writes, print disks and their avg IO/s)
   9. Find top 5 disks with lowest average IO/s (reads+writes, print disks and their avg IO/s)'''
for item in disk_data:
    read_IO_sec = item[4]/item[3]
    item.append(read_IO_sec)  # adding read IO per sec to disk_data list
    write_IO_sec = item[5]/item[3]
    item.append(write_IO_sec)  # adding write IO per sec to disk_data list
    avg_IO = round(((item[9] + item[10]) / 2), 2)  # calculating average IO for each disk
    item.append(avg_IO)

total_reads = sum([entry[9] for entry in disk_data])  # adding all reads IO/s values
total_writes = sum([entry[10] for entry in disk_data])  # adding all write IO/s values

print('Disks are processing', round(total_reads / len(disk_data)), 'read IO/s on average')
print('Disks are processing', round(total_writes / len(disk_data)), 'writes IO/s on average\n')

sorted_disk_data = sorted(disk_data, key=lambda value: value[11])  # sort disk_data by disk average IO
lowest_IO = sorted_disk_data[0:5]  # top 5 lowest avg IO/s
highest_IO = sorted_disk_data[-5:]  # top 5 highest avg IO/s

print('Top 5 disks with lowest average IO/s:\n',
      '| DC Name', '| Disk Serial No. |', 'Avg IO/s |')
for item in lowest_IO:
    print(item[0], item[2], item[11], sep='\t')
print()
print('Top 5 disks with highest average IO/s:\n',
      '| DC Name', '| Disk Serial No. |', 'Avg IO/s |')
for item in highest_IO:
    print(item[0], item[2], item[11], sep='\t')


