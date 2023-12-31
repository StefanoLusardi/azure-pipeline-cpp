#!/usr/bin/python
import argparse
import pathlib
import subprocess
import os
from command import run
import configparser

def check():
    run([ 'which', 'cmake' ])
    run(['cmake', '--version'])

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type",           choices=['Debug', 'Release'])
    parser.add_argument("profile",              help="Conan Profile")
    parser.add_argument("--build_dir",          required=False, default='./build')
    parser.add_argument("--integration_tests",  required=False, default=False, action='store_true')
    parser.add_argument("--unit_tests",         required=False, default=False, action='store_true')
    parser.add_argument("--coverage",           required=False, default=False, action='store_true')
    parser.add_argument("--benchmarks",         required=False, default=False, action='store_true')
    parser.add_argument("--examples",           required=False, default=False, action='store_true')
    parser.add_argument("--warnings",           required=False, default=False, action='store_true')
    parser.add_argument("--address_sanitizer",  required=False, default=False, action='store_true')
    parser.add_argument("--thread_sanitizer",   required=False, default=False, action='store_true')
    parser.add_argument("--clang_format",       required=False, default=False, action='store_true')
    parser.add_argument("--clang_tidy",         required=False, default=False, action='store_true')
    parser.add_argument("--cppcheck",           required=False, default=False, action='store_true')
    parser.add_argument("--cpplint",            required=False, default=False, action='store_true')
    parser.add_argument("--docs",               required=False, default=False, action='store_true')
    return parser.parse_args()

def main(args):
    current_working_directory = pathlib.Path(".conan").resolve()
    os.environ['CONAN_HOME'] = str(current_working_directory.absolute())
    print("Current Working Directory:", current_working_directory)
    conan_profile_path = pathlib.Path(current_working_directory.absolute(), "profiles", args.profile).resolve()

    profile = configparser.ConfigParser()
    profile.read(conan_profile_path)
    c_compiler = profile['buildenv']['CC']
    cxx_compiler = profile['buildenv']['CXX']

    subprocess.run(f"conan profile show --profile:build={args.profile} --profile:host={args.profile}", shell=True)

    run([
        'cmake',
        '-G', 'Ninja',
        '-D', f'CMAKE_C_COMPILER={c_compiler}',
        '-D', f'CMAKE_CXX_COMPILER={cxx_compiler}',
        '-D', f'CMAKE_BUILD_TYPE={str(args.build_type)}',
        '-B', f'{args.build_dir}/{args.build_type}',
        '-S', '.'
    ])

if __name__ == '__main__':
    check()
    main(parse())
