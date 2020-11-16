import os
class download:
    def __init__(self,libs):
        for i in libs:
            tostr = str(os.system("pip show " + i))
            tostr = tostr.split(":")
            if tostr[0] == "1":
                os.system("pip install " + i)
            else:
                pass
