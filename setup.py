from setuptools import setup, find_packages
from setuptools.command.install import install

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='jenkenv',
    author='jamesrobertalbert@gmail.com',
    version='0.0.3',
    long_description=readme(),
    url='https://github.com/jamesalbert/jenkenv',
    packages=['jenkenv'],
    package_data={'jenkenv': ['jenkinsfile-runner']},
    include_package_data=True,
    install_requires=[
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'jenkenv=jenkenv.__init__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)
