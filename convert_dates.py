import os
import shutil
from pathlib import Path
import re

p = Path.home()/'Downloads'/'Spam Folder'/'Dates'

def convert_date(po, mm, dd, yyyy, f):
    new_date = re.sub(po, fr'{dd}-{mm}-{yyyy}', f)
    return new_date

def rename_file(f, new_f):
    shutil.move(p/f, p/new_f)

for folder, subfolders, filenames in os.walk(p):
    print(folder)
    for file in filenames:
        p_match = r'(\d{2})-(\d{2})-(\d{4})'
        match = re.match(p_match, file)
        mm = match.group(1)
        dd = match.group(2)
        yyyy = match.group(3)
        new_file = convert_date(p_match, mm, dd, yyyy, file)
        rename_file(file, new_file)