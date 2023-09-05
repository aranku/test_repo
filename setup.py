from setuptools import setup
import torch
print(torch.__file__)
print(torch.__version__)
from setuptools import setup, find_packages
raise Exception("wtf")

setup(
    name="funniest",
    version="0.1",
    packages=find_packages(),
)