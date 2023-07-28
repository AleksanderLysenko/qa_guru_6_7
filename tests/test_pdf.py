import os

from pypdf import PdfReader

from tests.conftest import resources_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_pdf_read():
    reader = PdfReader(os.path.join(resources_path, "docs-pytest-org-en-latest.pdf"))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412
    assert 'https://merlinux.eu/' in text
