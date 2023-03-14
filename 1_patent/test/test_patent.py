#!/usr/bin/env python3

"""
Test code for patent program
Run me from the same directory as patent.py

IDEA:
    * import directly module
    * with self.assertRaises(Exception) as context:
"""
from unittest import TestCase, main as test_main  # For formated test
from subprocess import Popen, PIPE  # For shell_execute
from os.path import dirname, abspath  # Get root dir
import sys  # Hide stderr
import os  # Hide stderr

root_dir = dirname(dirname(abspath(__file__)))

class TestPatent(TestCase):
    """ Main Unitest class """

    def test_good(self):
        """ Test runner 1 """
        for patent, idd in [
                ['AAAA000', 1],  # Start
                ['AAAA001', 2],
                ['AAAA042', 43],
                ['AAAA999', 1000],
                ['AAAB001', 1002],
                ['ABCD012', 731013],
                ['DCBA210', 54106211],  # Decreasing digits
                ['ZZZZ999', 456976000],  # End
                ['zzzz999', 456976000],
                ]:
            self.assert_patent_id(patent, idd)

    # Commented out to avoid ugly output at revision
    #def test_bad(self):
    #    """ Should fail """
    #    for patent in [
    #            ['tooooooooooolooong'],
    #            ['$&%$&'],
    #            ]:
    #        self.assert_patent_raise(patent)

    def assert_patent_raise(self, patent):
        """ Assert it will fail """
        with open(os.devnull, 'w', encoding='utf8') as devnull:
            with RedirectStdStreams(stdout=devnull, stderr=devnull):
                ret = shell_execute(f'{root_dir}/patent.py {patent}')
                self.assertNotEqual(0, ret[0])

    def assert_patent_id(self, patent, idd):
        """ From subshell """
        ret = shell_execute(f'{root_dir}/patent.py {patent}')
        self.assertEqual(str(idd), ret[1])


def shell_execute(cmd):
    """ Helper: Execute shell command
    Return: (exit status, stdout, stderr)
    """
    with  Popen(cmd, stdout=PIPE, shell=True, universal_newlines=True) as pipe:
        output, error = pipe.communicate()
    output = output.rstrip() if output is not None else ''
    error = error.rstrip() if error is not None else ''
    status = pipe.returncode
    return status, output, error


class RedirectStdStreams():
    """ From: https://stackoverflow.com/questions/6796492/temporarily-redirect-stdout-stderr """
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr
        self.old_stdout = None
        self.old_stderr = None

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush()
        self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush()
        self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


if __name__ == '__main__':
    test_main()
