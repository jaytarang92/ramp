import web_gen as wg
import sys

routes = []

def main():
    while True:
        route = raw_input("What would you like you name your route? : ")
        if  route == '' or int(route[0]):
            print 'Sorry try again using a string!'
            route
        elif route != '' and route != 'quit':
            routes.append(route)
        elif route == 'quit':
            print "Thanks for using the generator!"
            break
        else:
            print 'Sorry try again using a string!'
            route
    wg.cleanup()
    project = wg.WebProjectFlask()
    project.create_project(routes)

if __name__ == '__main__':
    main()
