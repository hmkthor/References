
def find(n):

    for i in range(2,n):
        if(n%i==0):
            print(str(n)+' is not a prime number.')
            return
    
    print(str(n)+' is a prime number')

if __name__ == '__main__':
    n=int(input())
    find(n)