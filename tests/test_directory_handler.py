import unittest
import set_up
import os

class DirectoryHandlerTestCase(unittest.TestCase):
    """docstring for DirectoryHandlerTestCase."""
    def setUp(self):
        self.directoryHandler = set_up.DirectoryHandler()
    def test_gets_home_directory(self):
        actual_home_directory = self.directoryHandler.get_home_directory()
        self.assertIsNotNone(actual_home_directory)
        # TODO: Use regex matching to assert

if __name__ == '__main__':
    unittest.main()
