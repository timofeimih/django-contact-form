# -*- coding: utf-8 -*-
import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-contact-form',
    version='0.1',
    packages=['contact-form'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Simple mail sender from ajax',
    long_description="",
    url='http://www.codesgroup.eu/',
    author='Timofei Mihhailov',
    author_email='timofeimih@gmail.com.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
