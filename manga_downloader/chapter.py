import os

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class Chapter(object):
    def __init__(self, manga_name, chapter_link):
        self.manga_name = manga_name
        self.chapter_link = chapter_link
        self.chapter_number = float(self.chapter_link.split('/')[-1])

    def download_chapter(self):
        download_path = os.path.join(
            'mangas',
            self.manga_name.replace(' ', '_').lower(),
            str(self.chapter_number),
        )

        self._makedirs(download_path)
        self._download_pages(download_path)

    def _makedirs(self, path):
        os.makedirs(path, exist_ok=True)

    def _download_pages(self, download_path):
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
            response = requests.get(page_link)
            file_path = os.path.join(download_path, file_name)

            with open(file_path, 'wb') as file:
                file.write(response.content)
