#!/usr/bin/env python                                                       
# -*- coding: utf-8 -*-

import os
from shutil import copy, copyfile

from file_scanner import scan_dir
from path_util import resolve_file


def copy_res(source, dest):
    if not os.path.exists(dest):
        print("create res dir ", dest)
        os.makedirs(dest)
    files = scan_dir(source, ['*'])                                    
    for f in files:
        new_file = resolve_file(dest, source, f)
        new_parent_dir = new_file[0:new_file.rindex('/')]
        if not os.path.exists(new_parent_dir):
            os.makedirs(new_parent_dir)
        copy_res_item(f, new_file)        



def copy_res_item(source, dest):
    if not os.path.exists(source):
        print("cp source %s not exist " % source)
        return
    try:
        copyfile(source, dest)
        #copy(source, dest)
        print("copy resource to %s " % dest)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        #exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        #exit(1)


if __name__ == '__main__':
    copy_res_item("/tmp/abc","/tmp/cde")
    copy_res("/tmp/er", "/tmp/er-copy")

