import os.path

def abs_path_from_project_root(pic):
    path = os.path.abspath(f'{pic}')
    return path