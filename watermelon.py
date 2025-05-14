w=int(input("enter weight of watermelon"))
if (w%2!=0 or w==2):
    print("No")
else:
    a=w//2
    if(a%2==0):
        print(a,a)
    else:
        print(a-1,a+1)
