import sys
import os


replacement = {
    'из':        'from',
    'спиздить': 'import',
    'высрать': 'print',
    'че_бля': 'input',
    'в': 'in',
    'попиздим': 'while',
    'пиздюк': 'for',
    'че_по_цифрам': 'int',
    'ты_че_русский': 'str',
    'списочек': 'list',
    'так_бля': 'def',
    'сука': '=',
    'приеби': '+',
    'отъеби': '-',
    'часики': 'time',
    'отдых': 'sleep',
    'записываю': 'append',
    'лови': 'return'
    }

files = sys.argv[1: ]

for file in files:
    with open(file + '.ypy', 'r') as f:
        code = f.read()
        for key, val in sorted(replacement.items(), reverse=True):
            code = code.replace(f"{key} ", f"{val} ")
            code = code.replace(f" {key}", f" {val}")
            code = code.replace(f"{key}(", f"{val}(")
            code = code.replace(f" {key}:", f" {val}:")
            code = code.replace(f" {key}(", f" {val}(")
            code = code.replace(f"\n{key}:", f"\n{val}:")

    with open(file + '.py', 'w') as f:
        f.write(code)

