
n=int(input("Enter the length of the ladder :"))
def no_of_ways(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return no_of_ways(n-1)+no_of_ways(n-2)
    # return aims
print(no_of_ways(n))