import os
import shutil


def clear_screenshots_folder(path='utils/screenshots'):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
