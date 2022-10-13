from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in epos_restaurant/__init__.py
from epos_restaurant import __version__ as version

setup(
	name="epos_restaurant",
	version=version,
	description="ePOS for Coffee and Restaurant",
	author="EST Computer",
	author_email="pheakdey.micronet@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
