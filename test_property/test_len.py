#!/usr/bin/env python
# coding=utf-8
class test(object):
    @property
    def ret(self):
        return [1,2,3,4]

    def length(self):
        return len(self.ret)

print test().length()
