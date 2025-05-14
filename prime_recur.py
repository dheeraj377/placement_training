def prime(n,m=2):
    if n%m==0:
        return False
    if m*m > n:
        return True
    return prime(n,m+1)
n=int(input())
if prime(n):
    print("prime number")
print("not a prime number")

"""n=int(input())
flag=0
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
         flag+=1
         break
if flag==0:
    print("prime")
else:
    print("not prime")"""
