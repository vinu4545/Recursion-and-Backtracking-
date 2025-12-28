# a=int(input("Enter a Number :"))
# b=int(input("Enter a Number :"))
# def power(a,b):
#     if b==0:
#         return 1
#     if b==1:
#         return a
#     if b%2==0:
#         return power(a,b//2)*power(a,b//2)
#     else:
#         return a*power(a,b//2)*power(a,b//2)

# print(power(a,b))


a=int(input("Enter a Number :"))
b=int(input("Enter a Number :"))
def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    
    ans=power(a,b//2)
    if b%2==0:
        print(b)
        print(ans*ans)
        print("-------")
        return ans*ans
    else:
        print(b)
        print(a*ans*ans)
        print("-------")
        return a*ans*ans

print(power(a,b))
