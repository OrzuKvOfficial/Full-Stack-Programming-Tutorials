import bisect

def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1
