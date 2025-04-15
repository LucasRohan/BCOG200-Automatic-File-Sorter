# BCOG200-Automatic-File-Sorter
### Final Project


### Brief 3-5 sentence description of planned Project

###     My computer files are a mess because I usually dump them into the same directory each time as sorting them manually often takes way too long. To solve this, I want to create an automatic file sorter. One that can scan a directory and sort each file into pre-made or new sub-folders for each type of file (image, video, or document). This program will include the ability to remove duplicate files with permission of the user. A log of all actions must also be created and kept in a separate subfolder to track system actions.


### Functions

###     A - Scan directory, create file list.
###     B - Create sub-folders in directory, sort file list. Sub-folders include duplicate/removal list.
###     C - Prompt user and show duplicate / removal list.
###     D - Track each file movement and create log of what file is moved where.

--
### Sales Pitch

###     Is your computer cluttered with different types of files all dumped into the same folder? Everyone know that manually parsing through and organizing files can be excruciatingly time-consuming and tedious so I created Sortify. Sortify is a python-based, automatic file sorter that helps its user sort a cluttered file directory into organized subfolders. Along with arranging files, Sortify detects unwanted duplicates as well as tracks where each file has moved to. Download Sortify and declutter your directories!


### Functions

###     def scan_dir -- Scans directory and creates a list of all_dir_files. all_dir_files will be a tuple containing (direcotry_path, file).
    def scan_directory(directory_path):

###     def get_file_type -- Loops through list of all_dir_files and sorts them into either document_list, image_list, or video_list based on the file extension (.txt, .pdf, .jpeg, .png, .mp4, ...)
    def get_file_type(file_name):

###     def create_subfolders -- Creates subfolders of 'Documents', 'Images', 'Videos', 'Duplicates', 'Log', and 'Other'. Within 'Dupliactes', creates another set of each subfolder excluding 'Duplicates' and 'Log'.
    def create_subfolders(directory_path):

###     def file_hash -- Gets a hash value for each file and is used later when sorting files to declare whether it is a duplicate or not.
    def file_hash(file_path):

###     def sort_files -- Loop through file list and call def file_hash to get the hash value. Make list of hashes. Check if file hash value is in hashes list, if so, duplicate is found and put file into duplicate folder, if not, call def get_file_type and sort into that subfolder. Have action list. Append action list each time a file is moved and provide info of what file was located where and where it was moved to.
    def sort_files(file_list, directory_path):

###     def prompt_user_deletion -- Tells user duplicate(s) have been found. Print each file name and ask if dupliate should be deleted (yes/no). If yes, remove duplicate from directory. If no, do nothing.
    def prompt_user_deletion(directory_path, duplicates):

###     def log_actions -- Keeps track of all file movements from x to y with timestamps. Tracks each file movement as "Moved (file) from X to Y" or "Removed duplicate (file)"
    def log_actions(directory_path, actions):

###     def main -- Gets input of directory path from user.


### Example use cases:

###     1. After downloading images from a homework assignment, lecture slideshows, and a mischealaneous video from the internet, the users downloads folder will be messy and harder to look through it for a specfic file such as one of the lecture slideshows. If it was sorted, it would be quicker easier to find the slideshow needed.

###     2. Sometimes when manually organizing computer files, a file may be accidentally deleted when it wasn't supposed to be. A log for all file actions can retrieve that file and an automated program drastically decreases this probability.


### Data input:

###     Documents: .pdf, .docx, .txt, .doc, .xlsx, .xls, .pptx, .ppt, .rtf
###     Images: .jpg, .jpeg, .gif, .png, .bmp, .tiff, .webp
###     Videos: .mp4, .mov, .avi, .mkv, .wmv, .flv
