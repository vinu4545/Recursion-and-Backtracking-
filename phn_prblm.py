
digits=["","","abc","def","ghi","jkl","mno","pqr","stu","vwxyz"]

res=[]
def permutaion(s,i,ans):
    if i==len(s):
        res.append(ans[:])
        return 
    letters=digits[int(s[i])]
    for letter in letters:
        ans.append(letter)
        permutaion(s,i+1,ans)
        ans.pop()

strr=input("Enter a digit :")
permutaion(strr,0,[])
print(f"Answer : {res}")