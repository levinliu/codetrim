#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CodeTrim to filter specific lang and trim code
"""

import os

from group_renamer import regroup, package_rename
from comment import filter_codes
from file_scanner import scan_dir
from copy_static import copy_res

def load(path):
    with open(path, "r") as afile:
        lines = afile.readlines()
        return lines
    return None 


def filter_code(path):
    lines = load(path)
    return filter_codes(lines)


def resolve_file(dest, project_dir, f):
    relative_path = str(f)[len(project_dir):]
    if relative_path.startswith("/"):
        return dest + relative_path
    else:
        return dest + "/" + relative_path
 
   
def refine_project(project_dir, dest, from_group, to_group, types = ['.py']):
    if not os.path.exists(dest):
        print("create dir ", dest)
        os.makedirs(dest)
    files = scan_dir(project_dir, types)
    for f in files:
        lines = filter_code(f)
        new_file = resolve_file(dest, project_dir, f)
        new_parent_dir = new_file[0:new_file.rindex('/')]
        if not os.path.exists(new_parent_dir):
            os.makedirs(new_parent_dir)
        with open(new_file,'w+') as fwrite:
            fwrite.writelines(lines) 
        print("generate file " + new_file)
        regroup(new_file, from_group, to_group)
    print("finish code refinement")
    handle_resources(project_dir, dest)


def regroup_after_refine(project_dir, from_group, to_group, types):
    files = scan_dir(project_dir, types)
    for f in files:
        package_rename(f, from_group, to_group)


def handle_resources(project_dir, dest):
    res_paths = ["/src/main/resources", "/src/test/resources"]
    for res in res_paths:
        res_from = project_dir + res
        res_to = dest + res
        copy_res(res_from, res_to) 
        print("finish resource refinement from %s to %s " %(res_from,res_to))


if __name__ == "__main__":
    proj_dir = '/Users/mac/Development/learn/er-spark'
    dest = '/tmp/cleancode'
    fg1 = 'org.wumiguo.ser'
    tg1 = 'org.bd720.ercore'
    types = ['.scala', '.java' ]
    refine_project(proj_dir, dest, fg1, tg1, types)
    proj2 = "/Users/mac/Development/learn/er-job"
    dest2 = "/tmp/cleancode-erjob"
    fg2 = 'org.wumiguo.erjob'
    tg2 = 'org.bd720.erjob'
    refine_project(proj2, dest2, fg2, tg2, types)
    regroup_after_refine(proj2, fg1, tg1, types)
 

