try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import mirasu

with open('README.rst') as f:
    readme = f.read()

setup(
    name='mirasu',
    version=mirasu.__version__,
    py_modules=['mirasu'],
    author='Ryan Gonzalez',
    author_email='rymg19@gmail.com',
    description='Automatically call super before or after methods.',
    long_description=readme,
    url='https://github.com/kirbyfan64/mirasu',
)
