from pathlib import Path

from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Python MyAnimeList v2 API wrapper.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

setup(
    name='pyMALv2',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="Clarence",
    author_email="public@cm0.dev",
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    keywords=['python', 'myanimelist', 'api', 'wrapper', 'v2'],
    url='https://github.com/mclarence/pyMALv2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)