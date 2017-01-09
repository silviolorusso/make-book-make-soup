#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys


f = open(sys.argv[1], 'r')

f = f.read()

# print Make Square

f = re.sub(r"A","a", "1", f)
f = re.sub(r"B","b", "2", f)
f = re.sub(r"C","c", "3", f)
f = re.sub(r"D","d", "4", f)
f = re.sub(r"E","e", "5", f)
f = re.sub(r"F","f", "6", f)
f = re.sub(r"G","g", "7", f)
f = re.sub(r"H","h", "8", f)
f = re.sub(r"I","i", "9", f)
f = re.sub(r"I","i", "10", f)
f = re.sub(r"J","j", "11", f)
f = re.sub(r"K","k", "12", f)
f = re.sub(r"L","l", "13", f)
f = re.sub(r"M","m", "14", f)
f = re.sub(r"N","n", "15", f)
f = re.sub(r"O","o", "16", f)
f = re.sub(r"P","p", "17", f)
f = re.sub(r"Q","q", "18", f)
f = re.sub(r"R","r", "19", f)
f = re.sub(r"S","s", "20", f)
f = re.sub(r"T","t", "21", f)
f = re.sub(r"U","u", "22", f)
f = re.sub(r"V","v", "23", f)
f = re.sub(r"W","w", "24", f)
f = re.sub(r"X","x", "25", f)
f = re.sub(r"Y","y", "26", f)
f = re.sub(r"Z","z", "27", f)

# f = re.sub(r"[^■]", " ", f)

print f

