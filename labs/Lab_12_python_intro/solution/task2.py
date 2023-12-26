import heapq

def MedianSearch(n, arr):
    max_el = [], min_el = [], result = 0
    for i in range(n):
        heapq.heappush(max_el, -arr[i])  
        heapq.heappush(min_el, -heapq.heappop(max_el))
        
        if len(min_el) > len(max_el):
            heapq.heappush(max_el, -heapq.heappop(min_el))  
        result -= max_el[0]  

    return result


if __name__ == '__main__':
    n, arr = int(input()), list(map(int, input().split()))
    print(MedianSearch(n, arr))