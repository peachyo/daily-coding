# low-high-low-high

def alternate(ll):
    prev = ll
    cur = ll.next

    while cur:
        if prev.data > cur.data:
            prev.data, cur.data = cur.data, prev.data

        if not cur.next:
            break

        if cur.next.data > cur.data:
            cur.next.data, cur.data = cur.data, cur.next.data

        prev = cur.next
        cur = cur.next.next

    return ll

