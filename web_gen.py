import sys
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
    with open(file_name, 'a+') as new_file:
        new_file.write(content)
        '''
        for c in content.split('\n'):
            if c.rstrip():
                new_file.write(c + '\n')
        '''


class WebProjectFlask:

    def __init__(self):
        pass

    def create_route(self, rname):
        write2file(Ft.route % (rname, rname), 'output/ramp_routes.py')
        write2file(Ft.resource % (rname, rname), 'output/app.py')

    def create_appPy(self):
        write2file(Ft.header+Ft.index_func, 'output/app.py')

    def create_index(self):
        write2file(templates.index_page, 'output/templates/index.html')

    def create_project(self):
        self.create_appPy()
        write2file(Ft.rr_import, 'output/ramp_routes.py')
        for num in range(1, int(sys.argv[1])+1):
            self.create_route(sys.argv[num+1])
        write2file(Ft.if_main, 'output/app.py')
        self.create_index()

if __name__ == '__main__':
    cleanup()
    project = WebProjectFlask()
    project.create_project()
