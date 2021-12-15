import os


def get_parent_path(current_path):
    return os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")