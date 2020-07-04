from setuptools import setup

setup(
    name='test-repo',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:feng-tao/test-package-pypi.git',
    author='Tao Feng',
    author_email='t@gmail.com',
    license='unlicense',
    packages=['test-repo'],
    zip_safe=False
)
