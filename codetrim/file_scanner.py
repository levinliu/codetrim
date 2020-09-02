#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


def scan_dir(path,file_types = []):
    allfiles = []
    files = os.listdir(path)
    for f in files:
        fpath = path + "/" + f
        if os.path.isdir(fpath):
            if is_valid_type(fpath, file_types):
                allfiles.append(fpath)
                #print("get a dir ", fpath)
            allfiles.extend(scan_dir(path + "/" + f, file_types))
        else:
            #print("get a file ", fpath)
            if is_valid_type(fpath, file_types):
                allfiles.append(fpath)
            #pass
    return allfiles


def is_valid_type(fpath, types=[]):
    if types == [] or '*' in types:
        return True
    for t in types:
        if fpath.endswith(t):
            return True
    return False 


if __name__ == "__main__":
    # execute only if run as a script
    a = scan_dir("/tmp") 
    print("all file ", a)
    print("scala files ", scan_dir("/tmp",[".log",".java"]))

