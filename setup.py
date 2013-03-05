from setuptools import setup, find_packages
setup(
    name='yoluk',
    author='Ozge Yoluk',
    author_email='ozge.yoluk@scilifelab.se',
    packages=['yoluk',],
    scripts=['scripts/getting_data.py'],
    long_description=open('README.txt').read(),
    version=1.0,
    install_requires=['untangle']
)

