from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in professional/__init__.py
from professional import __version__ as version

setup(
	name="professional",
	version=version,
	description="custam app",
	author="NSFS",
	author_email="nextstepforsmartsolutions@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
