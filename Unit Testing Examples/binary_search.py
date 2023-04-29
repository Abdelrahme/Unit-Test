def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
high=[5,2,3,5,9,82,654,23,12,16,11561,57,516516,5555]
print(binary_search(high,12))