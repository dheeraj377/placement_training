a=list(map(int,input().split()))
sum=0
for i in range(0,len(a)):
    if i%2!=0:
        if a[i]%2==0:
            sum+=a[i]
print(sum)
        
    
