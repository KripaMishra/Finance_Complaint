from setuptools import setup, find_packages
from typing import List

PROJECT_NAME= 'Finance-Complaint'
VERSION= '0.0.1'
AUTHOR= "Kripa Mishra"
DESCRIPTION= "This is a sample of industry ready solution"

REQUIREMENT_FILE_NAME= "requirements.txt"

HYPHEN_E_DOT="-e ."

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_files:
        requirement_list= requirement_files.readlines()
        requirement_list= [requirements.replace("\n","") for requirements in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    

setup(
    name= PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires= get_requirements_list()
)