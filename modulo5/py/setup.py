from setuptools import setup, find_packages

setup(
    name='packages',
    version='0.0.1',
    packages=['packages'],
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ]
)
