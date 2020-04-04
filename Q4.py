
def slf(n):

    print(n)
    if(n==1):
        return
    slf(n-1)

if __name__ == "__main__":
    n = int(input())
    slf(n)