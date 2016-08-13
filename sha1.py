#!/usr/bin/env python
"""
usage: python -m sha1 <filename>
       python -m sha1 < filename
"""
import sys
import hashlib

# --- these fields are required for packaging
__version__ = '1.1'
__author__ = 'anatoly techtonik <techtonik@gmail.com>'
__license__ = 'Public Domain'
__url__ = 'https://github.com/techtonik/sha1'
# /-- these fields are required for packaging

if sys.stdin.isatty():  # stdin is not piped
  if not sys.argv[1:]:
    sys.exit(__doc__.strip())
  source = open(sys.argv[1], 'rb')
else:
  source = sys.stdin

sha1sum = hashlib.sha1()
block = source.read(2**16)
while len(block) != 0:
  sha1sum.update(block)
  block = source.read(2**16)
print(sha1sum.hexdigest())
source.close()

# quick test should give you this
#
#   $ sha1.py UNLICENSE 
#   fad0fbaf831fead007f4465821459c58a2973eb0
#   $ sha1.py < UNLICENSE 
#   fad0fbaf831fead007f4465821459c58a2973eb0
