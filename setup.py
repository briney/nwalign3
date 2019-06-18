import glob
import os

from setuptools import setup, find_packages
from distutils.extension import Extension

import numpy
np_include = numpy.get_include()
include_dirs = [np_include, "nwalign", "nwalign3"]

version = '0.1.2'

try:
    import nwalign3
    doc = nwalign3.__doc__
except:
    doc = ""

matrix_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nwalign3/matrices')
matrix_names = ['matrices/{}'.format(os.path.basename(f)) for f in sorted(glob.glob(os.path.join(matrix_dir, '*')))]

setup(name='nwalign3',
      version=version,
      description="Needleman-Wunsch global sequence alignment",
      long_description=doc,
      ext_modules=[Extension("nwalign3/cnwalign",
                      sources=["nwalign3/cnwalign.c"],
                      include_dirs=include_dirs)],
      keywords='sequence bioinformatics alignment needleman-wunsch',
      url='https://github.com/briney/nwalign3',
      # download_url='http://bitbucket.org/brentp/biostuff/get/tip.tar.gz',
      author='Bryan Briney',
      author_email='briney@scripps.edu',
      license='BSD',
      test_suite='nose.collector',
      include_package_data=True,
      zip_safe=False,
      packages=['nwalign3'],
      # package_dir={'': 'nwalign'},
      package_data={'nwalign3': ['*.pyx', "*.c"]},
      install_requires=['numpy', 'cython'],
      entry_points={'console_scripts': ['nwalign3 = nwalign3:main']},
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing'],)
