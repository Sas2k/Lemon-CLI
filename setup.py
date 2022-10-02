from setuptools import setup, find_packages

long_description = open('README.md', "r", encoding="utf-8").read()

setup(
    name="Lemon-CLI",
    version="1.0.1",
    packages=find_packages(),
    install_requires=["Lemon-Library"],
    author="Sasen Perera",
    author_email="sas8.communications@gmail.com",
    description="A Component generator for Lemon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sas2k/Lemon-CLI"
)