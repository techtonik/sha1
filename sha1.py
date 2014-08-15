#!/usr/bin/env python
"""
usage: python -m sha1 <filename>
"""
import sys
import hashlib

# --- these fields are required for packaging
__version__ = '0.5'
__author__ = 'anatoly techtonik <techtonik@gmail.com>'
__license__ = 'Public Domain'
# /-- these fields are required for packaging

if not sys.argv[1:]:
  sys.exit(__doc__.strip())

sha1sum = hashlib.sha1()
with open(sys.argv[1], 'rb') as source:
  sha1sum.update(source.read(2**16))
print(sha1sum.hexdigest())
