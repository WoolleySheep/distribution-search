import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="list-search-functions",
    version="1.0.0",
    description="Pure-Python implementations of common list-search algorithms",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/WoolleySheep/list-search-functions",
    author="Matthew Woolley",
    author_email="matt.wool@live.com.au",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["list-search-functions"],
    include_package_data=True,
)