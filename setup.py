from setuptools import setup, find_packages
import unittest

def find_test_suite():
    loader = unittest.TestLoader()
    tests = loader.discover("test", pattern="*_test.py")
    return tests

with open("README.rst", "rb") as file:
    readme = file.read().decode("utf-8")

setup(
    name="matrix-logging",
    version="1.0.0",
    packages=find_packages(),
    description="Logging for Python",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Andy Lang",
    url="",
    download_url="",
    keywords=["logging", "python"],
    python_requires=">=3.5",
    test_suite="setup.find_test_suite"

)
