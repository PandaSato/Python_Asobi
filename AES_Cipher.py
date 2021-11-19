from Crypto.Cipher import AES
import hashlib 

hexdigest = hashlib.sha256('a'.encode()).hexdigest()
digest = hashlib.sha256('a'.encode()).digest()
digest2 = hashlib.sha256('b'.encode()).digest()

#cipher = AES.new(digest, AES.MODE_CBC,digest2)

test = [2, 3, 5, 7]
# convert list to bytearray
byte_array = bytearray(test)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')