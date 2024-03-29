def merge_arrays(arr1, arr2):
    merged = []
    i = 0
    j = 0
 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
 
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
 
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
 
    return merged
 
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
merged_array = merge_arrays(arr1, arr2)
print(*merged_array)
