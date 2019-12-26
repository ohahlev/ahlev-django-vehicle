# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import vehicle

setup(
    name='ahlev-django-vehicle',
    version=vehicle.__version__,
    description='vehicle app using django framework',
    long_description='vehicle app using django framework',
    long_description_content_type='text/x-rst',
    author='ahlev',
    author_email='ohahlev@gmail.com',
    include_package_data=True,
    url='https://github.com/ohahlev/ahlev-django-vehicle/tree/%s' % vehicle.__version__,
    packages=find_packages(),
    install_requires=[
        'django-tinymce',
        'ahlev-django-css-js',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
