from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lead_integration/__init__.py
from lead_integration import __version__ as version

setup(
	name="lead_integration",
	version=version,
	description="Integrations to generate leads",
	author="IBSL-IT",
	author_email="design@indibasolutions.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
