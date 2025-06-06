from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    JYPEN_E_DOT='-e.'
    with open(file_path) as file_obj:
        
        requirements=file_obj.readlines()
        [req.replace ('\n','') for req in requirements]
        

        if JYPEN_E_DOT in requirements:
            requirements.remove(JYPEN_E_DOT)
        
setup(
    name='mlproject',
    version='0.0.1',
    author='Krish',
    author_email='kaustubhthorat1288.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
)