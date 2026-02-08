def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    print("count: " , count)

    while len(arr) > 0:
        num = arr.pop(0)
        print("num: " , num)
        count[num] += 1
        print("count[num]: " , count[num])

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            print("arr: " , arr)
            count[i] -= 1
            print("count[i]: ", count[i])

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)
