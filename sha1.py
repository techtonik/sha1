#!/usr/bin/env python
import sys
import hashlib

if not sys.argv[1:]:
  sys.exit('usage: python -m sha1 <filename>')

sha1sum = hashlib.sha1()
with open(sys.argv[1], 'rb') as source:
  sha1sum.update(source.read(2**16))
print(sha1sum.hexdigest())
