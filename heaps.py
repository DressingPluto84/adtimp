def heapsort(k):
    hs = len(k) - 1
    end = len(k) - 1
    while hs > 0:
        max_heapify(k, hs, 1)
        k[1], k[hs] = k[hs], k[1]
        hs -= 1

def max_heapify(k, heapsize, i):
    left = 2*i
    right = 2*i + 1
    if left <= heapsize and k[i] < k[left]:
        largest = left
    else:
        largest = i
    if right <= heapsize and k[largest] < k[right]:
        largest = right
    if largest != i:
        k[i], k[largest] = k[largest], k[i]
        max_heapify(k, len(k[largest:]), largest)

def min_heapify(k: list, heapsize: int, i: int):
    left = 2*i
    right = 2*i + 1
    if left <= heapsize and k[i] > k[left]:
        smallest = left
    else:
        smallest = i
    if right <= heapsize and k[smallest] > k[right]:
        smallest = right
    if smallest != i:
        k[i], k[smallest] = k[smallest], k[i]
        min_heapify(k, len(k[:smallest]), smallest)

def bubble_up(k, i):
    if i // 2  > 0 and k[i] > k[i // 2]:
        k[i], k[i//2] = k[i//2], k[i]
        bubble_up(k, i//2)

def addElem(k, heapsize):
    pass

def uToh(k):
    for i in range((len(k) - 1) // 2, 0, -1):
        max_heapify(k, len(k) - 1, i)

k = [-1, 10, 2, 3, 1, 7, 9, 8, 4]
min_heapify(k, len(k) - 1, 1)
print(k)