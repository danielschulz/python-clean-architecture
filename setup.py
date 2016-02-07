#!/usr/bin/env python3
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

NAME = 'dharma'
VERSION = (0, 0, 1)
INSTALL_REQUIRES = (
    'traitlets>=4.0.0',
)
TEST_REQUIRE = (
    'pytest>=2.8',
)


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


if __name__ == '__main__':
    setup(
        name=NAME,
        version='.'.join(str(i) for i in VERSION),
        cmdclass={'test': PyTest},
        install_requires=INSTALL_REQUIRES,
        tests_require=TEST_REQUIRE,
        packages=find_packages(exclude=['tests']),
    )