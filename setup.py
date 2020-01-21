import setuptools
from cmake_setuptools import *
setuptools.setup(
     name='timeswipe1',
     version='0.4',
     ext_modules=[CMakeExtension('run')],
     cmdclass={'build_ext': CMakeBuildExt},
     author="Ilya Gavrilov",
     author_email="gilyav@gmail.com",
     description="TimeSwipe python3 module",
     long_description="pydoc timeswipe",
     long_description_content_type="text/markdown",
     url="https://github.com/panda-official/TimeSwipe",
     install_requires = ['cmake_setuptools'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
