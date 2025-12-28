
res=[]
def subset(arr,i,ans):
    if i==len(arr):
        res.append(ans.copy())
        return ans
    subset(arr,i+1,ans)
    ans.append(arr[i])
    subset(arr,i+1,ans)
    ans.pop()

arr=[1,2,3]
subset(arr,0,[])
print(f'subsets are {res}')