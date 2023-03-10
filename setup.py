from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements
    """
    hyef_e = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyef_e in requirements:
            requirements = requirements.remove(hyef_e)
    
    return requirements

setup(
    name = "Used Car price prediction",
    version = '0.0.1',
    author = 'prathapj',
    author_email= 'praathapj@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)