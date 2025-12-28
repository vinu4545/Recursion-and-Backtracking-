n=int(input("Enter Length of Fibonacci Series that you wwant !!"))
def fibo(n):
    if n==0 or n==1:
        print(0)
        print(1)
    if n>1:
        fibo(n-1)+fibo(n-2)
        print(n)
fibo(10)
