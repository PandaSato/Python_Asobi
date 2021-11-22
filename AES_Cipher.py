import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

salt = bytes.fromhex('7a4ab182abfa7b8aa77aa8a687a6')
salt2 = bytes.fromhex('b6b5b7b567b5b7b65b65bb7b76cc')


## from string, makes its unique hashcode
def getHashCode(str):
    return hashlib.sha256(str.encode()+salt2).hexdigest()[:32]

## Testing AES Cipher
class AESCipher(object):

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()+salt).digest()

    def encrypt(self, str):
        raw = str.encode()
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        try:
            enc = base64.b64decode(enc)
            iv = enc[:AES.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode()
        except:
            return 'DecodeError'
    
    def write(self, txtPath, text):
        cipherText = self.encrypt(text)
        f=open(txtPath,'wb')
        f.write(cipherText)
        f.close()
        
    def readlines(self,txtPath):
        f=open(txtPath,'rb')
        decodedText = self.decrypt(f.read())
        print(decodedText)

    def _pad(self, s):
        padLength = self.bs - len(s) % self.bs
        return s + padLength * bytes([padLength])

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

print(getHashCode("abc"))
cipher = AESCipher('abc')
print(cipher.decrypt(cipher.encrypt("안녕")))
cipher.write('test','안녕\n만나서반가워')
cipher.readlines('test')
