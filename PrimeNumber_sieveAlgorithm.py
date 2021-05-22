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
if sieve[n]==1:
    print('Prime')
else:
    print('Not Prime')
