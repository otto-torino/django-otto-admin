import os
#from distutils.core import setup
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-otto-admin',
    version='0.1.1',
    packages=['otto_admin', 'otto_admin.templatetags'],
    include_package_data=True,
    license='MIT License',
    description='Django admin customization app for django-suit providing google analytics widgets in the admin index',
    long_description=README,
    url='http://github.com/otto-torino/django-otto-admin',
    author='abidibo',
    author_email='abidibo@gmail.com',
    install_requires=[
        'Django',
        'django-suit',
        'google-api-python-client',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ]
)
