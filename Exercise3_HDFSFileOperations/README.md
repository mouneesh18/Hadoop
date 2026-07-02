# Exercise 3 - HDFS File Operations

## Objective
Perform file operations in Hadoop Distributed File System (HDFS) using text files.

## Files
- sample1.txt
- sample2.txt
- sample3.txt

## Operations Performed
1. Created three text files
2. Created an HDFS directory
3. Uploaded files into HDFS
4. Listed files in HDFS
5. Displayed file contents
6. Copied a file in HDFS
7. Renamed a file in HDFS
8. Downloaded a file from HDFS
9. Deleted a file from HDFS

## HDFS Commands Used

Create directory:
hdfs dfs -mkdir -p /user/$USER/exercise3/input

Upload files:
hdfs dfs -put sample1.txt /user/$USER/exercise3/input/
hdfs dfs -put sample2.txt /user/$USER/exercise3/input/
hdfs dfs -put sample3.txt /user/$USER/exercise3/input/

List files:
hdfs dfs -ls /user/$USER/exercise3/input

View contents:
hdfs dfs -cat /user/$USER/exercise3/input/sample1.txt
hdfs dfs -cat /user/$USER/exercise3/input/sample2.txt
hdfs dfs -cat /user/$USER/exercise3/input/sample3.txt

Copy file:
hdfs dfs -cp /user/$USER/exercise3/input/sample1.txt /user/$USER/exercise3/input/sample1_copy.txt

Rename file:
hdfs dfs -mv /user/$USER/exercise3/input/sample2.txt /user/$USER/exercise3/input/sample2_renamed.txt

Download file:
hdfs dfs -get /user/$USER/exercise3/input/sample3.txt downloaded_files/

Delete file:
hdfs dfs -rm /user/$USER/exercise3/input/sample1_copy.txt

## Result
Successfully performed HDFS file operations including creating, uploading, listing, viewing, copying, renaming, downloading, and deleting files.
