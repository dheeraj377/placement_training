"""def reverse(n,r=0):
    if n==0:
        return r
    r=r*10+(n%10)
    n=n//10
    return reverse(n,r)
n=int(input())
print(reverse(n))"""
n=int(input())
r=0
while n:
    r=(n%10)+r*10
    n=n//10
print(r)


    
    
