import os
import pytest
from main import scan_directory, get_file_type, file_hash, DOCUMENTS, IMAGES, VIDEOS

test_pkg = '/Users/lucasrohan/Documents/BCOG200/Final_Project/BCOG-Automatic-File-Sorter/Test/test_pkg'

def test_confirm_scanned_file_list():
    expected_files = []
    for file in os.listdir(test_pkg):
        if os.path.isfile(os.path.join(test_pkg, file)):
            expected_files.append((test_pkg, file))

    file_list = scan_directory(test_pkg)
    result_files = file_list
    ### Calls scan_directory() from main.py

    assert set(result_files) == set(expected_files)


def test_confirm_file_type():
    expected_files = []
    for file in os.listdir(test_pkg):
        if os.path.isfile(os.path.join(test_pkg, file)):
            expected_files.append((test_pkg, file))

    document_list, image_list, video_list = get_file_type(expected_files)
    ### Calls get_file_type() from main.py

    for file in expected_files:
        file_path = os.path.join(test_pkg, file)
        file_ext = os.path.splitext(file)[1]

        if file_ext in DOCUMENTS:
            assert file in document_list
            print(f'{file} should be categorized in Documents correctly.')

        elif file_ext in IMAGES:
            assert file in image_list
            print(f'{file} should be categorized in Images correctly.')

        elif file_ext in VIDEOS:
            assert file in video_list
            print(f'{file} should be categorized in Videos correctly.')

        else:
            print(f'{file}: Unkown file type')


def test_hash_duplicates():
    test_file_1 = os.path.join(test_pkg, 'test_image_1')
    test_file_2 = os.path.join(test_pkg, 'test_image_1_copy')

    assert os.path.exists(test_file_1)
    assert os.path.exists(test_file_2)

    test_file_1_hash = file_hash(test_file_1)
    test_file_2_hash = file_hash(test_file_2)
    ### Calls file_hash() from main.py

    assert test_file_1_hash == test_file_2_hash, 'Hashes do not match. Duplicate not found.'

### Run using pytest test_duplicates.py