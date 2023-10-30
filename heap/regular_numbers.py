# divide by 60
# n^3 numbers. Sorting will take O(n^3logn)
# get the first n number
import heapq


def regular_numbers(n):
    twos = [2 ** i for i in range(n)]
    threes = [3 ** i for i in range(n)]
    fives = [5 ** i for i in range(n)]

    solution = set()
    for two in twos:
        for three in threes:
            for five in fives:
                solution.add(two * three * five)

    return sorted(solution)[:n]


# O(nlog(n)) each heap op takes log(n) for n numbers
def regular_numbers2(n):
    solution = [1]
    last = 0; count = 0

    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x; count +=1
            heapq.heappush(solution, 2*x)
            heapq.heappush(solution, 3*x)
            heapq.heappush(solution, 5*x)
