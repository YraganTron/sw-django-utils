# coding: utf-8
# python setup.py sdist register upload
from setuptools import setup, find_packages

setup(
    name='sw-django-utils',
    version='0.0.24',
    description='Soft Way company django utils.',
    author='Telminov Sergey',
    author_email='sergey@telminov.ru',
    url='https://github.com/telminov/sw-django-utils',
    include_package_data=True,
    packages=find_packages(),
    license='The MIT License',
    requires=[
        'django',
        'sqlparse',
    ],
)
