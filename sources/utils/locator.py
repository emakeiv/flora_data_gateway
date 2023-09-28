import os

basedir = './'


def ensure_folder_exists(name):
    if not os.path.exists(os.path.join(basedir, name)):
        os.mkdir(os.path.join(basedir, name))
