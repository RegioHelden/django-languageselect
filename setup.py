# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='django-languageselect',
    packages=find_packages(),
    version='0.1.3',
    description='Simple language select as custom template tag',
    author='RegioHelden GmbH',
    author_email='opensource@regiohelden.de',
    url='https://github.com/RegioHelden/django-languageselect',
    keywords=["django", "language"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    install_requires=[
        "Django>=1.3",
    ],
    include_package_data=True,
    long_description=open("README.md").read(),
    zip_safe=False
)
