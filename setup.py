#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess
from setuptools import setup, find_packages, Command

def read_readme(fname):
   try:
      import pypandoc
      return pypandoc.convert('README.md','rst')
   except (IOError, ImportError):
      return ''

def get_version():
   #git_version=subprocess.check_output(["git", "describe", "--always"])
   #if '.' not in git_version:
   #   return "0.0.dev"+git_version
   return subprocess.check_output(["git", "describe", "--tags"]).rstrip()

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    version_git = subprocess.check_output(["git", "describe", "--tags"]).rstrip()
except:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__=" + version_git)

setup(
    name = "python-cson",
    version = "{ver}".format(ver=version_git),
    url = 'https://github.com/lifthrasiir/cson',
    download_url = 'https://github.com/gt3389b/python-cson/',
    license = 'MIT',
    description = "Python library for CSON (schema-compressed JSON)",
    author = 'Russell Leake',
    author_email = 'gt3389b@gmail.com',
    py_modules = ["cson"],
    entry_points = {
       'console_scripts' : [
          'python-cson = cson:main'
         ]
       },
    long_description = read_readme('README.md'),
    include_package_data = True,
    cmdclass = { 'test': PyTest },
    zip_safe = False,
    keywords = 'json cson cursive'
)
