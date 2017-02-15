import sys
import os
import time
import shutil
import argparse
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

def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--routes", help="enter routes here seperated by ,")
    return parser.parse_args()

class WebProjectFlask:

    def __init__(self, fname):
        self.folder_name = fname
        pass

    def create_route(self, rname):
        write2file(Ft.route % (rname, rname), '{}/ramp_routes.py'.format(self.folder_name))
        write2file(Ft.resource % (rname, rname), '{}/app.py'.format(self.folder_name))

    def create_appPy(self):
        write2file(Ft.header+Ft.index_func, '{0}/app.py'.format(self.folder_name))

    def create_index(self):
        os.mkdir('{}/templates/'.format(self.folder_name))
        write2file(templates.index_page, '{}/templates/index.html'.format(self.folder_name))

    def create_project(self, arg_arr):
        self.create_appPy()
        write2file(Ft.rr_import, '{}/ramp_routes.py'.format(self.folder_name))
        [self.create_route(a) for a in arg_arr]
        write2file(Ft.if_main, '{}/app.py'.format(self.folder_name))
        self.create_index()
        os.mkdir('{}/static'.format(self.folder_name))
        os.system("cp -rv code-prettify/* {}/static/.".format(self.folder_name))

#if __name__ == '__main__':
#    cleanup()
#    args = check_args()
#    aArr = args.routes.split(',')
#    project = WebProjectFlask()
#    project.create_project(aArr)
