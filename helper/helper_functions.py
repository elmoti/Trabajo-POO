import os
import sys


def resource_path(relative_path):
    base_path = os.path.abspath(".")
    if getattr(sys, "frozen", False):
        # The application is frozen
        base_path = os.path.dirname(sys.executable)
    return os.path.join(base_path, relative_path)


def lib_file(imagen):
    result = "lib/"+imagen
    try:
        img = open(imagen)
        return result
    except:
        return imagen
