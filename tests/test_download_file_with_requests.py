import os.path

import requests

from tests.conftest import tmp_path

url = 'https://selenium.dev/images/selenium_logo_square_green.png'


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
def test_download_with_request():

    response = requests.get(url)
    with open(os.path.join(tmp_path, 'selenium_logo.png',), 'wb') as file:
        file.write(response.content)

    assert os.path.exists(os.path.join(tmp_path, 'selenium_logo.png'))

    size = os.path.getsize(os.path.join(tmp_path, 'selenium_logo.png'))

    assert size == 30803
