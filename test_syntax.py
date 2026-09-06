#!/usr/bin/env python
import glob
import os
import py_compile
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PY_FILES = [
    os.path.join(PROJECT_ROOT, path)
    for path in glob.glob('**/*.py', recursive=True)
    if 'venv' not in path.replace('\\', '/')
]

errors = []
for path in PY_FILES:
    try:
        py_compile.compile(path, doraise=True)
    except py_compile.PyCompileError as exc:
        errors.append((path, str(exc)))

if errors:
    print('Syntax errors found:')
    for path, message in errors:
        print(path)
        print(message)
    sys.exit(1)

print('All Python files compile successfully.')
