#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os
import re

from setuptools import setup, find_packages


def get_version(*file_paths):
    """Retrieves the version from django_scrubber/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Django>=2.2.19',
]

setup_requirements = []

test_requirements = []

setup(
    name='django_languageselect',
    version=get_version('django_languageselect', '__init__.py'),
    description='Simple language select as custom template tag',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author='RegioHelden GmbH',
    author_email='entwicklung@regiohelden.de',
    url='https://github.com/RegioHelden/django-languageselect',
    packages=find_packages(include=['django_languageselect']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='django_languageselect',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
