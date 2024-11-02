from setuptools import setup, find_packages

# Define package metadata
NAME = "pypi-hello-world"
VERSION = "0.0.1"
AUTHOR = "Raghav Sethi"
AUTHOR_EMAIL = "work.raghavsethi@gmail.com"
DESCRIPTION = "A Hello World project to test PyPi"
URL = "https://github.com/05rs/pypi-hello-world"
LICENSE = "Apache"

# Define dependencies (if any)
INSTALL_REQUIRES = [
    "Flask"
]



# Find package structure
PACKAGES = ["hello_world"]

# Create setup arguments
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
)

# python3 setup.py sdist bdist_wheel
