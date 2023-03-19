def quick(arr):
    if len(arr) <= 1:
        return arr

    # Choose the pivot element (in this case, the last element)
    pivot = arr[-1]

    # Create two sub-arrays for elements smaller and larger than the pivot
    left = []
    right = []

    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # Recursively sort the left and right sub-arrays
    left_sorted = quick(left)
    right_sorted = quick(right)

    # Combine the sorted sub-arrays and the pivot element into the final sorted array
    return left_sorted + [pivot] + right_sorted
