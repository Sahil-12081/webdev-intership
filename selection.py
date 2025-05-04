def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the current element
        array[ind], array[min_index] = array[min_index], array[ind]

# Take input from the user
input_str = input("Enter elements of the array separated by spaces: ")
arr = list(map(int, input_str.split()))
size = len(arr)

selectionSort(arr, size)

print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
