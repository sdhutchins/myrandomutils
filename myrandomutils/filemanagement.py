"""File Management Utilities"""

import shutil
import os
import tarfile
from tarfile import ReadError
from datetime import datetime

class DeleteDir(object):
    """Delete a certain directory from all sub directories.
    This function uses os.walk to walk a top level directory and delete pycache
    directories in each subdirectory.
    """
    def __init__(self, rootpath, directoryname):
        r = rootpath
        # Directories to exclude
        delete = [directoryname]
        for root, dirs, files in os.walk(r, topdown=True):
            for directory in dirs:
                if directory in delete:
                    dirpath = os.path.join(root, directory)
                    try:
                        shutil.rmtree(dirpath)
                        print("The following directory was deleted: %s" % dirpath)
                    except:
                        raise OSError


class DeleteCache(DeleteDir):
    """Delete pycache directories."""
    def __init__(self, rootpath=r'C:\Users\shutchins2',
                 directoryname='__pycache__'):
        super(DeleteCache, self).__init__(rootpath, directoryname)


class Extractor(object):
    """Extract tar.gz archives"""
    def __init__(self, filename):
        self.filename = filename
        self.extract_archive()

    def extract_archive(self):
        if os.path.isfile(self.filename) and str(self.filename).endswith('.tar.gz'):
            tar = tarfile.open(self.filename)
            tar.extractall()
            tar.close()

        elif not str(self.filename).endswith('.tar.gz'):
            raise ReadError('Not a tar archive')
        else:
            raise FileNotFoundError


class Archiver(object):
    """Archive folders"""
    def __init__(self, archive_name, archive_type, folder2archive):
        self.archive_types = ['zip', 'gztar']
        self._format = '%m-%d-%Y@%I:%M:%S-%p'
        self._date = str(datetime.now().strftime(self._format))
        self.archive_name = archive_name + '_archive' + self._date
        self.archive_type = archive_type
        self.archivefolder()

    def archivefolder(self):
        shutil.make_archive(self.archive_name, self.archive_type,
                            self.folder2archive)
