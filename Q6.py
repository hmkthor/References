
"""
def reverse(str):

    reversed = ""
    n = len(str)
    
    while(n>0):
        reversed += str[n-1]
        n = n-1
    
    print(reversed)
        
if __name__ == "__main__":
    str = input()
    
    reverse(str)
"""

def reverse(n):
    if n==0:
        return 0
    
    print(n%10, end = '')
    reverse(n//10)

if __name__ == "__main__":
    n = int(input())
    reverse(n)