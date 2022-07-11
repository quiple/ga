#!/usr/bin/env python

import os
import sys
from pathlib import Path

d = sys.argv[1]
o = Path(d).stem
psb = b'PSB'
gim = b'MIG.00.1PSP'
at3 = b'RIFF'
ex = '.bin'
i = 0
j = 0

with open(d, 'rb') as f:

  while i < os.path.getsize(d):
    k = 0
    f.seek(i, 0)

    while True:
      k += 1
      f.seek(i + 0x800 * k, 0)
      m = f.read(16)

      if m.startswith(psb) or m.startswith(gim) or m.startswith(at3) or m == b'':
        f.seek(i, 0)
        g = f.read(0x800 * k)
        os.makedirs(o, exist_ok = True)
        with open(o + '/' + str(j) + '_' + str(hex(i)) + ex, 'wb') as n:
          n.write(g)
        print(o + '/' + str(j) + '_' + str(hex(i)) + ex)
        i += 0x800 * k
        break

    j += 1
