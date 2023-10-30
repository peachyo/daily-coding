# top k pairs of websites with the greatest similarity
# similarity between websites equals number of users in common/total users. known as Jaccard index
import heapq
from collections import defaultdict


# for each pair of website, to cacluate union of its users, take O(n^2*m),
# where n is number of websites and m is the number of users
def compute_similarity(a, b, visitors):
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b])


def top_pairs(log, k):
    visitors = defaultdict(set)
    for site, user in log:
        visitors[site].add(user)

    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.headpush(pairs, (0, ('', '')))

    for i in range(len(sites) - 1):
        for j in range(i + 1, len(sites)):
            score = compute_similarity(sites[i], sites[j], visitors)
            heapq.heappushpop(pairs, (score, (sites[i], sites[j])))

    return [pair[i] for pair in pairs]
