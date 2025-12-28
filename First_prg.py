def recur(n):
    if n==0:
        return n
    print(n)
    print("--------------")
    return n+recur(n-1)
    print(n)
    print("--------------")
print(recur(5))