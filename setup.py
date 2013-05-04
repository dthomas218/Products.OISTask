from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='Products.OISTask',
      version=version,
      description="Allows tracking of customer tasks and associated expenses incurred.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='task tracking expenses plone archetypes',
      author='Tim Knapp',
      author_email='tim@emergetec.com',
      url='http://www.emergetec.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
