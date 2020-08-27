# --------------------------------------------------------------------------------
# Author: Claude Gibert
#
# --------------------------------------------------------------------------------
import os


def clean_save(filename, data):
    """
        Creates a temporary file and saves the data into it,
        then renames the temporary file to filename. This is
        clean in a system where directories are being watched
        and files are processed when found.
    """
    f = open('%s.tmp' % filename, 'w')
    f.write(data)
    f.close()
    os.rename('%s.tmp' % filename, filename)


def directory_list(path, extension=None):
    """
        Returns list of file names in a directory. If extension is specified,
        only files with that extensions are returned.

        :param path: absolute or relative path to the directory
        :param extension: file name extension (without the '.')
        :return: a list of file names (without the path).
    """
    result = []
    if os.path.exists(path):
        files = os.listdir(path)
        if extension is None:
            result = files
        else:
            for file in files:
                file_list = file.split('.')
                if file_list[-1] == extension:
                    result.append(file)
    return result


def mkdir(directory):
    """
        Creates a directory without failing if the directory exists.
        :param directory: path to directory
        :return:
    """
    try:
        os.makedirs(directory)
    except OSError:
        pass


class FileWatcher(object):
    """
    Watches a file and when being polled, returns True if the file was
    modified since the object was created.
    """
    def __init__(self, file):
        self.file = file
        self.latest = os.stat(file).st_mtime

    def __call__(self):
        current = os.stat(self.file).st_mtime
        if current != self.latest:
            self.latest = current
            return True
        return False


class FileBrowser(object):
    def __init__(self, path, extension=None):
        self._path = path
        self._extension = extension

    def __call__(self, visitor):
        files = directory_list(self._path, self._extension)
        for filename in files:
            full_path = '%s/%s' % (self._path, filename)
            visitor(self, full_path, filename)

    @staticmethod
    def delete_file(full_path):
        os.unlink(full_path)

    @staticmethod
    def move_file(full_path, destination):
        os.rename(full_path, destination)


def free_space_fs(pathname):
    """
        Get the free space of the filesystem containing pathname
    """
    stat = os.statvfs(pathname)
    # use f_bfree for superuser, or f_bavail if filesystem
    # has reserved space for superuser
    return stat.f_bfree*stat.f_bsize
