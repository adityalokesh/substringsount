n=input("enter the string")
x=input("enter the substring")
count=0
for i in range(len(n)):
    if(n.find(x)==-1):
       count=count
    else:
     pos=int(n.find(x))
     n=n[pos+1:]
     count+=1
print(count)

