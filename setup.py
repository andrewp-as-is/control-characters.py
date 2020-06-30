import setuptools

setuptools.setup(
    name='control-characters',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
