
def game(n):
    for i in range (1,n+1):
        if i%3==0:
            print('x', end=' ')
        else :
            print(i, end=' ')

if __name__ == "__main__":
    n = int(input())
    game(n)