#!/usr/bin/env python
# -*- coding: utf-8 -*-


def filter_codes(lines):
    comment_stack = 0
    find_comment = False
    codelines = []
    for l in lines:
        if l.strip() == "":
            continue
        elif comment_line(l):
            continue
        elif comment_start(l):
            find_comment = True
            comment_stack+=1
            continue
        elif comment_end(l):
            if comment_endwith_start(l):
                comment_stack+=1
            comment_stack-=1
            if comment_stack ==0:
                find_comment = False
            continue
        elif not find_comment and has_inner_comment(l):
            snip = trim_inner_comment(l)
            if snip.strip() != '':
                codelines.append(snip)
        elif not find_comment and comment_endwith_start(l):
            comment_stack+=1
            find_comment = True
            if comment_stack ==1:
                codelines.append(extract_before_comment(l))
            continue
        elif comment_startwith_end(l):
            comment_stack-=1
            if comment_stack != 0:
                continue
            find_comment = False
            snip = extract_after_comment_end(l)
            if snip.strip() != '':
                codelines.append(snip if snip.endswith('\n') else snip + '\n')
            continue
        elif not find_comment and has_line_comment(l):
            snip = extract_before_line_comment(l)
            if snip.strip() != '':
                codelines.append(snip if snip.endswith('\n') else snip + '\n')
            continue 
        elif not find_comment: 
            codelines.append(l)
    return codelines 


def extract_before_comment(line):
    index = line.index("/*")
    return line[0:index]


def extract_before_line_comment(line):
    index = line.index("//")
    return line[0:index]


def is_comment(content):
  sc = str(content)
  sc = sc.strip()
  if comment_line(sc) or comment_start(sc) or comment_end(sc):
      return True
  return False


def comment_line(content):
    sc = str(content).strip()
    if sc.startswith("//"):
        return True
    elif sc.startswith("/*") and sc.endswith("*/"):
        return True 
    return False


def comment_start(content):
    sc = str(content).strip()
    if sc.startswith("/*"):
        return True
    return False


def comment_endwith_start(content):
    sc = str(content).strip()
    if "/*" in sc and not sc.startswith("/*"):
        return True
    return False


def has_line_comment(content):
    sc = str(content).strip()
    if "//" in sc and not sc.startswith("//"):
        return True
    return False


def comment_startwith_end(content):
    sc = str(content).strip()
    if "*/" in sc and not sc.endswith("*/"):
        return True
    return False


def extract_after_comment_end(line):
    index = line.index("*/")
    if index+2 < len(line):
        return line[index+2:]
    else: 
        return ''


def comment_end(content):
    sc = str(content).strip()
    if sc.endswith("*/"):
        return True
    return False


def has_inner_comment(content):
    sc = str(content)
    if not sc.startswith("/*") and "/*" in sc and "*/" in sc and not sc.endswith("*/"):
        return True
    return False 


def trim_inner_comment(content):
    sc = str(content)
    left = sc.index("/*")
    right = sc.index("*/")
    return sc[0:left] + sc[right+2:]
    

if __name__ == '__main__':
    print(is_comment("/* hello */"))
    print(is_comment("// test " ))
    print(is_comment("*.a"))
    print(is_comment("aa */"))
    print(is_comment("a*b"))
