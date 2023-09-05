from setuptools import setup
import torch
print(torch.__file__)
print(torch.__version__)
from setuptools import setup, find_packages
raise Exception("wtf")

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      zip_safe=False)