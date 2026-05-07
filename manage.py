#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 👇 新增这两行，强制 Python 用 UTF-8 编码，避免 latin-1 问题
os.environ["PYTHONUTF8"] = "1"
sys.setrecursionlimit(1500)  # 可选，避免递归限制

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentjobs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
