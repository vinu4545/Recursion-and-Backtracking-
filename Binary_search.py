arr = []
n = int(input("Enter size of an array: "))

for i in range(n):
    ele = int(input("Enter array element: "))
    arr.append(ele)

arr.sort() 
print("Sorted array:", arr)

key = int(input("Enter a key element to search: "))

def binary_search(low, high, key):
    if low > high:
        print("Element not found")
        return

    mid = (low + high) // 2  

    if arr[mid] == key:
        print(f"Element found at position: {mid}")
        return
    elif arr[mid] > key:
        binary_search(low, mid - 1, key)
    else:
        binary_search(mid + 1, high, key)

binary_search(0, len(arr) - 1, key)
