n=int(input())
s=0
d=n**2
t=d
while t:
    r=t%10
    s=s+r
    t=t//10
if(n==s):
    print('Neon Number')
else:
     print('Not Neon Number')