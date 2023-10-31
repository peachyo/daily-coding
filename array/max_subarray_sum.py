# Kadane's algorith. include or exclude current number, O(n)
def max_subarray_sum(arr):
    max_so_far = max_ending_here = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def max_circular_subarray(arr):
    max_subarray = max_subarray_sum(arr)
    max_subarray_wraparround = sum(arr) - max_subarray

    return max(max_subarray_wraparround, max_subarray)


if __name__ == '__main__':
    input = [-5,-1,-8,-9]
    print(max_subarray_sum(input))
    input = [34, -50, 42, 14, -5, 86]
    print(max_subarray_sum(input))
