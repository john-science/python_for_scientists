# WARNING! THE ORDER OF THE IMPORTS BELOW IS IMPORTANT! DO NOT CHANGE!
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
# WARNING! THE ORDER OF THE IMPORTS ABOVE IS IMPORTANT! DO NOT CHANGE!
from glob import glob


#setup(cmdclass={'build_ext': build_ext},
#      ext_modules=cythonize('finding_primes.pxd'))

#setup(cmdclass={'build_ext': build_ext},
#      ext_modules=cythonize(Extension('*', ['finding_primes.pxd'])))


EXT_MODULES = [Extension(p[:-4], [p, p[:-2] + 'y'], extra_compile_args=["-w"])
               for p in glob('*.pxd')]



# do the actual setup / install
setup(cmdclass={'install': install,
                'build_ext': build_ext},
      name='finding_primes',
      packages=find_packages(),
      ext_modules=cythonize(EXT_MODULES, force=True))
