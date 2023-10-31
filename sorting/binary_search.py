def binary_search(array, x):
    low = 0; high = len(array) - 1
    found = False

    while low <= high and not found:
        mid = (low + high)//2
        if x == array[mid]:
            found = True
        elif x < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return found