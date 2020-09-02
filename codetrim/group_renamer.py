#!/usr/bin/env python                                                       
# -*- coding: utf-8 -*-

import os



def regroup(path, from_group, to_group):
    new_path = folder_rename(path, from_group, to_group)
    package_rename(new_path, from_group, to_group)


def regroup_path(path, from_group, to_group):
    fgroup_path = (from_group+'.').replace('.','/')
    tgroup_path = (to_group+'.').replace('.','/')
    new_path = path.replace(fgroup_path,tgroup_path)
    return new_path


def folder_rename(path, from_group, to_group):
    new_path = regroup_path(path, from_group, to_group)
    last_index = new_path.rindex('/')
    new_path_parent = new_path[0:last_index]
    if not os.path.exists(new_path_parent):
        os.makedirs(new_path_parent)
    os.rename(path, new_path)
    print("rename from " + path + " to " + new_path)
    return new_path


def package_rename(path, from_group, to_group):
    new_lines = []
    found_match = False
    with open(path,'r') as f:
        lines = f.readlines()
        for l in lines:
            if from_group in l:
                found_match = True
                l = l.replace(from_group, to_group)
            new_lines.append(l)
    if found_match:
        with open(path,'w+') as f:
            f.writelines(new_lines)
    print("finish package rename on " + path + ' match ' + str(found_match))
    if len(new_lines) > 0:
        print(" first "  + new_lines[0])


if __name__ == '__main__':
    p = '/tmp/cleancode/src/main/scala/org/bd720/ercore/CallERFlowLauncher.scala'
    p = '/tmp/cleancode/src/main/scala/org/bd720/ercore/model/IdDuplicates.scala'
    g1 = 'org.wumiguo.ser'
    g2 = 'org.bd720.ercore'
    regroup(p,g1,g2)
  



