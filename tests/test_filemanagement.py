"""This is the test suite for file_management.py."""
import unittest
import os
from shutil import rmtree

from myrandomutils import DeleteCache


class TestFileManagement(unittest.TestCase):
    """Test File Management classes."""

    def setUp(self, rootpath=os.getcwd()):
        self.rootpath = rootpath

        os.makedirs('__pycache__', exist_ok=True)

    def test_file_management(self):
        """Test the DeleteCache class."""
        DeleteCache(self.rootpath)


if __name__ == '__main__':
    unittest.main()
