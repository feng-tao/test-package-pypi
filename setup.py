from setuptools import setup

setup(
    name='tao-test-repo',
    version='0.0.2',
    description='My private package from private github repo',
    #url='git@github.com:feng-tao/test-package-pypi.git',
    author='Tao Feng',
    author_email='t@gmail.com',
    install_requires=[
        'lark-parser==0.8.5',
    ],
    license='unlicense',
    packages=['tao-test-repo'],
    zip_safe=False
)
