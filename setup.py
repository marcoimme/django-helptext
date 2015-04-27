#!/usr/bin/env python
from setuptools import setup, find_packages

dirname = 'helptext'

app = __import__(dirname)

setup(
    name=app.NAME,
    version=app.get_version(),
    url='https://github.com/marcoimme/django-helptext',
    description="This is a Django application to insert help text into html page.",
    author='marcoimme',
    author_email='marcoimme@gmail.com',
    license='BSD',
    packages=find_packages('.'),
    include_package_data=True,
    platforms=['linux'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers'
    ]
)
