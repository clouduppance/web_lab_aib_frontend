def calculate_median_sum(N, numbers):
    result_sum = 0
    sorted_numbers = []

    for i in range(1, N + 1):
        sorted_numbers.append(numbers[i - 1])
        sorted_numbers.sort()

        length = len(sorted_numbers)
        median_index = length // 2

        if length % 2 == 1:
            result_sum += sorted_numbers[median_index]
        else:
            result_sum += (sorted_numbers[median_index - 1] + sorted_numbers[median_index]) / 2

    return result_sum


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))

    result = calculate_median_sum(N, numbers)
    print(result)
 