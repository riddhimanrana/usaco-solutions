N = int(input())
bacteria_levels = list(map(int, input().split()))

def apply_pesticide(current_level, desired_level):
    diff = desired_level - current_level
    return abs(diff)

total_applications = 0

for i in range(N-1, -1, -1):
    desired_level = bacteria_levels[i-1] if i > 0 else 0
    total_applications += apply_pesticide(bacteria_levels[i], desired_level)

print(total_applications + 1)
