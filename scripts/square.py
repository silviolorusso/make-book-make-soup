#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys


f = open(sys.argv[1], 'r')

f = f.read()

# print Make Square

f = re.sub(r" ", "■", f)
f = re.sub(r"[^■]", " ", f)

print f