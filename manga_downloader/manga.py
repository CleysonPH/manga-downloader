import os

import requests
import requests_cache
from bs4 import BeautifulSoup

from config import REQUESTS_SQLITE_CACHE
from manga_downloader.chapter import Chapter
from manga_downloader.exceptions import MangaNotFound, ChapterNotFound


requests_cache.install_cache(REQUESTS_SQLITE_CACHE)


class Manga(object):

    def __init__(self, name):
        self.name = name
        self.link = 'https://unionleitor.top/manga/{}'.format(
            self.name.replace(' ', '-').lower())

        response = requests.get(self.link)
        if not response.history:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            raise MangaNotFound(
                'Manga {} not Found in the Union Mangas website'.format(
                    self.name
                )
            )

        self.author = ''
        self.artist = ''
        self.status = ''
        self.chapters = self._get_chapters()

        self._get_perfil_data()

    def _get_perfil_data(self):
        perfil_data = self.soup.find_all(
            'h4', class_='media-heading manga-perfil')

        self.author = perfil_data[2].text.split(':')[-1].strip()
        self.artist = perfil_data[3].text.split(':')[-1].strip()
        self.status = perfil_data[4].text.split(':')[-1].strip()

    def _get_chapters(self):
        chapter_list = []
        caps = self.soup.find_all('div', class_='row lancamento-linha')
        for cap in caps:
            chapter_number = cap.find('a').get('href')
            chapter_list.append(
                Chapter(self.name, chapter_number)
            )

        return chapter_list

    def download_all_chapters(self):
        for chapter in self.chapters:
            chapter.download_chapter()

    def download_chapter(self, chapter_number):
        found = False
        for chapter in self.chapters:
            if chapter.chapter_number == chapter_number:
                found = True
                chapter.download_chapter()

        if not found:
            raise ChapterNotFound(
                'The chapter {} of {} is not found in the Union Mangas website'.format(
                    chapter_number,
                    self.name
                )
            )
