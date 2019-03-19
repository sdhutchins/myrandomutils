"""This is the test suite for file_management.py."""
import unittest
import os

from myrandomutils import DeleteDir


class TestFileManagement(unittest.TestCase):
    """Test File Management classes."""

    def setUp(self, rootpath=os.getcwd()):
        self.rootpath = rootpath

        os.makedirs('__pycache__', exist_ok=True)

    def test_file_management(self):
        """Test the DeleteCache class."""
        DeleteDir(self.rootpath).delete_cache()


if __name__ == '__main__':
    unittest.main()
