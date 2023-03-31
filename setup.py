# Author: Yuki Yamamoto <curious.yamamon@gmail.com>
# Copyright (c) 2023 Yuki Yamamoto
# License: MIT License

from setuptools import setup

import dnxmy

DESCRIPTION = "dnxmy: dummy data generator for machine learning and statistics"
NAME = 'dnxmy'
AUTHOR = 'Yuki Yamamoto'
AUTHOR_EMAIL = 'curious.yamamon@gmail.com'
URL = 'https://github.com/roseiricho/dnxmy'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/roseiricho/dnxmy'
VERSION = dnxmy.__version__
PYTHON_REQUIRES = ">=3.7"

INSTALL_REQUIRES = [
    'numpy >=1.20.3',
    'pandas>=1.2.4'
]


PACKAGES = [
    'dnxmy'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering'
]

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )