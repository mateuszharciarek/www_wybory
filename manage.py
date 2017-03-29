#!/usr/bin/env python
import os
import sys
import xlrd
# ----------------------------------------------------------------------
def open_file(path):
    book = xlrd.open_workbook(path)
    first_sheet = book.sheet_by_index(0)
    cell = first_sheet.cell(0, 0)


# ----------------------------------------------------------------------



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    path = "dane/gm-okr01.xls"
    open_file(path)
    execute_from_command_line(sys.argv)