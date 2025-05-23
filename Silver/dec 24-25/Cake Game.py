def calculate_cake_distribution(cake_sizes):
    total_cakes = len(cake_sizes)
    total_cake_size = sum(cake_sizes)
    elsie_turns = total_cakes // 2 - 1

    if elsie_turns < 0:
        return [total_cake_size, 0]

    cumulative_sum = [0] * (total_cakes + 1)
    for i in range(1, total_cakes + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + cake_sizes[i - 1]

    max_left_sum = [0] * (elsie_turns + 1)
    max_right_sum = [0] * (elsie_turns + 1)

    for i in range(1, elsie_turns + 1):
        max_left_sum[i] = cumulative_sum[i]
        max_right_sum[i] = cumulative_sum[total_cakes] - cumulative_sum[total_cakes - i]

    max_elsie_share = float('-inf')
    for left in range(elsie_turns + 1):
        right = elsie_turns - left
        current_sum = max_left_sum[left] + max_right_sum[right]
        max_elsie_share = max(max_elsie_share, current_sum)

    bessie_share = total_cake_size - max_elsie_share
    return [bessie_share, max_elsie_share]

def main():
    number_of_test_cases = int(input())
    for _ in range(number_of_test_cases):
        number_of_cakes = int(input())
        cake_sizes = list(map(int, input().split()))
        result = calculate_cake_distribution(cake_sizes)
        print(f"{result[0]} {result[1]}")

if __name__ == "__main__":
    main()
