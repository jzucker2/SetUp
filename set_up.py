#!/usr/bin/env python

import os
import shutil
import subprocess

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
    def get_coding_directory(self):
        return os.path.join(self.get_home_directory(), 'Documents', 'Coding')
    def get_screenshots_directory(self):
        return os.path.join(self.get_home_directory(), 'Pictures', 'Screenshots')
    # def get_coding_symlink(self):
    #     return os.path.join(self.get_home_directory(), 'Coding')
    def set_up_path_and_home_and_desktop_symlink(self, directory_path):
        print 'directory_path: %s' % directory_path
        directory_name = os.path.basename(os.path.normpath(directory_path))
        print 'directory_name: %s' % directory_name
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        home_symlink_path = os.path.join(self.get_home_directory(), directory_name)
        print 'home_symlink_path: %s' % home_symlink_path
        if not os.path.exists(home_symlink_path):
            os.symlink(directory_path, home_symlink_path)
        desktop_symlink_path = os.path.join(self.get_home_directory(), 'Desktop', directory_name)
        print 'desktop_symlink_path: %s' % desktop_symlink_path
        if not os.path.exists(desktop_symlink_path):
            os.symlink(directory_path, desktop_symlink_path)

class FinderCommandExecutor(object):
    """docstring for FinderCommandExecutor."""
    def __init__(self):
        super(FinderCommandExecutor, self).__init__()
    def _execute_finder_command(self, command, shell=False):
        return subprocess.check_call(command, shell=shell)
    def redirect_screenshots(self):
        return self._execute_finder_command("defaults write com.apple.screencapture location ~/Pictures/Screenshots; killall SystemUIServer", shell=True)
    def add_recently_used_applications_stack_to_dock(self):
        return self._execute_finder_command("defaults write com.apple.dock persistent-others -array-add '{ \"tile-data\" = { \"list-type\" = 1; }; \"tile-type\" = \"recents-tile\"; }'; killall Dock", shell=True)

class Booter(object):
    """docstring for Booter."""
    def __init__(self, **kwargs):
        super(Booter, self).__init__()
        self.directory_handler = kwargs.pop('directory_handler')
        self.finder_command_executor = kwargs.pop('finder_command_executor')
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
    def set_up_coding_directory(self):
        self.directory_handler.set_up_path_and_home_and_desktop_symlink(self.directory_handler.get_coding_directory())
    def set_up_screenshots_directory(self):
        self.directory_handler.set_up_path_and_home_and_desktop_symlink(self.directory_handler.get_screenshots_directory())
    def set_up_custom_finder_commands(self):
        screen_shots_redirect_result = self.finder_command_executor.redirect_screenshots()
        print 'screen_shots_redirect_result: %s' % screen_shots_redirect_result
        recently_used_apps_stack = self.finder_command_executor.add_recently_used_applications_stack_to_dock()
        print 'recently_used_apps_stack: %s' % recently_used_apps_stack

    def set_up(self):
        self.copy_global_dot_files(self.directory_handler.get_project_dot_files_directory(), self.directory_handler.get_home_directory())
        print 'Copied home dot files'
        self.set_up_coding_directory()
        print 'Set up Coding directory and symlink'
        self.set_up_screenshots_directory()
        print 'Set up Screenshots directory and symlink'
        self.set_up_custom_finder_commands()
        print 'Set up custom finder commands'




def main():
    print 'hello'
    directory_handler = DirectoryHandler()
    finder_command_executor = FinderCommandExecutor()
    booter = Booter(directory_handler=directory_handler, finder_command_executor=finder_command_executor)
    booter.set_up()

if __name__ == "__main__":
    main()
