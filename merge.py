def merge(arr1, arr2):
    # create two vars to traverse both list at the same time and one final sorted list
    index1 = 0
    index2 = 0
    mergedList = []
    # use while loop to traverse the both lists at the same time
    while (index1 < len(arr1) and index2 < len(arr2)):
        if (arr1[index1] <= arr2[index2]):
            mergedList.append(arr1[index1])
            index1 += 1
        else:
            mergedList.append(arr2[index2])
            index2 += 1
    if (index1 < len(arr1)):
        while (index1 < len(arr1)):
            mergedList.append(arr1[index1])
            index1 += 1
    elif (index2 < len(arr2)):
        while (index2 < len(arr2)):
            mergedList.append(arr2[index2])
            index2 += 1
    return mergedList

