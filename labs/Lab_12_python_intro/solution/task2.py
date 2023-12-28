import heapq


def find_median(n, sequence):
    max_seq = [] 
    min_seq = []
    result = 0

    for i in range(n):
        heapq.heappush(max_seq, -sequence[i])
        heapq.heappush(min_seq, -heapq.heappop(max_seq))

        if len(min_seq) > len(max_seq):
            heapq.heappush(max_seq, -heapq.heappop(min_seq))
        result -= max_seq[0]

    return result


if __name__ == '__main__':
    n = int(input("Введите n: "))
    sequence = list(map(int, input("Введите последовательность: ").split()))

    print(find_median(n, sequence))