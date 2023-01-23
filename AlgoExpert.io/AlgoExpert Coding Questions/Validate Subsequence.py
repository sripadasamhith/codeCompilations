def isValidSubsequence(array, sequence):

    # create a new array
    newArray = []

    # check if array already equals sequence, 
    #       if sequence is one element and in array, 
    #       if all the elements in sequence and array are the same and members of each list
    if array == sequence or len(sequence) == 1 and sequence[0] in array or len(sequence) == sequence.count(sequence[0]) and len(array) == array.count(array[0]):
        
        return True

    else:

        # index array and find numbers in both array and sequence
        for nums in array:

            # append the number to newArray if in both lists
            if  nums in sequence:
                newArray.append(nums)
        
        # print("Array: " + str(newArray) + "\nSequence: " + str(sequence))

    # return true if both the arrays are exactly the same (contain same elements in same order)
    if sequence == newArray:
        return True
        
    else:
        return False