def length(head):
    if not head:
        return 0
    return 1+ length(head.next)

def intersect(a, b):
    m, n = length(a) + length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m-n):
            cur_a = cur_a.next
    else:
        for _ in range(n-m):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next

    return cur_a

