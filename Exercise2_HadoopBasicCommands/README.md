# Experiment 2 - Hadoop Basic Commands

## Objective
To understand and execute basic Hadoop HDFS commands for file and directory management.

## Tasks Performed
1. Created an HDFS directory
2. Uploaded local files to HDFS
3. Listed files and directories in HDFS
4. Viewed file contents using HDFS
5. Downloaded a file from HDFS to the local system

## Local Files
- students.txt
- courses.txt

## HDFS Commands Used

Create directory:
hdfs dfs -mkdir -p /user/$USER/experiment2/input

Upload files:
hdfs dfs -put students.txt /user/$USER/experiment2/input/
hdfs dfs -put courses.txt /user/$USER/experiment2/input/

List files:
hdfs dfs -ls /user/$USER/experiment2/input

View contents:
hdfs dfs -cat /user/$USER/experiment2/input/students.txt
hdfs dfs -cat /user/$USER/experiment2/input/courses.txt

Download file:
hdfs dfs -get /user/$USER/experiment2/input/students.txt downloaded_files/

## Result
Successfully performed basic HDFS file and directory operations.
