import shutil
import os

def empty_directory(path):
    shutil.rmtree(path)
    create_dir(path)


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
