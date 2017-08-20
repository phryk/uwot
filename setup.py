from setuptools import setup

setup(
    name = 'uwot',
    version = '0.0.0',
    py_modules = ['uwot'],
    install_requires = [
        'click',
        'peewee'
    ],
    entry_points='''
    [console_scripts]
    uwot=uwot:cli
    '''
)
