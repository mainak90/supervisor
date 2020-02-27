#!/usr/bin/env python
import os
import sys
import subprocess
from setuptools import setup

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['exec', 'logger', 'parser', 'watcher']

package_dir = {
    'exec': 'src/',
    'logger': 'src/',
    'parser': 'src/',
    'watcher': 'src/'
}

def prerequisite():
    try:
        subprocess.Popen("mkdir -p /etc/supervisor/log/ && cp conf/supervisor.json /etc/supervisor && chmod -R 777 /etc/supervisor/log/", shell=True)
    except Exception as e:
        print(e)

prerequisite()

setup(
    name='supervisor',
    version='1.0.0',
    description='very simple linux process supervisor',
    author='mdhar',
    author_email='mainak90@gmail.com',
    url='https://github.com/mainak90/supervisor',
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    license='Apache GPL',
    entry_points='''
        [console_scripts]
        supervisor=src.app:main
    '''
)