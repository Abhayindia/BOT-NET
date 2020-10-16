#!/usr/bin/env python3

import os

from setuptools import setup


def find_packages(path, base="", exclude=()):
    """ Find all packages in path """
    packages = []
    for item in os.listdir(path):
        if item[0] == '.':
            continue
        if path in exclude:
            continue
        directory = os.path.join(path, item)
        if os.path.isdir(directory):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            if module_name in exclude:
                continue
            packages.append(module_name)
            packages.extend(find_packages(directory, module_name, exclude))
    return packages


with open("./src/bot_net/README.md", "r") as fh:
    long_description = fh.read()


with open("./src/bot_net/requirements.txt", "r") as fh:
    install_requires = fh.readlines()


setup(
    name="bot_net",
    version='1.0',
    author="Abhay Chaudhary",
    description="Penetration testing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        'src',
        exclude=(
            'bot_net.docker',
            'bot_net.docs',
            'bot_net.lessons',
            'bot_net.resources.logos',
            'bot_net.resources.social'
        )
    ),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    package_data={
        '': [
            '*.html',
            '*.css',
            '*.js',
            '*.eot', '*.svg', '*.ttf', '*.woff', '*.woff2',
            '*.png', '*.jpg', '*.ico',
            'LICENSE',
            'requirements.txt',
            'bot_net-ascii.txt'
            # 'web.wsgi'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Topic :: Education :: Testing",
        'Topic :: Software Development :: Build Tools',
        "Topic :: System :: Clustering",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Hardware :: Symmetric Multi-processing",
        "Topic :: Utilities"
    ],
    entry_points={
        'console_scripts': [
            'bot_net = bot_net:main',
        ]
    },
    python_requires='>=3.6',
    keywords='bot_net penetration testing offensive cyber security pentest sniffing',
    project_urls={
        'Tracker': 'https://github.com/Abhayindia/BOT-NET',
        'Source': 'https://github.com/Abhayindia/BOT-NET',
        'Documentation': 'https://github.com/Abhayindia/BOT-NET'
    },
    install_requires=install_requires
)
