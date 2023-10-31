from collections import deque


def max_subarray(lst, k):
    for i in range(len(lst) - k + 1):
        print(max(lst[i:i + k]))


def max_of_subarrays(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i]>=lst[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i]>= lst[q[-1]]:
            q.pop()
        q.append(i)
        print(lst[q[0]])


