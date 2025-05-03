import os
from pathlib import Path
import re
dst = Path.home()/'Downloads'/'Spam Folder'
invalid_num = []
for folder, subfolders, filenames in os.walk(dst):
    for file in filenames:
        match = re.search(r'\d+', file).group()
        invalid_num.append(int(match))

for i in range(1,41):
    if i not in invalid_num:
        src = f'spam{str(i).zfill(3)}.txt'
        with open(dst/src, 'w') as f:
            f.write('spam')