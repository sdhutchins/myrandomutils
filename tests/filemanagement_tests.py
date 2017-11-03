"""This is the test suite for file_management.py."""
import unittest
import os

from myrandomutils import DeleteCache


class TestManager(unittest.TestCase):
    """Test the Manager module."""

    def setUp(self, rootpath):
        self.rootpath = os.path.join(os.getcwd(), '__pycache__')

        os.makedirs('__pycache__', exist_ok=True)

    def test_file_management(self):
        """Test the DeleteCache class."""
        DeleteCache(self.rootpath)


if __name__ == '__main__':
    unittest.main()
