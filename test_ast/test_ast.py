#!/usr/bin/env python
# coding=utf-8
import ast

print eval('1 + 2')
print eval("__import__('os').system('dir')")

print '='*50
print ast.literal_eval("__import__('os').system('dir')")
