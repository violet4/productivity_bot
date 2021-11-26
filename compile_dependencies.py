#!/usr/bin/env python3
import os
import subprocess


base_depends = {'alembic'}

def find_grep():
    brew_grep = '/usr/local/bin/ggrep'
    if os.path.exists(brew_grep):
        return brew_grep
    return 'grep'


def find_find():
    find_path = '/usr/bin/find'
    if os.path.exists(find_path):
        return find_path
    return 'find'


def compile_dependencies():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(this_dir, 'src')

    python_files = subprocess.check_output([
        find_find(), src_dir, '-name', '*.py', '-type', 'f'
    ]).decode().strip().split('\n')

    depends = base_depends.copy()
    for f in python_files:
        depends.update(subprocess.check_output([
            find_grep(), '-oP', '(?<=DEPENDS\()[^)]+', f
        ]).decode().strip().split('\n'))

    return depends


if __name__ == '__main__':
    for package in compile_dependencies():
        print(package)
