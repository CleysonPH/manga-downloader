import os

import requests
from bs4 import BeautifulSoup

from manga_downloader.chapter import Chapter


class Manga(object):

    def __init__(self, name):
        self.name = name
        self.link = 'https://unionleitor.top/manga/{}'.format(
            self.name.replace(' ', '-').lower())
        self.soup = BeautifulSoup(requests.get(
            self.link).content, 'html.parser')
        self.author = ''
        self.artist = ''
        self.status = ''
        self.chapters = []

        self._get_perfil_data()
        self._get_chapters()

    def _get_perfil_data(self):
        perfil_data = self.soup.find_all(
            'h4', class_='media-heading manga-perfil')

        self.author = perfil_data[2].text.split(':')[-1].strip()
        self.artist = perfil_data[3].text.split(':')[-1].strip()
        self.status = perfil_data[4].text.split(':')[-1].strip()

    def _get_chapters(self):
        caps = self.soup.find_all('div', class_='row lancamento-linha')
        for cap in caps:
            chapter_number = cap.find('a').get('href')
            self.chapters.append(
                Chapter(self.name, chapter_number)
            )

    def download_all_chapters(self):
        for chapter in self.chapters:
            chapter.download_chapter()

    def download_chapter(self, chapter_number):
        for chapter in self.chapters:
            if chapter.chapter_number == chapter_number:
                chapter.download_chapter()
