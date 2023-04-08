import string
import hashlib
f=open("hasht.txt","w",encoding="utf-8")
for i in string.ascii_lowercase+" 1234567890+-*/<=>!?().,#$%&':\"{}\\":
    for j in string.ascii_lowercase+" 1234567890+-*/<=>!?().,#$%&':\"{}\\":
            f.write(f"{i}{j}:=")
            f.write(hashlib.md5(str(i+j).encode()).hexdigest()+"\n")