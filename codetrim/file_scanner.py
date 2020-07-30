#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def scan_dir(path,file_type = '*'):
    allfiles = []
    files = os.listdir(path)
    for f in files:
        fpath = path + "/" + f
        if os.path.isdir(fpath):
            if file_type == '*':
                allfiles.append(fpath)
                #print("get a dir ", fpath)
            allfiles.extend(scan_dir(path + "/" + f, file_type))
        else:
            #print("get a file ", fpath)
            if file_type == '*':
                allfiles.append(fpath)
            elif f.endswith(file_type):
                allfiles.append(fpath)
            #pass
    return allfiles


if __name__ == "__main__":
    # execute only if run as a script
    a = scan_dir("/tmp") 
    print("all file ", a)
    print("scala files ", scan_dir("/tmp",".log"))

