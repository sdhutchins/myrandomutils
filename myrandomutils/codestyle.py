import os
import subprocess


class StyleFix(object):
    """Perform automatic pep8 for code in a top down fashion.

    pip install autope8 to use this.
    """
    def __init__(self, include, dirpath):
        # Directories to exclude
        include = [include]
        for root, dirs, files in os.walk(dirpath, topdown=True):
            dirs[:] = [d for d in dirs if d in include]
            for name in files:
                if name.endswith('.py'):
                    pep8cmd = "autopep8 --in-place --aggressive " + str(os.path.join(root, name))
                    os.system(pep8cmd)
                    print(pep8cmd)
                    callcmd = subprocess.check_output(pep8cmd, shell=True).decode()
                    if callcmd == 0:  # Command was successful.
                        print('Autopep8 was performed on %s' % name)
                    else:
                        print('Failed autopep8 on %s' % name)
