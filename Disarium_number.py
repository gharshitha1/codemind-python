n=int(input())
t=n
s=0
rev=0
while n:
    rev=(rev*10)+n%10
    n=n//10
for i in range(1,rev+1):
        r=rev%10
        s+=r**i
        rev=rev//10
        if s==t:
            print(True)
            break
else:
    print(False)
        
    
