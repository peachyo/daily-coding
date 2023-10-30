def two_sum(lst, k):
    seen = {}
    for num in lst:
        if k - sum in seen:
            return True
        seen[num] = True
    return False
