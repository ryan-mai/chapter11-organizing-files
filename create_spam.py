import os
from pathlib import Path
import shutil
import random
import re
p = Path.home()/'Downloads'/'Spam Folder'
Path(p/'Dates').mkdir(exist_ok=True)
p = Path.home()/'Downloads'/'Spam Folder'/'Dates'
def create_spam(dst):
    path = p/dst
    txt = re.search(r'\d{2}-\d{2}-\d{4}', dst).group()
    print(txt)
    if not path.exists():
        with open(path, 'w') as f:
            f.write(txt)

def create_dates(m, d):
    name = f'{str(m).zfill(2)}-{str(d).zfill(2)}-2025 Daily Report.txt'
    create_spam(name)

for i in range(1,4):
    if i == 2:
        for j in range(1, 29):
            create_dates(i,j)
    elif i%2 == 0: 
        for j in range(1, 32):
            create_dates(i,j)
    else:
        for j in range(1, 31):
            create_dates(i, j)
