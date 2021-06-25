N=1000
sieve=[1]*1000
def gen_sieve():
    sieve[0]=sieve[1]=0
    for i in range(2,int(N**0.5)+1):
        if sieve[i]==1:
            for j in range(i*i,N,i):
                sieve[j]=0
gen_sieve()
n=int(input())
for i in range(n-1,0,-1):
    if sieve[i]==1:
        k=i
        break
print(k)    
j=n+1       
while j>n:      
    if sieve[j]==1:
        h=j
        break
    j=j+1
print(h)    
if (n-k)>(h-n):
    print(h)
else:
    print(k)
