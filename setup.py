from setuptools import setup, find_packages

setup(
    name='portProbe',
    version='1.0.2',
    description='portProbe is a tool designed to efficiently probe for open ports. It will take both IP Address and Subdomains.',
    author='AashishSec',
    url='https://github.com/aashishsec/httpAlive',
    packages=find_packages(),
    install_requires=[
        'sockets',
        'ipaddress',
        'colorama',
        'requests'
    ],
    extras_require={
        'dev': ['argparse', 'concurrent.futures','random'],
    },
    entry_points={
        'console_scripts': [
            'portProbe = portProbe.portProbe:main',
        ],
    },
)
