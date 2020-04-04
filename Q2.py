
def shownums(k):
    if k>1:
        shownums(k-1)
    print(k)

if __name__ == "__main__":
    n = int(input())
    shownums(n)