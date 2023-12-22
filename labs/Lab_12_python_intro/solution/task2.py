def calculate_median_sum(n, numbers):
    medians = []

    for i in range(n):
        sorted_numbers = sorted(numbers[:i+1])

        if (i + 1) % 2 == 1:
            median = sorted_numbers[(i + 1) // 2]
        else:
            median = sorted_numbers[i // 2]

        medians.append(median)

    total_sum = sum(medians)
    return total_sum

if __name__ == '__main__':
    n = int(input())
    X = [int(input()) for _ in range(n)]

    result = calculate_median_sum(n, X)
    print(result)
