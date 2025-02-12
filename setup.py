from setuptools import find_packages, setup 

def get_requirements(file_path:str)->list:
    '''
    This function reads the requirements file and returns a list of requirements that will be installed in the environment.
    '''

    with open(file_path,'r') as fp:
        requirements = fp.read().splitlines()
    
    if '-e .' in requirements:
        requirements.remove('-e .')

    print(requirements)

    return requirements


setup(
    name = 'mlops_patients',
    version = '0.0.1',
    author = 'Sankalp',
    author_email = 'sankalpbisan07@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)