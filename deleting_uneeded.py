import os
from pathlib import Path
def get_size(f):
    for folder, subfolders, filenames in os.walk(f):
        for file in filenames:
            size = os.path.getsize(folder/Path(file))
            if size > 100*(10**6):
                print(file)
    print('Done!')
dir = Path.home()/'Downloads'
get_size(dir)
