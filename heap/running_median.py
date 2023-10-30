# given a stream of numbers, print out the median of the list so far after each new element

import heapq


# running time is O(nlogn), each heappush and heappop operation takes O(logn)
# >< , min heap for bigger number, max heap for smaller number.
# rebalance makes sure each half have the same number of items
def get_median(min_heap, max_heap):
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    elif len(min_heap) < len(max_heap):
        return -1 * max_heap[0]

    else:
        return (min_heap[0] + -1 * max_heap[0]) / 2.0


def add(num, min_heap, max_heap):
    if len(min_heap) + len(max_heap) < 1:
        heapq.headpush(min_heap, num)
        return

    median = get_median(min_heap, max_heap)
    if num > median:
        heapq.headpush(min_heap, num)
    else:
        heapq.headpush(max_heap, -1 * num)


def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -1 * root)
    elif len(max_heap) > len(min_heap) + 1:
        root = -1 * heapq.heappop(max_heap)
        heapq.heappush(min_heap, root)


def print_median(min_heap, max_heap):
    print(get_median(min_heap, max_heap))


def running_median(stream):
    min_heap = []
    max_heap = []
    for num in stream:
        add(num, min_heap, max_heap)
        rebalance(min_heap, max_heap)
        print_median(min_heap, max_heap)
