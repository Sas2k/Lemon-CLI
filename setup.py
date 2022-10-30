from setuptools import setup, find_packages

long_description = open('README.md', "r", encoding="utf-8").read()

requirements = list()
with open("requirements.txt") as fhand:
    requirements = [l.rpartition('==')[0] for l in fhand]

setup(
    name="Lemon-CLI",
    version="1.3.1",
    packages=find_packages(),
    install_requires=requirements,
    author="Sasen Perera",
    author_email="sas8.communications@gmail.com",
    description="A Component generator for Lemon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sas2k/Lemon-CLI"
)
