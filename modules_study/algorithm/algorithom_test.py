from hashlib import *

mm = md5()
mm.update("asdf" + '1234dsgadsfa')
print mm.digest()
print mm.digest_size
# print mm.digest.block_size

mm = new("ripemd160")
print mm.digest_size
mm.update("asdf")
print mm.digest()
mm.update('1234dsgadsfa')
print mm.digest()
print mm.digest_size

# dk = pbkdf2_hmac('sha256', b'password', b'salt', 100000)
