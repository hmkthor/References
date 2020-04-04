def cal(n):
    sum =0

    for i in range (0,n+1):
        sum = sum + i

    print(sum)

if __name__ == "__main__":
    n = int(input())
    cal(n)