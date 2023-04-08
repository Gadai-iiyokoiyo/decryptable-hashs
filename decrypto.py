am=input(">")
for a in am.split(" "):
    for i in open("hasht.txt","r").readlines():
        isp=i.split(":=")
        if(isp[1].replace("\n","")==a):
            print(isp[0],end="")
            break
print("\ncomplete. exit.")
