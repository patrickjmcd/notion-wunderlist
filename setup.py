# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='notion-wunderlist',
    version='0.1.0',
    install_requires=['notion>=0.0.21',
                      'python-dotenv>=0.10.1', 'wunderpy2>=0.1.6'],
    description='Syncs Notion tasks to Wunderlist',
    long_description=readme,
    author='Patrick McDonagh',
    author_email='patrickjmcd@gmail.com',
    url='https://github.com/patrickjmcd/notion-wunderlist',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': ['notion-wunderlist=notion_to_wunderlist:main'],
    }
)
