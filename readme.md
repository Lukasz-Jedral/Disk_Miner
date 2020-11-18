**Disk Miner**

The goal of this task is to prepare statistical analysis of set of data from disks.

Each entry of the data set consists of following fields separated by `;` character:

* datacenter
* hostname
* disk serial
* disk age (in s)
* total reads
* total writes
* average IO latency from 5 minutes (in ms)
* total uncorrected read errors
* total uncorrected write errors

The proper solution (a script in Python) should output following information:

 1. How many disks are in total
 2. How many disks are there in each DC
 3. Which disk is the oldest one and what is its age (in days)
 4. Which disk is the youngest one and what is its age (in days)
 5. What's the average disk age per DC (in days)
 6. How many read IO/s disks processes on average
 7. How many write IO/s disks processes on average
 8. Find top 5 disks with highest average IO/s (reads+writes, print disks and their avg IO/s)
 9. Find top 5 disks with lowest average IO/s (reads+writes, print disks and their avg IO/s)
10. Find disks which are most probably broken, i.e. have non-zero uncorrected errors (print disks and error counter)