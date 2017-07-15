#!/usr/bin/env python

import os
import shutil

class DirectoryHandler(object):
    """docstring for DirectoryHandler."""
    def __init__(self):
        super(DirectoryHandler, self).__init__()
    def get_home_directory(self):
        return os.path.expanduser('~')
    def get_set_up_directory(self):
        return os.path.dirname(os.path.realpath(__file__))
    def get_project_dot_files_directory(self):
        return os.path.join(self.get_set_up_directory(), 'global_dot_files')

class Booter(object):
    """docstring for Booter."""
    def __init__(self, **kwargs):
        super(Booter, self).__init__()
        self.directory_handler = kwargs.pop('directory_handler')
    def copy_global_dot_files(self, source, destination):
        print 'source: %s' % source
        print 'destination: %s' % destination
        onlyfiles = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
        for dot_file in onlyfiles:
            print dot_file
            dot_file_source = os.path.join(source, dot_file)
            print 'dot_file_source: %s' % dot_file_source
            dot_file_destination = os.path.join(destination, '.' + dot_file)
            print 'dot_file_destination: %s' % dot_file_destination
            shutil.copy(dot_file_source, dot_file_destination)
    def set_up(self):
        self.copy_global_dot_files(self.directory_handler.get_project_dot_files_directory(), self.directory_handler.get_home_directory())
        print 'Copied home dot files'




def main():
    print 'hello'
    directory_handler = DirectoryHandler()
    booter = Booter(directory_handler=directory_handler)
    booter.set_up()

if __name__ == "__main__":
    main()
