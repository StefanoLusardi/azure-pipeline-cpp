#!/usr/bin/python
import subprocess
import argparse
import pathlib
import os
import sys

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type", help="Debug or Release", choices=['Debug', 'Release'])
    parser.add_argument("profile", help="Conan Profile")
    parser.add_argument("-d", "--directories", help="Specific conanfiles directories", nargs='*', required=False)
    return parser.parse_args()

def conan_install(conanfile_directory, profile, build_type):
    command = [
        'conan', 'install', f'{conanfile_directory}',
        '--install-folder', f'build/modules', 
        '--settings', f'build_type={build_type}',
        '--profile:build', f'{profile}',
        '--profile:host', f'{profile}',
        '--build', 'missing'
    ]

    try:
        ret = subprocess.run(command)
        ret.check_returncode()
    except Exception as e:
        print(f'Unhandled Exception: {e}') 

def setup_conan_home():
    current_working_directory = pathlib.Path().resolve()
    os.environ['CONAN_USER_HOME'] = str(current_working_directory.absolute())
    print("Current Working Directory:", current_working_directory)

def main():
    setup_conan_home()
    args = parse()

    current_working_directory = pathlib.Path().resolve()

    conanfile_directories = []
    if not args.directories:
        conanfile_directories_include = set(current_working_directory.glob('**/conanfile.txt'))
        conanfile_directories_exclude = set(current_working_directory.glob('**/.conan/**/conanfile.*'))
        conanfile_directories = conanfile_directories_include - conanfile_directories_exclude
    else:
        conanfile_directories = args.directories

    for conanfile_directory in conanfile_directories:
        print("Processing directory:", conanfile_directory)
        conan_install(conanfile_directory, args.profile, args.build_type)

if __name__ == '__main__':
    sys.exit(main())
