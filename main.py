import os
import hashlib
import shutil
import datetime
import csv

DOCUMENTS = ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.rtf']
IMAGES = ['.jpg', '.jpeg', '.gif', '.png', '.bmp', '.tiff', '.webp']
VIDEOS = ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv']

### Scans directory and creates a list of all files and subfolders. Returns list
# of all files and subfolders.
def scan_directory(directory_path):
    file_list = []
    subdirectory_list = []

    try:
        for item in sorted(os.listdir(directory_path)):
            item_path = os.path.join(directory_path, item)

            if os.path.isfile(item_path):
                file_list.append(item_path)

            elif os.path.isdir(item_path):
                subdirectory_list.append(item_path)
                sub_files, subdirectories = scan_directory(item_path)
                file_list.extend(sub_files)
                subdirectory_list.extend(subdirectories)

    except Exception as e:
        print(f'❌ Error scanning directory: {e}')

    return file_list, subdirectory_list

### Loops through list of files and sorts them into categorizeds lists based on
# the file extension. Returns categorized lists.
def get_file_type(file_list):
    document_list = []
    image_list = []
    video_list = []
    other_list = []

    for file in file_list:
        file_ext = os.path.splitext(file)[1].lower()

        if file_ext in DOCUMENTS:
            document_list.append(file)
        elif file_ext in IMAGES:
            image_list.append(file)
        elif file_ext in VIDEOS:
            video_list.append(file)
        else:
            other_list.append(file)

    return document_list, image_list, video_list, other_list

### Creates categorized subfolders in directory. Creates a second set of
# categorized subfolders in duplicate folder exluding duplicate and log folders.
def create_subfolders(directory_path):
    try:
        folders = ['Documents', 'Images', 'Videos', 'Other', 'Duplicate', 'Log']
        for folder in folders:
            os.makedirs(os.path.join(directory_path, folder), exist_ok=True)

        dup_folder_path = os.path.join(directory_path, 'Duplicate')
        dup_folders = ['Documents', 'Images', 'Videos', 'Other']
        for sub_folder in dup_folders:
            os.makedirs(os.path.join(dup_folder_path, sub_folder), exist_ok=True)

        return dup_folder_path

    except Exception as e:
        print(f'❌ Error creating folders: {e}')
        raise

### Gets a hash value for a file passed. Returns a tuple containing the file and
# its hash value.
def get_file_hash(file, algorithm='sha256'):
    try:
        hash_function = hashlib.new(algorithm)

        with open(file, 'rb') as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                hash_function.update(chunk)

        hash = hash_function.hexdigest()
        file_hash_tuple = (file, hash)

        return file_hash_tuple

    except Exception as e:
        print(f'❌ Failed to hash file: {file}: {e}')
        return (file, None)

### Used an online resource to help me get the hashes and learn how to read
# files efficiently in chunks.
### 8192 Bytes = 8 Kilobytes. Good convention for file reading.
### Link: https://www.geeksforgeeks.org/python-program-to-find-hash-of-file/

### Loop through all files and gets a hash value for each. Put all hash values
# in a list to loop through to detect duplicate files. If a duplicate is
# detected, find which file category list it is in, and move the file to that
# duplicate folder. If not a duplicate, move find which file category list it is
# in, and move the file to that folder. After each file is moved, log where it
# was moved from and where it was moved to into actions list. Return list of
# duplicates and list of actions.
def sort_files(file_list, directory_path, dup_folder_path, document_list, image_list, video_list, other_list):
    files_with_hashes = []
    seen_hashes = {}
    duplicates = []
    actions = []
    
    for file in file_list:
        file_hash_tuple = get_file_hash(file)
        if file_hash_tuple[1] is None:
            continue
        files_with_hashes.append(file_hash_tuple)

    for file, hash in files_with_hashes:

        if hash in seen_hashes:
            ### duplicate found

            if file in document_list:
                target_folder = os.path.join(dup_folder_path, 'Documents')
            elif file in image_list:
                target_folder = os.path.join(dup_folder_path, 'Images')
            elif file in video_list:
                target_folder = os.path.join(dup_folder_path, 'Videos')
            else:
                target_folder = os.path.join(dup_folder_path, 'Other')

            target_path = os.path.join(target_folder, os.path.basename(file))

            try:
                shutil.move(file, target_path)
                duplicates.append(target_path)
                actions.append(f'{file}: Moved to {target_path}.')
            except Exception as e:
                print(f'❌ Error moving duplicate file: {file}: {e}')

        else:
            ### not a duplicate
            seen_hashes[hash] = file

            if file in document_list:
                target_folder = os.path.join(directory_path, 'Documents')
            elif file in image_list:
                target_folder = os.path.join(directory_path, 'Images')
            elif file in video_list:
                target_folder = os.path.join(directory_path, 'Videos')
            else:
                target_folder = os.path.join(directory_path, 'Other')
            
            target_path = os.path.join(target_folder, os.path.basename(file))

            try:
                shutil.move(file, target_path)
                actions.append(f'{file}: Moved to {target_path}')
            except Exception as e:
                print(f'❌ Error moving file: {file}: {e}')
                actions.append(f'{file}: Error moving file: {e}')

    return duplicates, actions

