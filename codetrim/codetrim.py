#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CodeTrim to filter specific lang and trim code
"""

import os

from group_renamer import regroup
from comment import is_comment
from file_scanner import scan_dir


def load(path):
    with open(path, "r") as afile:
        lines = afile.readlines()
        return lines
    return None 


def filter_code(path):
    codelines = []
    lines = load(path)
    for l in lines:
        if l.strip() == "":
            continue
        if not is_comment(l):
            codelines.append(l)
    return codelines 


def resolve_file(dest, project_dir, f):
    relative_path = str(f)[len(project_dir):]
    if relative_path.startswith("/"):
        return dest + relative_path
    else:
        return dest + "/" + relative_path
 
   
def refine_project(project_dir, dest, from_group, to_group, code = 'scala'):
    if not os.path.exists(dest):
        print("create dir ", dest)
        os.makedirs(dest)
    files = scan_dir(project_dir, '.'+code)
    for f in files:
        lines = filter_code(f)
        new_file = resolve_file(dest, project_dir, f)
        new_parent_dir = new_file[0:new_file.rindex('/')]
        if not os.path.exists(new_parent_dir):
            os.makedirs(new_parent_dir)
        with open(new_file,'w+') as fwrite:
            fwrite.writelines(lines) 
            print("generate file " , new_file)
            regroup(new_file, from_group, to_group)
    print("finish refinement")


if __name__ == "__main__":
    path = '/Users/mac/Development/learn/er-spark/src/main/scala/org/wumiguo/ser/methods/util/Converters.scala'
    lines = load(path)
    #print("lines " , lines)
    codelines = filter_code(path)
    for l in codelines:
        print("c:", l )
    proj_dir = '/Users/mac/Development/learn/er-spark'
    dest = '/tmp/cleancode'
    print("resolve file: ", resolve_file(dest, proj_dir, path))
    #filter_project(proj_dir, dest, 'scala')
    fg = 'org.wumiguo.ser'
    tg = 'org.bd720.ercore'
    refine_project(proj_dir, dest, fg, tg, 'scala')
 

