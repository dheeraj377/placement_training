l=list(map(int,input().split()))
a=l[0]
count=0
for i in l:
    if i>a:
        a=i
        count+=1
print(count)

               
        