### Tell user duplicate(s) have been found. Ask user if they want to delete all
# of them. If yes, delete all, if no, ask if they want to delete each file, one
# by one. If user wants to delete a duplicate file, remove duplicate file from
# directory, if not, do nothing. Log whether each file was deleted or not.
def prompt_user_deletion(directory_path, duplicates, actions):
    print('\n' + '=' * 60)
    print('🧹 Duplicate File Cleanup')
    print(f'🔍 {len(duplicates)} duplicate file(s) detected')
    print('\n' + '=' * 60)

    delete_all = False
    deleted_count = 0
    kept_count = 0
    skipped_count = 0

    user_delete_all = input('❔ Do you want to delete ALL duplicate files? Answer "yes" or "no":  ').strip().lower()
    
    if user_delete_all == 'yes':
        delete_all = True

    for file in duplicates:
        filename = os.path.basename(file)
        print('\n' + '-' * 20)
        print(f'📁 Duplicate file: {filename}')

        if not delete_all:
            user_input = input('🗑️ Do you want to delete this file? Answer "yes" or "no":  ').strip().lower()
        else:
            user_input = 'yes'

        if user_input == 'yes':
            try:
                os.remove(file)
                print(f'\n🗑️ Duplicate deleted: {filename}')
                actions.append(f'{file}: Duplicate Deleted.')
                deleted_count += 1
            except Exception as e:
                print(f'\n❌ Error deleting file: {file}: {e}')
                actions.append(f'{file}: Failed to delete due to error: {e}')
                skipped_count += 1

        elif user_input == 'no':
            print (f'\n📎 Duplicate Kept: {filename}')
            actions.append(f'{file}: Duplicate Kept.')
            kept_count +=1

        else:
            print(f'\n🛑 Invalid input. Skipped: {filename}')
            actions.append(f'{file}: Skipped duplicate deletion choice due to invalid input.')
            skipped_count += 1

    print('\n' + '=' * 60)
    print('📋 Duplicate Deletion Summary:')
    print(f'🗑️ Deleted: {deleted_count}')
    print(f'📎 Kept: {kept_count}')
    print(f'🛑 Skipped: {skipped_count}')
    print('\n' + '=' * 60)

### Goes into log folder, creates .csv file. Writes a header, each action, and
# timestamp in the .csv file.
def log_actions(directory_path, actions):
    try:
        log_folder = os.path.join(directory_path, 'Log')
        os.makedirs(log_folder, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H-%M")
        log_file_path = os.path.join(log_folder, f'Log_{timestamp}.csv')

        with open(log_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(f'Log created on {timestamp}\n')
            writer.writerow(['Actions:\n'])

            for action in actions:
                writer.writerow([action])

    except Exception as e:
        print(f'❌ Error writing log file: {e}')

### Gets input of directory path from user. Runs all functions. Prints summary
# statistics when sorting, duplicate deletion, and logging is complete.
def main():
    print('\n' + '=' * 60)
    print('Enter full path to directory you want to sort.')
    print('Example: /Users/Name/Folder1/Folder2/Folder3...')
    directory_path = input('\nYour directory path here:  ')
    if not os.path.isdir(directory_path):
        print('❌ Error: Directory path entered does not exist or is formatted incorrectly')
        return

    try:
        dup_folder_path = create_subfolders(directory_path)

        file_list, subdirectory_list = scan_directory(directory_path)
        document_list, image_list, video_list, other_list = get_file_type(file_list)
        duplicates, actions = sort_files(file_list, directory_path, dup_folder_path, document_list, image_list, video_list, other_list)

        prompt_user_deletion(directory_path, duplicates, actions)

        log_actions(directory_path, actions)

        print('\n' + '=' * 60)
        print('✅ File Sorting Complete!')
        print('📂 All actions logged in "Log" folder')
        print('=' * 60)

    except Exception as e:
        print(f'❌ Unexpected error: {e}')

    print('\n' + '=' * 60)
    print('📋 Final Summary')
    print('-' * 60)
    print(f' Total files scanned:       {len(file_list)}')
    print(f' Duplicates detected:       {len(duplicates)}')
    print(f' Actions recorded:          {len(actions)}')
    print('-' * 60)
    print("🥳 Done! You may now close this window.")
    print('-' * 60 + '\n')

if __name__ == "__main__":
    main()