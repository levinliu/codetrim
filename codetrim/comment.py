#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_comment(content):
  sc = str(content)
  sc = sc.strip()
  if sc.startswith("/**") or sc.startswith("//") or sc.startswith("*"):
    return True
  return False


if __name__ == '__main__':
  print(is_comment("/** hello */"))
  print(is_comment("// test " ))
  print(is_comment("* test" ))
  print(is_comment("*.a"))
