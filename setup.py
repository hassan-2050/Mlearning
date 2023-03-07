from setuptools import find_packages,setup
from typing import List
hyphen='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        [requirement.replace ("/n","") for requirement in requirements ]

        if hyphen in requirements:
            requirements.remove(hyphen)




setup(

name="mlproject",
author="hassan imam",

packages=find_packages(),

install_requires=get_requirements('requirements.txt')

)
