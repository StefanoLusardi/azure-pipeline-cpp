#!/usr/bin/python
import platform
import subprocess
import argparse
import pathlib
import sys
import os

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("compiler", help="Compiler name", choices=['gcc', 'clang', 'apple-clang', 'msvc'])
    parser.add_argument("compiler_version", help="Compiler version")
    return parser.parse_args()

def run(command):
    try:
        ret = subprocess.run(command)
        ret.check_returncode()
    except Exception as e:
        print(f'Unhandled Exception: {e}')

def conan_profile_create(profile_name, args):
    run([ 'conan', 'profile', 'detect', f'--name={profile_name}', '--force'])
    # run([ 'conan', 'profile', 'update', f'env.CONAN_CMAKE_GENERATOR=Ninja', f'{profile_name}']) # for conan v1 recipes
    run([ 'conan', 'profile', 'update', f'conf.tools.cmake.cmaketoolchain:generator=Ninja', f'{profile_name}']) # for conan v2 recipes
    run([ 'conan', 'profile', 'update', f'conf.tools.system.package_manager:mode=install', f'{profile_name}'])
    run([ 'conan', 'profile', 'update', f'conf.tools.system.package_manager:sudo=True', f'{profile_name}'])

    if args.compiler != None:
        run([ 'conan', 'profile', 'update', f'settings.compiler={args.compiler}', f'{profile_name}' ])
    
    if args.compiler_version != None:
        run([ 'conan', 'profile', 'update', f'settings.compiler.version={args.compiler_version}', f'{profile_name}'])

    if args.compiler == 'msvc':
        if platform.system() != 'Windows':
            raise RuntimeError("msvc  is only supported on Windows")
        
        compiler = 'cl'
        run([ 'conan', 'profile', 'update', f'env.CC={compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'env.CXX={compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', 'settings.compiler.cppstd=20', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', 'settings.compiler.runtime=dynamic', f'{profile_name}'])

    if args.compiler == 'apple-clang':
        if platform.system() != 'Darwin':
            raise RuntimeError("apple-clang is only supported on MacOS")
        
        cc_compiler = 'clang'
        cxx_compiler = 'clang++'
        run([ 'conan', 'profile', 'update', f'env.CC={cc_compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'env.CXX={cxx_compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'settings.compiler.libcxx=libc++', f'{profile_name}'])

    if args.compiler == 'clang':
        cc_compiler = f'clang-{args.compiler_version}' if platform.system() == 'Linux' else 'clang'
        cxx_compiler = f'clang++-{args.compiler_version}' if platform.system() == 'Linux' else 'clang++'
        run([ 'conan', 'profile', 'update', f'settings.compiler.libcxx=libstdc++11', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'env.CC={cc_compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'env.CXX={cxx_compiler}', f'{profile_name}'])

    if args.compiler == 'gcc':
        cc_compiler = f'gcc-{args.compiler_version}' if platform.system() == 'Linux' else 'gcc'
        cxx_compiler = f'g++-{args.compiler_version}' if platform.system() == 'Linux' else 'g++'
        run([ 'conan', 'profile', 'update', f'env.CC={cc_compiler}', f'{profile_name}'])
        run([ 'conan', 'profile', 'update', f'env.CXX={cxx_compiler}', f'{profile_name}'])

def conan_profile_show(profile_name):
    run([ 'conan', 'profile', 'show', f'{profile_name}' ])

def setup_conan_home():
    current_working_directory = pathlib.Path().resolve()
    os.environ['CONAN_HOME'] = str(current_working_directory.absolute())
    print("Current CONAN_HOME Directory:", current_working_directory)

def main():
    setup_conan_home()
    args = parse()

    if args.compiler is not None and args.compiler_version is not None:
        profile_name = f'{args.compiler+args.compiler_version}'
    else:
        profile_name = "default"
    
    conan_profile_create(profile_name, args)
    conan_profile_show(profile_name)

if __name__ == '__main__':
    sys.exit(main())
