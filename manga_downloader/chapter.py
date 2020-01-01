import os

import requests
import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

from config import REQUESTS_SQLITE_CACHE
from manga_reader.reader import Reader


requests_cache.install_cache(REQUESTS_SQLITE_CACHE)


class Chapter(object):
    def __init__(self, manga_name, chapter_link):
        self.manga_name = manga_name
        self.chapter_link = chapter_link
        self.chapter_number = float(self.chapter_link.split('/')[-1])
        self.download_path = os.path.join(
            'mangas',
            self.manga_name.replace(' ', '_').lower(),
            str(self.chapter_number),
        )
        self.pages = []

    def download_chapter(self):
        self._makedirs()
        self._download_pages()

        r = Reader(self)
        r.make_reader_file()

    def _makedirs(self):
        os.makedirs(self.download_path, exist_ok=True)

    def _download_pages(self):
        print('Downloading chapter {} of {}'.format(
            self.chapter_number,
            self.manga_name)
        )

        soup = BeautifulSoup(requests.get(
            self.chapter_link).content, 'html.parser')
        pages = soup.find_all('img', class_='img-manga')

        # for page_number, page in enumerate(pages, start=1):
        for page_number in tqdm(range(len(pages))):
            page_link = pages[page_number].get('src')
            file_extension = page_link.split('.')[-1]
            file_name = '{}.{}'.format(page_number, file_extension)
            self.pages.append(file_name)
            file_path = os.path.join(self.download_path, file_name)

            if not os.path.exists(file_path):
                response = requests.get(page_link)

                with open(file_path, 'wb') as file:
                    file.write(response.content)
