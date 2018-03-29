"""
wrap
-------------

This is the description for that library
"""
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='wrap',
    version='2018.03.01',
    url='https://github.com/pingf/wrap.git',
    license='MIT',
    author='Jesse MENG',
    author_email='pingf0@gmail.com',
    description='useful wrap collections',
    long_description=read('README.rst'),
    py_modules=['wrap'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['wrap'],
    zip_safe=False,
    include_package_data=True,
    # package_data={
        # 'wrap.xxx': ['*'],  # All files from folder A
    # },
    platforms='any',
    install_requires=[
        'logcc'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
