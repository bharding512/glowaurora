#!/usr/bin/env python3
from setuptools import setup as Setup
from numpy.distutils.core import setup,Extension
from os.path import join
from glob import glob

fortranfiles=['machprec.f90','egrid.f90','maxt.f90','glow.f',
              'vquart.f90','gchem.f','ephoto.f','solzen.f90','rcolum.f90',
              'etrans.f','exsect.f','ssflux.f','snoem.f90','snoemint.f',
              'geomag.f','nrlmsise00.f','qback.f','fieldm.f','iri90.f',
              'aurora_sub.f']

root='fortrancode'

fortranpaths = [join(root,f) for f in fortranfiles]
fortdata = glob(join(root,'*.dat'))

#%%
with open('README.rst') as f:
	long_description = f.read()

ext=[Extension(name='aurora',
               sources=fortranpaths,
               f2py_options=['quiet'],
)]
               #include_dirs=[root],
               #library_dirs=[root])]

#%% install
Setup(	  install_requires=['gridaurora','msise00','pymap3d',
                         'numpy','pandas','astropy'],
       dependency_links = ['https://github.com/scienceopen/msise00/tarball/master#egg=msise00',
                          'https://github.com/scienceopen/gridaurora/tarball/master#egg=gridaurora',
                          'https://github.com/scienceopen/pymap3d/tarball/master#egg=pymap3d'
                            ],)
setup(name='glowaurora',
      version='0.1',
	  description='Python wrapper for Stan Solomon GLOW auroral model',
	  long_description=long_description,
	  author='Michael Hirsch',
	  author_email='hirsch617@gmail.com',
	  url='https://github.com/scienceopen/glowaurora',
      packages=['glowaurora'],
      package_data={'': fortdata},
      include_package_data=True,
      ext_modules=ext,
      data_files=[('',fortdata) ]
      )