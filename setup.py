from setuptools import setup, find_packages

setup(
    name='PermutationFeatureSelector',
    version='0.1.0',
    description='A package for calculating permutation importance and selecting features.',
    author='Itsuki Ito',
    author_email='itoitsuki.28@gmail.com',
    url='https://github.com/Itsuki-2822/PermutationFeatureSelector', 
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'lightgbm'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)