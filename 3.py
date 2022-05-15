filename="mh.txt"
infile=open(filename,'r')
m=infile.readlines()
infile.close()
h=0
for i in m:
    t=i.rstrip().split(",")
    print(t[0])
    answ=input()
    if answ==t[-1]:
        h+=1
un=input("enter your username ")
print(un,'\t',h)
outfile=open("mhr.txt",'w')
outfile.write(un+'\t'+str(h))
outfile.close()