#!/usr/bin/env python
# coding=utf-8
from pkg_resources import iter_entry_points

for entry_point in iter_entry_points('magnum.drivers'):
    print entry_point, entry_point.load(require=False)
