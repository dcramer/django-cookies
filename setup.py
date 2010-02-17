import os
from setuptools import setup, find_packages

setup(name='django-cookies',
    version=".".join(map(str, __import__("djcookies").__version__)),
    description='Drop-in replacement for Django\'s request.COOKIES',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-cookies',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
