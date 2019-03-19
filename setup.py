from setuptools import setup, find_packages

setup(
    name='preciouspackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Preciousnkuna/preciouspackage.git',
    author='Precious Nkuna',
    author_email='preciousp.nkuna@gmail.com'
)
