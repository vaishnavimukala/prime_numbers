#def prime(n):
#   count=0
#   for i in range(2,n+1):
#       if n%i==0:
#           count+=1
#   if count==1:
#       return True
#   else:
#       return False
#n=int(input())
#l=[]
#for i in range(1,n+1):#find out factors of n
#   if n%i==0:
#        l.append(i)
#print(l)        
#for i in l:
#    if prime(i):#check if factor is prime or not
#print(i,end=' ')
N=1000
sieve=[1]*1000
def gen_seive():
    sieve[0]=sieve[1]=0
    for i in range(2,int(N**0.5)+1):
        if sieve[i]==1:
            for j in range(i*i,N,i):
                sieve[j]=0
gen_seive()
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        if sieve[i]==1:
            print(i,end=' ')
            
#if sieve[n]==1:
#        print('prime ')
#else:
#        print("not prime")
    
        
