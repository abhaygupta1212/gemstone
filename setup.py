from setuptools import find_packages, setup
HYPHEN_E_DOT = "-e ."

def get_requirements():
    requirements = []
    with open("requirements.txt") as file_object:
        requirements = [req.replace("\n", "") for req in file_object.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name = "GemstoneProject",
    version="0.0.1",
    author="Abhay Gupta", 
    author_email="abhaygupta.xyz@gmail.com",
    install_requires = get_requirements(),
    packages=find_packages()
)