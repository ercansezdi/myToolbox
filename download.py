import os


def download_libs():
    libraries = ["keyboard", "pillow", "pymongo", " pymongo[srv]", "pyperclip"]
    for libs in libraries:
        os.system("pip install " + libs)
