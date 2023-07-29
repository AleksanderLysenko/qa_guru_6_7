import csv
import os

from tests.conftest import resources_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_create_csv():
    with open(os.path.join(resources_path, 'eggs.csv'), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    assert os.path.exists(os.path.join(resources_path, 'eggs.csv'))


def test_read_row_csv():
    with open(os.path.join(resources_path, 'eggs.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
    assert len(row) == 3

    os.remove(os.path.join(resources_path, 'eggs.csv'))

