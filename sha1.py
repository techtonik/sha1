import sys
import hashlib

print(hashlib.sha1(open(sys.argv[1], 'rb').read()).hexdigest())
