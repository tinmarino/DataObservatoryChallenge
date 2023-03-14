#!/usr/bin/env python3

"""
Test code for patent program
Run me from the same directory as patent.py
"""
from unittest import TestCase, main as test_main  # For formated test
from subprocess import Popen, PIPE  # For shell_execute
from os.path import dirname, abspath  # Get root dir

root_dir = dirname(dirname(abspath(__file__)))

class TestPatent(TestCase):
    """ Main Unitest class """

    def test_main(self):
        """ Test runner 1 """
        for patent, idd in [
                ['AAAA000', 1],
                ['AAAA001', 2],
                ['AAAA042', 43],
                ['AAAA999', 1000],
                ['AAAB001', 1002],
                ]:
            self.assert_patent_id(patent, idd)

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


if __name__ == '__main__':
    test_main()
