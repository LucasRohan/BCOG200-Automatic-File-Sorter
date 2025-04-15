# Auto detect text files aad perform LF normalization
* text=auto

DOCUMENTS = ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.rtf']
IMAGES = ['.jpg', '.jpeg', '.gif', '.png', '.bmp', '.tiff', '.webp']
VIDEOS = ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv']

### Functions

###     def scan_dir -- Scans directory and creates a list of all_dir_files. all_dir_files will be a tuple containing (direcotry_path, file).
def scan_directory(directory_path):
    file_list = []
    for file in ###directory wanted:
        path of file = ___ 
        if confirmed file 
            file_list.append(file)
    return file_list

###     def get_file_type -- Loops through list of all_dir_files and sorts them into either document_list, image_list, or video_list based on the file extension (.txt, .pdf, .jpeg, .png, .mp4, ...)
def get_file_type(file_name, file_list):
    document_list = []
    image_list = []
    video_list = []
    for file in file_list
        get file extension
            if file ext in DOCUMENTS
                append document_list
            if file ext in IMAGES
                append image_list
            if file exxt in VIDEOS
                append video_list
    return document_list, image_list, video_list

###     def create_subfolders -- Creates subfolders of 'Documents', 'Images', 'Videos', 'Duplicates', 'Log', and 'Other'. Within 'Dupliactes', creates another set of each subfolder excluding 'Duplicates' and 'Log'.
def create_subfolders(directory_path):
    go to wanted directory
        create folder 'Documents'
        create folder 'Images'
        create folder 'Videos'
        create folder 'Duplicate'
        create folder 'Log'
        create folder 'Other'
    go to newly created duplicate folder
        create folder 'Documents'
        create folder 'Images'
        create folder 'Videos'

###     def file_hash -- Gets a hash value for each file and is used later when sorting files to declare whether it is a duplicate or not.
def file_hash(file_path):
    get hash value
        read hash value 
    return hash in string form

###     def sort_files -- Loop through file list and call def file_hash to get the hash value. Make list of hashes. Check if file hash value is in hashes list, if so, duplicate is found and put file into duplicate folder, if not, call def get_file_type and sort into that subfolder. Have action list. Append action list each time a file is moved and provide info of what file was located where and where it was moved to.
def sort_files(file_list, directory_path):
    hashes = {}
    duplicates = []
    actions = []
    
    for each file in file_list:
        ___ = call file_hash(file)

        if ___ in hashes
            ### duplicate found
            move file to duplicates folder
            append duplicates
                ### must sort duplicates file later
        else:
            ### not a duplicate
            call get_file_type(file)
            get destination folder path
            move file to destination
            append actions "moved ___ to {file_type}"

    return duplicates, actions

###     def prompt_user_deletion -- Tells user duplicate(s) have been found. Print each file name and ask if dupliate should be deleted (yes/no). If yes, remove duplicate from directory. If no, do nothing.
def prompt_user_deletion(directory_path, duplicates, actions):
    tell user duplicates have been found
    for file in duplicates
        print duplicate file
        ask user if they want the file to be deleted (yes/no) ### use quotes
            if yes
                remove the file / path 
                print duplicate deleted
                append actions
            if no
                print duplicate not deleted
                append actions

###     def log_actions -- Keeps track of all file movements from x to y with timestamps. Tracks each file movement as "Moved (file) from X to Y" or "Removed duplicate (file)"
def log_actions(directory_path, all_actions):
    access log folder
    create log document
    get timestamp 
    for action in actions:
        write action in log document

###     def main -- Gets input of directory path from user.
def main():
    directory_path = get directory by asking user for input with full path to directory
    create_subfolders(directory_path)
    file_list = scan_directory(directory_path)
    duplicates, actions = sort_files(file_list, directory_path)

    delete_actions = []
    all actions = actions + delete_actions
    pompt delete = prompt_user_deletion(directory_path, duplicates, actions)
        if something deleted
            append delete_actions
    log_actions(directory, all actions)
    print completion

            

if __name__ == "__main__":
    main()