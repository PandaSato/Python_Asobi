##Test Diffie Hellman key exchange

import random

p = 2**61-1 ## mersenne prime number

g=random.randint(2,p-2)
a=random.randint(2,p-2)
b=random.randint(2,p-2)
ga=pow(g,a,p) ## public key g^a
gb=pow(g,b,p) ## public key g^b
key1=pow(ga,b,p) 
key2=pow(gb,a,p) 
print("key : "+hex(key1)+" "+hex(key2)) #get g^ab
print(" ".join(["pk1 : "+hex(ga),"pk2 : "+hex(gb),"pk1*pk2 : "+hex((key1*key2)%p)]))