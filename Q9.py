# 해당수가 소수인지 찾기
def find(n):
    
    for i in range(2,n):
        if(n%i==0):
            return
    
    print(n)

if __name__ == '__main__':
    n = int(input())
    for i in range(2,n+1):
        find(i)