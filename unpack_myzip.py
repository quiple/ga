#!/usr/bin/env python

import os
import sys
import zlib
from pathlib import Path

d = sys.argv[1]
o = Path(d).stem
m = b'\x00\xFFMYZIP'
psb = b'PSB'
gim = b'MIG.00.1PSP'
at3 = b'RIFF'
cnut = b'\xFA\xFARIQS'
bmp = b'BM'
phd = b'PPHD'
i = 0
j = 0

with open(d, 'rb') as f:

  while i < os.path.getsize(d):
    k = 0
    f.seek(i, 0)

    if f.read(16).startswith(m):

      while True:
        k += 1
        f.seek(i + 0x800 * k, 0)

        if f.read(16).startswith(m) or f.read(16) == b'':
          f.seek(i + 12, 0)
          g = zlib.decompress(f.read(0x800 * k - 12))
          ex = '.bin'
          if g.startswith(psb): ex = '.psb'
          if g.startswith(gim): ex = '.gim'
          if g.startswith(at3): ex = '.at3'
          if g.startswith(cnut): ex = '.cnut'
          if g.startswith(bmp): ex = '.bmp'
          if g.startswith(phd): ex = '.phd'
          os.makedirs(o, exist_ok = True)
          with open(o + '/' + str(j) + '_' + str(hex(i)) + ex, 'wb') as n:
            n.write(g)
          print(o + '/' + str(j) + '_' + str(hex(i)) + ex)
          i += 0x800 * k
          break

    j += 1
