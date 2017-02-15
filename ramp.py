import web_gen as wg
import sys
import os
import shutil

routes = []

def main():
    folder = raw_input("Where would you like to put your project?: ")
    folder_name = folder
    if os.path.exists(folder_name):
        print 'Folder exists already. Needs to be removed!'
        overwrite = raw_input("Would like to remove "+folder_name+", and it's contents? : [y/n]")
        if overwrite.lower() == 'y':
            shutil.rmtree(folder_name)
        else:
            print 'Exiting. Please choose another folder name and relaunch!'
            os.exit(1)
    os.mkdir(folder)
    while True:
        route = raw_input("What would you like you name your route? : ")
        #if route == '' or int(route[0]):

        #    print 'Sorry try again using a string!'
        #    route
        if route != '' and route != 'quit':
            routes.append(route)
        elif route == 'quit':
            print "Thanks for using the generator!"
            break
        else:
            print 'Sorry try again using a string!'
            route
    wg.cleanup()
    project = wg.WebProjectFlask(folder_name)
    project.create_project(routes)

if __name__ == '__main__':
    main()
