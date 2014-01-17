#!/usr/bin/python

import argparse

from os.path import join, dirname, abspath

class TestParser(object):
    def __init__(self):
        """Initialize the high level parser.
        """
        self._parser = argparse.ArgumentParser()
        self.configure()

    def configure(self) :
        """Define the commands. 
        """
        self._parser.add_argument('-r', '--roles', type=int, default=10, help='Number of Roles')
        self._parser.add_argument('-R', '--resources', type=int, default=10, help='Number of Resources')
        self._parser.add_argument('-o', '--old-config', default=False, dest='old_config', action='store_true', help='Use old/existing configuration or not!')

    def parse(self):
        """Parse the command line arguments.
        """
        args = self._parser.parse_args()
        return args

    def help(self):
        """Print parser help message.
        """
        self._parser.print_help()
        return None


if __name__ == '__main__':
    p = TestParser()
    p.help()


# __END__
