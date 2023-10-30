import bisect


class HitCounter:
    def __init__(self):
        self.hits = []

    def record(self, timestamp):
        # self.hits.append(timestamp)
        bisect.insort_left(self.hits, timestamp)

    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        # count = 0
        # for hit in self.hits:
        #     if lower <= hit <= upper:
        #         count += 1
        # return count
        left = bisect.bisect_left(self.hits, lower)
        right = bisect.bisect_right(self.hits, upper)
        return right - left


