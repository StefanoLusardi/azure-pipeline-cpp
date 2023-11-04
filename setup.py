import os
import subprocess
import sys

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def build_extension(self, ext):
        subprocess.check_call(["cmake", "--version"])
        subprocess.check_call(["ninja", "--version"])

        self.build_type = os.environ.get("DEMO_PYBIND_BUILD_TYPE", "Release")
        self.cmake_configure(ext)
        self.cmake_build()

    def cmake_configure(self, ext):    
        output_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        if not output_dir.endswith(os.path.sep):
            output_dir += os.path.sep

        subprocess.check_call([
            'cmake',
            '-G', 'Ninja',
            '-D', f'CMAKE_BUILD_TYPE={self.build_type}',
            '-D', f'CMAKE_LIBRARY_OUTPUT_DIRECTORY={output_dir}',
            '-D', f'PYTHON_EXECUTABLE={sys.executable}',
            '-D', f'EXAMPLE_VERSION_INFO={self.distribution.get_version()}',
            '-B', f'{self.build_temp}/{self.build_type}',
            '-S', ext.sourcedir
        ])

    def cmake_build(self):
        subprocess.check_call([
            'cmake',
            '--build', f'{self.build_temp}/{self.build_type}',
            '--parallel', '16',
            '--config', self.build_type
        ])

setup(
    name="pydemo",
    version="0.0.1",
    author="Stefano Lusardi",
    author_email="lusardi.stefano@gmail.com",
    description="A demo project using pybind11 and CMake",
    ext_modules=[CMakeExtension("demo")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
)