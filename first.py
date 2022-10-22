import csv
import heapq

def get_data(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(int(row[1]))

    return data

def get_top_k(arr, k):
    heap = []
    for i in arr:
        if len(heap) < k:
            heapq.heappush(heap, i)
        else:
            first = heapq.heappop(heap)
            if i > first:
                heapq.heappush(heap, i)
            else:
                heapq.heappush(heap, first)

    return heap

def main():
    filename = 'orders.csv'
    data = get_data(filename)
    top_3 = get_top_k(data, 3)
    print(top_3)

main()