import os
import shutil

## Directory consts
src_dir = "C:\\Users\\<UserName>\\Downloads\\"
dest_dir_newfolder = "C:\\Users\\<UserName>\\Desktop\\newfolder"

# with os.scandir(src_dir) as items:
#   for item in items:
#     print(item.name)

with os.scandir(src_dir) as items:
    for item in items:
        name = item.name
        dest = src_dir
        if name.endswith('.png') or name.endswith('.jpg') or name.endswith('.jpeg'):
            shutil.move(src_dir + name, dest_dir_newfolder)