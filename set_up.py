#!/usr/bin/env python

import os

class DirectoryHandler(object):
    """docstring for DirectoryHandler."""
    def __init__(self):
        super(DirectoryHandler, self).__init__()
    def get_home_directory(self):
        return os.path.expanduser('~')
    def get_set_up_directory(self):
        return os.path.dirname(os.path.realpath(__file__))
    def get_home_dot_files_directory(self):
        return os.path.join(self.get_set_up_directory(), 'home_dot_files')

class Booter(object):
    """docstring for Booter."""
    def __init__(self, directory_handler):
        super(Booter, self).__init__()
        self.directory_handler = directory_handler
    def copy_home_dot_files(self):
        pass
    def set_up(self):
        self.copy_home_dot_files()
        print 'Copied home dot files'



def main():
    print 'hello'

if __name__ == "__main__":
    main()
