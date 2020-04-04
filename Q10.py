from math import sqrt

def find(n):
    gcd_front = []
    gcd_back = []

    i=1
    while(i<=sqrt(n)):
        if(n%i==0):
            gcd_front.append(i)
            if(i!=n//i):
                gcd_back.insert(0,n//i)
        i = i+1
    
    if(len(gcd_front)==1):
        print(str(n)+' 은 소수 입니다. ')
        return

    print(gcd_front+gcd_back)

if __name__ == "__main__":
    n = int(input())

    for i in range(2,n+1):
        find(i)
    

