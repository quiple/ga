#!/usr/bin/env python

import os
import sys
import zlib
from pathlib import Path

d = sys.argv[1]
o = Path(d).stem
m = b'\x00\xFF\x4D\x59\x5A\x49\x50\x00'
ex = '.bin'

with open(d, 'rb') as f:
  s = os.path.getsize(d)
  g = zlib.compress(f.read(), level = 7)

with open(o + '_compressed' + ex, 'wb') as n:
  n.write(m + s.to_bytes(4, byteorder = 'big') + g)
