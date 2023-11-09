#!/usr/bin/python
import subprocess
import argparse
import pathlib
import os
import sys
import shutil

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type", help="Debug or Release", choices=['Debug', 'Release'])
    parser.add_argument("profile", help="Conan Profile")
    parser.add_argument("-d", "--directories", help="Specific conanfiles directories", nargs='*', required=False)
    return parser.parse_args()

def setup_conan_home():
    current_working_directory = pathlib.Path(".conan").resolve()
    os.environ['CONAN_HOME'] = str(current_working_directory.absolute())
    print("CONAN_HOME Directory:", current_working_directory)

def update_conan_profiles():
    src = pathlib.Path("scripts", "conan", "profiles").resolve()
    dst = pathlib.Path(os.getenv('CONAN_HOME'), "profiles").resolve()
    shutil.copytree(src, dst, dirs_exist_ok=True)

def check_conan_profile(profile):
    command = "conan profile list"
    try:
        ret = subprocess.run(command, shell=True, capture_output=True)
        ret.check_returncode()
        profiles = ret.stdout.decode().strip().splitlines()
        if profile in profiles:
            print("Conan Profile found:", profile)
        else:
            print("ERROR! Conan Profile not found:", profile)
            for profile in profiles:
                print(profile)
            sys.exit(1)

    except Exception as e:
        print(f'Unhandled Exception: {e}') 

def conan_install(conanfile_directory, profile, build_type):
    command = f"conan install {conanfile_directory} --output-folder=build/modules --settings build_type={build_type} --profile:build={profile} --profile:host={profile} --build missing"
    try:
        ret = subprocess.run(command, shell=True, capture_output=True)
        ret.check_returncode()
    except Exception as e:
        print(f'Unhandled Exception: {e}') 

def main():
    args = parse()
    setup_conan_home()
    update_conan_profiles()
    check_conan_profile(args.profile)

    conanfile_directories = []
    if not args.directories:
        current_working_directory = pathlib.Path().resolve()
        conanfile_directories_include = set(current_working_directory.glob('**/conanfile.txt'))
        conanfile_directories_exclude = set(current_working_directory.glob('**/.conan/**/conanfile.*'))
        conanfile_directories = conanfile_directories_include - conanfile_directories_exclude
    else:
        conanfile_directories = args.directories

    for conanfile_directory in conanfile_directories:
        print("Installing conanfile:", conanfile_directory)
        conan_install(conanfile_directory, args.profile, args.build_type)

if __name__ == '__main__':
    sys.exit(main())
