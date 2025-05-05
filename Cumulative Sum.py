def cumulative_sum(k):
    total = []
    start = 0
    for i in k:
        start += i
        total.append(start)
    return total
k = [1, 2, 3, 4, 5]
print(cumulative_sum(k))
