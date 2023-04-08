import hashlib,sys
if(len(sys.argv)==2):
    if(sys.argv[1]=="-f" or sys.argv[1]=="/f"):
        am=open(input("file name:"),"r").read().lower().replace("\n","\\n")
    else:
        am=input(">").lower()
else:
    am=input(">").lower()
a=[]
for i2 in range(0,len(am),2):
    if(len(am[i2:i2+2])!=2):
        print("Target token length is not 2. Abort.")
        print("------------------------------------")
        print("Problem Token:\""+am[i2:i2+4]+"\"")
        exit()
    a.append(am[i2:i2+2])

for j in a:
    for i in open("hasht.txt","r").readlines():
        isp=i.split(":=")
        if(isp[0].replace("\n","")==j):
            print(isp[1].replace("\n",""),end=" ")
            break