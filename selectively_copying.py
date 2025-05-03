import shutil
import os
from pathlib import Path

p = Path.home()/'Downloads'
dst = Path(p/'Keychain Business').mkdir(exist_ok=True)
for folder, subfolders, files in os.walk(p):
    print(folder)
    for file in files:
        if file.endswith('.png'):
            src = folder/Path(file)
            if not src.exists():
                shutil.move(src, dst)
print('Done!')