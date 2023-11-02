#!/usr/bin/python
import argparse
from command import run

def check():
    run([ 'which', 'cmake' ])
    run(['cmake', '--version'])

def parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("build_type", choices=['Debug', 'Release'])
    parser.add_argument("--build_dir", help="Build Directory", required=False, default='./build')
    return parser.parse_args()

def build(args):
    run([
        'cmake',
        '--build', f'{args.build_dir}/{args.build_type}',
        '--parallel', '16'
    ])

if __name__ == '__main__':
    check()
    build(parse())