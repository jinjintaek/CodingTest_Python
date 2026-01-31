from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]

    for course_size in course:
        counter = Counter()
        for order in orders:
            for comb in combinations(order, course_size):
                counter[comb] += 1

        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for comb, count in counter.items():
                    if count == max_count:
                        answer.append(''.join(comb))
                        
    return sorted(answer)