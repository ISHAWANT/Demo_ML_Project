from setuptools import setup,find_packages
from typing import List

# declearing variable for setup function
PROJECT_NAME='housing-predictor'
VERSION='0.0.3'
AUTHOR='ishawant'
DESCRIPTION='This is a first FSDS Nov batch Machine Learning Project'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'


def get_requirements_list()->List[str]: 
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        """
        Desription: This function is going to return list of requirement mention in requirements.txt file
        
        return This function is going to return a list which contain name of libraries mentioned in requirements.txt file 
        """
        requirement_file.readlines().remove('-e .')
    

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),  #packages= ['housing']
    install_requires=get_requirements_list()  
)
# python setup.py install

 