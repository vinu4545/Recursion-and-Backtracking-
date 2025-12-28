arr=[]
n=int(input("Enter array size : "))
for i in range(0,n):
    ele=int(input("Enter a element : "))
    arr.append(ele)

def bubble_Sort(arr,n):
    if n==0 or n==1:
        return arr
    for i in range(0,n-1):       #0-->n-1
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)
    
    return bubble_Sort(arr,n-1)
print(bubble_Sort(arr,n))