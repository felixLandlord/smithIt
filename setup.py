from setuptools import setup, find_packages

setup(
    name='smithIt',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'smith=core.creator:main',
        ],
    },
    install_requires=[
        'pyyaml',
    ],
)
