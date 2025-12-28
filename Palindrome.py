s = input("Enter a String : ")

def reversing(s, i, j):
    if i >= j:
        return s
    s[i], s[j] = s[j], s[i]
    return reversing(s, i + 1, j - 1)

lst = list(s)
reversed_list = reversing(lst, 0, len(lst) - 1)
reversed_str = ''.join(reversed_list)
if reversed_str==s:
    print("Given string is Palindrome")
else:
    print("Given string is not Palindrome") 