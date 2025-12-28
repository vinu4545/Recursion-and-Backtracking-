def merge(arr, s, e):
    mid = (s + e) // 2
    arr2 = arr[s:mid + 1]
    arr3 = arr[mid + 1:e + 1]

    idx_arr2 = 0
    idx_arr3 = 0
    main_arr_idx = s

    while idx_arr2 < len(arr2) and idx_arr3 < len(arr3):
        if arr2[idx_arr2] < arr3[idx_arr3]:
            arr[main_arr_idx] = arr2[idx_arr2]
            idx_arr2 += 1
        else:
            arr[main_arr_idx] = arr3[idx_arr3]
            idx_arr3 += 1
        main_arr_idx += 1

    while idx_arr2 < len(arr2):
        arr[main_arr_idx] = arr2[idx_arr2]
        idx_arr2 += 1
        main_arr_idx += 1

    while idx_arr3 < len(arr3):
        arr[main_arr_idx] = arr3[idx_arr3]
        idx_arr3 += 1
        main_arr_idx += 1


def merge_sort(arr, s, e):
    if s >= e:
        return

    mid = (s + e) // 2
    merge_sort(arr, s, mid)
    merge_sort(arr, mid + 1, e)
    merge(arr, s, e)


arr = []
n = int(input("Enter size of array: "))
for i in range(n):
    ele = int(input(f"Enter element {i+1}: "))
    arr.append(ele)

print("Original array:", arr)
merge_sort(arr, 0, n - 1)
print("Sorted array:", arr)



# merge_sort(0,4)
# │
# ├── merge_sort(0,2)
# │   │
# │   ├── merge_sort(0,1)
# │   │   ├── merge_sort(0,0)   → returns
# │   │   ├── merge_sort(1,1)   → returns
# │   │   └── merge(0,1)
# │   │
# │   ├── merge_sort(2,2)       → returns
# │   └── merge(0,2)
# │
# ├── merge_sort(3,4)
# │   ├── merge_sort(3,3)       → returns
# │   ├── merge_sort(4,4)       → returns
# │   └── merge(3,4)
# │
# └── merge(0,4)


