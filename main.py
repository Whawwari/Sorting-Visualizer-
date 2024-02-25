import matplotlib.pyplot as plt
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_plot(arr, title=f'Bubble Sort - Step {i*n+j}')

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            update_plot(arr, title=f'Insertion Sort - Step {i*len(arr)+j}')
        arr[j+1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_plot(arr, title=f'Selection Sort - Step {i}')

def merge_sort(arr, l, r):
    if l < r:
        m = (l+r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [arr[l+i] for i in range(n1)]
    R = [arr[m+1+j] for j in range(n2)]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    update_plot(arr, title='Merge Sort')

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    update_plot(arr, title='Quick Sort')
    return i+1

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    update_plot(arr, title='Heap Sort')

def update_plot(arr, title):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(title)
    plt.pause(0.05)

def generate_array(size, max_value=100):
    return [random.randint(1, max_value) for _ in range(size)]

def main():
    try:
        num_elements = int(input("Enter the number of elements in the array: "))
        print("Choose a sorting method:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    array = generate_array(num_elements)
    plt.figure()

    if choice == 1:
        bubble_sort(array)
    elif choice == 2:
        insertion_sort(array)
    elif choice == 3:
        selection_sort(array)
    elif choice == 4:
        merge_sort(array, 0, len(array) - 1)
    elif choice == 5:
        quick_sort(array, 0, len(array) - 1)
    elif choice == 6:
        heap_sort(array)
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
        return

    plt.show()

if __name__ == '__main__':
    main()
