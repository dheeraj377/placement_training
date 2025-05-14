def prime(n,m=2):
    if n<2:
        return False
    if m*m<n:
        return True
    if n==2:
        return True
    if n%m==0:
        return False
    return prime(n,m+1)
def fun(l,i=0):
    if i==len(l):
        return 0
    if prime(l[i]):
         return 1+fun(l,i+1)
    else:
        return fun(l,i+1)
l=[2,3,5,7,9,4]
print(fun(l))
