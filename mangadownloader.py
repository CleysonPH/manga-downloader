import click

from manga_downloader.manga import Manga
from manga_downloader.exceptions import MangaNotFound, ChapterNotFound


@click.command()
@click.option('--manga', default='Kimetsu no Yaiba', prompt='Manga', help='Name of the manga you want to download')
@click.option('--chapter', default='All', prompt='Chapter', help='Number of the chapter you want to download')
def manga_downloader(manga, chapter):
    try:
        m = Manga(manga)

        if chapter == 'All':
            m.download_all_chapters()
        else:
            m.download_chapter(float(chapter))
    except MangaNotFound:
        click.echo('Manga {} not found'.format(manga))
    except ValueError:
        click.echo('Chapter must be a number')
    except ChapterNotFound:
        click.echo('Chapter {} of {} is not found.'.format(chapter, manga))


if __name__ == "__main__":
    manga_downloader()