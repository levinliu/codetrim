#!/usr/bin/env python                                                       
# -*- coding: utf-8 -*-


def resolve_file(dest, project_dir, f):                                    
    relative_path = str(f)[len(project_dir):]
    if relative_path.startswith("/"):
        return dest + relative_path
    else:
        return dest + "/" + relative_path
