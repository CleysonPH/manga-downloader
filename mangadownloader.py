import click

from manga_downloader.manga import Manga
from manga_downloader.exceptions import MangaNotFound, ChapterNotFound


@click.command()
@click.option('--manga', required=True, prompt='Manga', help='Name of the manga you want to download')
@click.option('--chapter', required=False, default=1, type=str, help='Number of the chapter you want to download')
@click.option('--all', is_flag=True, help='Download all the chapters')
@click.option('--last', is_flag=True, help='Download the last chapter')
def manga_downloader(manga, chapter, all, last):
    try:
        m = Manga(manga)
        click.echo('Title: {}'.format(m.name))
        click.echo('Genres: {}'.format(m.genres))
        click.echo('Author: {}'.format(m.author))
        click.echo('Artist: {}'.format(m.artist))
        click.echo('Status: {}'.format(m.status))

        if all:
            m.download_all_chapters()
        elif last:
            m.download_last_chapter()
        else:
            m.download_chapter(chapter)
    except MangaNotFound:
        click.echo('Manga {} not found'.format(manga))
    except ChapterNotFound:
        click.echo('Chapter {} of {} is not found.'.format(chapter, manga))


if __name__ == "__main__":
    manga_downloader()
