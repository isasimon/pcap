from setuptools import setup, find_packages

setup(
    name='mypkg',
    version='0.0.2',
    packages=find_packages(
        where='.',
        exclude=['mypkg.tests'],  # empty by default
    ),
    install_requires=[
        'requests'
    ],
)