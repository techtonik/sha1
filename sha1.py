import sys
import hashlib

if not sys.argv[1:]:
  sys.exit('usage: python -m sha1 <filename>')

print(hashlib.sha1(open(sys.argv[1], 'rb').read()).hexdigest())
