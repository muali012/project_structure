"""
The setup.py file is an essential part of packaging 
and distributing Python projects.
It is used by setuptools (or distutils in older Python versions)
to define the configuration of your project, such as its metadata, 
dependencies, and more.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements
    from the requirements.txt file.
    """
    requirements_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_list

setup(
    name="SampleProject",
    version="0.0.1",
    author="Umair Ali",
    author_email="umair.tech@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
