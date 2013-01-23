from setuptools import setup, find_packages
import sys, os

version = '0.1dev'

setup(name='myapp',
      version=version,
      description="Biostuff and all that jazz",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='yoluk biostuff',
      author='Ozge Yoluk',
      author_email='ozge.yoluk@scilifelab.se',
      url='',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
