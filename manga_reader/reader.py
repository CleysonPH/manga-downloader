import os
import webbrowser

from jinja2 import Environment, FileSystemLoader


class Reader(object):
    def __init__(self, chapter, file_loader='manga_reader/templates', template='reader.html'):
        self.chapter = chapter
        self.file_loader = FileSystemLoader(file_loader)
        self.env = Environment(loader=self.file_loader)
        self.template = self.env.get_template(template)

    def make_reader_file(self):
        html = self.template.render(chapter=self.chapter)
        file_name = str(self.chapter.chapter_number) + '.html'
        output_file = os.path.join(self.chapter.download_path, file_name,)

        with open(output_file, 'w') as file:
            file.write(html)

        webbrowser.open(os.path.realpath(output_file))
