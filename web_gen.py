import os
import time
import shutil
import templates
from templates import FlaskStuff as Ft

test_mode = True


def cleanup():
    if test_mode and os.path.exists('output'):
        shutil.rmtree('output')
        os.mkdir('output')
        os.mkdir('output/templates')


def write2file(content, file_name):
    with open(file_name, 'ab') as new_file:
        new_file.write(content)
        '''
        for c in content.split('\n'):
            if c.rstrip():
                new_file.write(c + '\n')
        '''


class WebProjectFlask:

    def __init__(self):
        pass

    def create_flask(self):
        route = ('crap', 'crap', 'crap', 'crap')
        write2file(templates.index_page, 'output/templates/index.html')
        write2file(Ft.header+Ft.index_func+Ft.route % route+Ft.if_main, 'output/app.py')


if __name__ == '__main__':
    cleanup()
    project = WebProjectFlask()
    project.create_flask()