from collections import Counter

def possible_hay_types(n, hay_preferences):
    hay_count = Counter(hay_preferences)
    half_n = n // 2
    candidates = [hay for hay, count in hay_count.items() if count > half_n]

    if n % 2 == 0:
        half_hays = [hay for hay, count in hay_count.items() if count == half_n]
        if len(half_hays) == 2:
            candidates.extend(half_hays)

    if n == 2:
        candidates = False
    if not candidates:
        return [-1]
    return sorted(set(candidates))

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    hay_preferences = list(map(int, input().split()))
    result = possible_hay_types(N, hay_preferences)
    results.append(result)

for result in results:
    print(' '.join(map(str, result)))
