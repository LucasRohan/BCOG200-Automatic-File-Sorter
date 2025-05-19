import os
import pytest
from main import scan_directory, get_file_type, get_file_hash, DOCUMENTS, IMAGES, VIDEOS

test_pkg = os.path.join(os.path.dirname(__file__), 'Test', 'test_pkg')

def test_confirm_scanned_file_list():
    expected_files = []
    for file in os.listdir(test_pkg):
        file_path = os.path.join(test_pkg, file)
        if os.path.isfile(file_path):
            expected_files.append(file_path)

    result_files, _ = scan_directory(test_pkg)

    assert set(result_files) == set(expected_files)
    ### Calls scan_directory() from main.py


def test_confirm_file_type():
    expected_files = []
    for file in os.listdir(test_pkg):
        file_path = os.path.join(test_pkg, file)
        if os.path.isfile(file_path):
            expected_files.append(file_path)

    document_list, image_list, video_list, other_list = get_file_type(expected_files)
    ### Calls get_file_type() from main.py

    for file_path in expected_files:
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext in DOCUMENTS:
            assert file_path in document_list
            print(f'{file} should be categorized in Documents correctly.')

        elif file_ext in IMAGES:
            assert file_path in image_list
            print(f'{file} should be categorized in Images correctly.')

        elif file_ext in VIDEOS:
            assert file_path in video_list
            print(f'{file} should be categorized in Videos correctly.')

        else:
            print(f'{file}: Unkown file type')


def test_hash_duplicates():
    test_file_1 = os.path.join(test_pkg, 'test_image_1.jpg')
    test_file_2 = os.path.join(test_pkg, 'test_image_2(duplicate).jpg')

    assert os.path.exists(test_file_1)
    assert os.path.exists(test_file_2)

    _, test_file_1_hash = get_file_hash(test_file_1)
    _, test_file_2_hash = get_file_hash(test_file_2)
    ### Calls get_file_hash() from main.py

    assert test_file_1_hash == test_file_2_hash, 'Hashes do not match. Duplicate not found.'

### Run using pytest test_duplicates.py