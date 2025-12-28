

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick_sort(left)+middle +quick_sort(right)

arr=[]
n=int(input("Enter the size of an Array :"))
for i in range(n):
    ele=int(input("Enter Array Element :"))
    arr.append(ele)
print(quick_sort(arr))


# quick_sort([5,3,8,3])   pivot=5
#  ├── quick_sort([3,3])  pivot=3
#  │        ├── quick_sort([]) → []
#  │        ├── middle=[3,3]
#  │        └── quick_sort([]) → []
#  │        return [3,3]
#  │
#  ├── middle = [5]
#  │
#  └── quick_sort([8]) → [8]

# Final return = [3,3] + [5] + [8]
#               = [3,3,5,8]
