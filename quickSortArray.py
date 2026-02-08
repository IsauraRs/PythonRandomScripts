def partition(array, low, high):
    pivot = array[high]
    print(pivot)
    i = low - 1
    print(i)

    for j in range(low, high):
        print(j)
        print(array[j])
        if array[j] <= pivot:
            i += 1
            print(i)
            array[i], array[j] = array[j], array[i]
            print("Array for j: " , array)

    array[i+1], array[high] = array[high], array[i+1]
    print("Array out: " ,array)
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)