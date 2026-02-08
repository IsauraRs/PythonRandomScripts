myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        print("poppedValWhile: ",val)
        radixIndex = (val // exp) % 10
        print("radixIndex" , radixIndex)
        radixArray[radixIndex].append(val)
        print("radixArray: " , radixArray)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            print("poppedValueForBucket: " , val)
            myArray.append(val)
            print("myArray: " , myArray)

    exp *= 10

print("Sorted array:", myArray)