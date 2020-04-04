
def prime_check(n):
    check = [True] * (n+1)
    check[0] = False 
    check[1] = False

    i=2

    while i<=n:
        if(check[i]==True):
            print(i)
            k=1
            j=1
            while(j<=n):
                k = k+1
                j = i*k
                if(j<=n):
                    check[j] = False
                
        i=i+1

if __name__ == '__main__':
    n=int(input())
    prime_check(n)