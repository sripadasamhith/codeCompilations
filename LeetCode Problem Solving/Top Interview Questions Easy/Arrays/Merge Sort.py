import math

def mergeSort(array: []):

    if len(array) > 1:
        # get midpoint of array by floored value of half length
        arrayMidpoint = len(array) // 2
        # store and pass left and right sides of midpoints recursively
        arrayLeftHalf = array[:arrayMidpoint]
        arrayRightHalf = array[arrayMidpoint:]
        mergeSort(arrayLeftHalf)
        mergeSort(arrayRightHalf)

        # declare initializers
        i = j = x = 0
        # check to see if left or right sides are greater and sort in ascending order
        while i < len(arrayLeftHalf) and j < len(arrayRightHalf):
            if arrayLeftHalf[i] <= arrayRightHalf[j]:
                array[x] = arrayLeftHalf[i]
                i += 1

            else:
                array[x] = arrayRightHalf[j]
                j += 1

            x += 1

        # check to see if all elements were left out in left half (applicable for odd sized arrays)
        while i < len(arrayRightHalf):
            array[x] = arrayLeftHalf[i]
            i += 1
            x += 1
        # check to see if all elements were left out in right half (applicable for odd sized arrays)
        while j < len(arrayRightHalf):
            array[x] = arrayRightHalf[j]
            j += 1
            x += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [12,3,7,9,14,6,11,2]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is ")
    printList(arr)