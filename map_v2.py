#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keys = line.split()
    for idx in range(0,len(keys)-1):
        value = 1
        print( "%s\t%d" % (keys[idx]+'-'+keys[idx+1], value) )
