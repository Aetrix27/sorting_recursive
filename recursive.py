#!python


from re import I


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(1) average, since it traverses through both at the same time
    Memory usage: O(1), no extra memory being used """
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
        
   
print(merge([1,2,6],[2,4,3]))

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n * logn) for every case, since it always divides the array and compares each time.
    Memory usage: O(n) in all cases since it must copy the data when sorting."""
    #Check if list is so small it's already sorted (base case)
    if len(items) == 1:
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

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
