#!python


from re import I


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) average, since it traverses through both at the same time
    Memory usage: O(1), only makes new array """
    # Repeat until one list is empty
    #  Find minimum item in both lists and append it to new list
    # Append remaining items in non-empty list to new list

    merged_list = []
    i = 0
    j = 0
    
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            merged_list.append(items1[i])
            i += 1
        
        else:
            merged_list.append(items2[j])
            j += 1
    
    merged_list += items1[i:] 
    merged_list += items2[j:]
    return merged_list
        
   
print(merge([1,2,4],[3,5,6]))

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n * logn) for every case, since it makes O(n) copies when dividing the array into smaller ones and compares each time.
    Memory usage: O(n) in all cases since it must copy the data when sorting."""
    #Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items
    elif len(items) > 1:
        #Split items list into approximately equal halves
        mid = len(items)//2
        first_part = items[:mid]
        second_part = items[mid:]
        #Sort each half by recursively calling merge sort
        merge_sort(first_part)
        merge_sort(second_part)
        i = 0
        j = 0
        k = 0
  
        while i < len(first_part) and j < len(second_part):
            if first_part[i] < second_part[j]:
                items[k] = first_part[i]
                i += 1
            else:
                items[k] = second_part[j]
                j += 1
            #Moves to next block division
            k += 1

        #Merge sorted halves into one list in sorted order
        while i < len(first_part):
            items[k] = first_part[i]
            i += 1
            k += 1

        while j < len(second_part):
            items[k] = second_part[j]
            j += 1
            k += 1
    return items
  
print(merge_sort([1,7,3,6,2]))

def partition_external(items):
    """
    Time complexity: O(n) all cases because each item that is passed in is compared to the pivot
                    and appended to the new list.
    Space complexity: O(n) since when you partition the input, O(n) space is created for the
                        new lists.
    """
    if len(items) <= 1:
        return "List too small"
    pivot_index = 0
    pivot_value = items[pivot_index]
    smaller_items = []
    larger_items = []
    same = []

    for item in items:
        if item == pivot_value:
            same.append(item)
        elif item < pivot_value:
            smaller_items.append(item)
        elif item > pivot_value:
            larger_items.append(item)
    return smaller_items, same, larger_items

def partition_in_place(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (Choose the first or last element as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) average and worst case, since you have to sort through the 
    low to high range, and O(1) best case, where the low would equal the high.
    Memory usage: O(1), since it is sorted in place. """
    #Choose a pivot any way and document your method in docstring above
    pivot = items[low]
    start = low +1
    partitioning = True
    #Loop through all items in range [low...high]
    #Move items greater than pivot into back of range [p+1...high]
    #Move items less than pivot into front of range [low...p-1]
    while partitioning:
        while start <= high and items[high] >= pivot:
            high -= 1
        
        while start <= high and items[start] <= pivot:
            start += 1
        #Swaps items in order to sort
        if start <= high:
            items[start], items[high] = items[high], items[start]
        else:
            #Found a value of high and low that is out of order or low is now higher than high
            partitioning = False

    #Move pivot item into final position [p] and return index p
    items[low], items[high] = items[high], items[low]

    return high

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: Average and best case is O(n * logn) since the selected pivots help to sort efficiently.
    Worst case running time: Worst case is O(n^2) since we may have to go through both arrays completely to sort them.
    Memory usage: Memory is O(1) for all cases, since it is an in place sort. """
     
    #Check if high and low range bounds have default values (not given)
    if low == None and high == None:
        low = 0
        high = len(items)-1
    #Check if list or range is so small it's already sorted (base case)
  
    if low >= high:
        return 
    #Partition items in-place around a pivot and get index of pivot
    part = partition_in_place(items, low, high)
    #Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, part-1)
    quick_sort(items, part+1, high)


items = [1,4,2,5,6,1,2,5]
quick_sort(items)
print(items)

