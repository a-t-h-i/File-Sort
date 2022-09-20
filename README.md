# File-Sort
A CLI based file sorting program that sorts files based on file extension by creating a folder for the files

Usage:

File-Sort allows you to compress files of a certain (specified) extension into an archive and gives you the option to delete them after the files have been compressed successfully.

That can be done using these commands:

Compress files of specified extension
sort -c <extension> 

Compress files of specified extension and then delete them
sort -cd <extension>


File-Sort also allows you to move files to a folder named with the type of files in it i.e. It can move .png files to a folder named /PNG. It also allows you to move
files to a specified folder

That can be done using these commands:

Move files to a folder with extension name
sort -f <extension>

Move Files to a specified folder
sort -f <extension> <path_to_target_folder>





