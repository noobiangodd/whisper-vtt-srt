import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="whisper_vtt-srt",
    packages=find_packages(),
    py_modules=["whisper_vtt-srt"],
    author="Maximiliano Lira Del Canto",
    install_requires=[
        'whisper @ git+https://github.com/openai/whisper.git@main#egg=whisper'
    ],
    description="Generate subtitles for videos using Whisper",
    entry_points={
        'console_scripts': ['whisperSubs=whisperSubs.cli:main'],
    },
    include_package_data=True,
)
