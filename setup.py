from setuptools import setup

setup(name='scripts',
      version='0.1',
      description='',
      url='',
      author='Pier-Luc Charbonneau',
      author_email='Pier-Luc Charbonneau',
      license='Apache License, Version 2.0',
      packages=['jenkins_demo'],
      install_requires=[
          'json',
          'argparse',
          'sys',
          'pprint',
          'time',
      ],
      zip_safe=False)