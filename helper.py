import os
import pathlib


def get_files(root):
    res = {}
    for path, subdirs, files in os.walk(root):
        for name in files:
            path_as_list = str(pathlib.Path(path, name)).split('\\')
            if path_as_list[-1].lower().endswith('.mp4'):
                if not res.get(path_as_list[2]):
                    res[path_as_list[2]] = []
                res[path_as_list[2]].append(pathlib.Path('/'.join(path_as_list[2:])))
    return res
