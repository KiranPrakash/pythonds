def bubble_sort(array):
    for passnum in range(len(array)-1, 0, -1):
       #print(passnum)
       for i in range(passnum):
           print(i,passnum)
           if array[i] > array[i+1]:
               array[i], array[i+1] = array[i+1], array[i]


def selection_sort(array):
    for fillslot in range(len(alist)-1,0,-1):
        max_pos = 0
        for locat in range(1, fillslot+1):
            if array[locat] > array[max_pos]:
                max_pos = locat

        array[fillslot], array[max_pos] = array[max_pos], array[fillslot]


def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position>0 and array[position -1] > current_value:
             array[position] = array[position-1]
             position -= 1
        array[position] = current_value

def shell_sort(array):
    gap = len(array)//2

    while gap > 0:
        for index in range(gap, len(array)):
            current_value = array[index]
            position = index

            while position >= gap and array[position-gap]> current_value:
                array[position] = array[position-gap]
                position -= gap

            array[position] = current_value

        gap //= 2

def merge_sort(array):
    # if the list is empty or has one item then it is sorted( that is the base case
    if len(array)> 1:
        mid = len(array)//2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1

            else:
                array[k] = right_half[j]
                j += 1
            k +=1

        while i < len(left_half):
            array[k] = left_half[i]
            i +=1
            k +=1

        while j < len(right_half):
            array[k] = right_half[j]
            j +=1
            k +=1


def quick_sort(array):
    quick_sort_helper(array, 0, len(alist)-1)


def quick_sort_helper(array, low, high):
    """ Reason why quick sort is better than merge sort, Merge sort is not an in place sorting, which means that
    it takes extra space for sorting so the space complexity is O(n), where as quick sort we could do it in constant time
    and both are O(nlogn) time complexity in average case where as worst case Quick sort is O(n**2)

    We implement quick sort in two steps, the first step, first method that finds the pivot such that all the array elements
    to the left of pivot is smaller than the pivot value and right is larger than the pivot value.

    The second step is to do split the original array into sub array in place recursively and find the pivot for each of them
    The base index is where there is only one element in the array and it is sorted"""
    if low < high:
        p_index = partition(array, low, high)

        quick_sort_helper(array, low, p_index-1)
        quick_sort_helper(array, p_index+1, high)


def partition(array, low, high):
    p_index = low
    pivot = array[high]

    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index +=1

    array[p_index], array[high] = array[high], array[p_index]

    return p_index


alist = [54,26,93,17,77,31,44,55,20]
alist1 = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
quick_sort(alist)
print(alist)




