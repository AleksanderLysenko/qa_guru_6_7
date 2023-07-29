import os
from zipfile import ZipFile, ZIP_DEFLATED

from tests.conftest import resources_path, tmp_path

file_dir = os.listdir(resources_path)
print(file_dir)


def test_create_zip_archive():
    with ZipFile(os.path.join(tmp_path, 'test.zip'), mode='w', compression=ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(resources_path, file)
            zf.write(add_file)

    assert os.path.exists(os.path.join(tmp_path, 'test.zip'))


def test_check_zip_archive():
    name = []
    with ZipFile(os.path.join(tmp_path, 'test.zip'), mode='a') as zf:
        for file in zf.infolist():
            name.append(os.path.basename(file.filename))

    assert name == file_dir

    os.remove(os.path.join(tmp_path, 'test.zip'))

