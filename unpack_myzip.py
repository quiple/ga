#!/usr/bin/env python

import os
import sys
import zlib
from pathlib import Path

d = sys.argv[1]
o = Path(d).stem
m = b'\x00\xFF\x4D\x59\x5A\x49\x50\x00'
ex = '.bin'
i = 0
j = 0

with open(d, 'rb') as f:

  while i < os.path.getsize(d):
    k = 0
    f.seek(i, 0)

    if f.read(8) == m:

      while True:
        k += 1
        f.seek(i + 0x800 * k, 0)

        if f.read(8) == m or f.read(8) == b'':
          f.seek(i + 12, 0)
          g = zlib.decompress(f.read(0x800 * k - 12))
          os.makedirs(o, exist_ok = True)
          with open(o + '/' + str(j) + '_' + str(hex(i)) + ex, 'wb') as n:
            n.write(g)
          print(o + '/' + str(j) + '_' + str(hex(i)) + ex)
          i += 0x800 * k
          break

    j += 1
