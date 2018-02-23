# -*- coding: utf-8 -*-

"""Main module."""
import platform
import shutil

def get_platform():
    s = "The platform is " + platform.platform()
    total, used, free = shutil.disk_usage(__file__)
    s += '\n'
    s += "total: {}".format(total)
    s += '\n'
    s += "used: {}".format(used) 
    s += '\n'
    s += "free: {}".format(free)
    return s

if __name__ == '__main__':
    print(get_platform())