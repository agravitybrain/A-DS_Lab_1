"""
main.py
module for experiments
"""
import time
import random
import copy


def selection_sort(list_sort: list) -> (list):
    """
    Implements a selection sorting algorithm
    Return sorted list
    >>> selection_sort([4,5,3,2,1,0])
    [0, 1, 2, 3, 4, 5]
    """
    global selection_c

    for i in range(len(list_sort)):
    
        min_index = i

        for j in range(i+1, len(list_sort)):
            selection_c += 1
            if list_sort[min_index] > list_sort[j]:
                min_index= j

        list_sort[i], list_sort[min_index] = list_sort[min_index], list_sort[i]

    return list_sort


def insertion_sort(array: list):
    """
    insertion sort 

    """
    for index in range(1, len(array)):
        currentValue = array.pop(index)
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            # array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1

        array.insert(currentPosition, currentValue)


def merge_sort(sorting_list: list) -> (list):
    '''
    Implements a merge sorting algorithm
    Return sorted list
    >>> merge_sort([4,5,3,2,1,0])
    [0, 1, 2, 3, 4, 5]
    '''
    global merge_c
    if len(sorting_list) > 1:

        midle = len(sorting_list) // 2
        first_part = sorting_list[:midle]
        second_part = sorting_list[midle:]

        merge_sort(first_part)
        merge_sort(second_part)

        i = j = k = 0

        while i < len(first_part) and j < len(second_part):
            if first_part[i] < second_part[j]:
                sorting_list[k] = (first_part[i])
                i += 1
                k += 1
            else:
                sorting_list[k] = (second_part[j])
                j += 1
                k += 1 
            merge_c += 1


        while i < len(first_part):
            sorting_list[k] = (first_part[i])
            i += 1
            k += 1


        while j < len(second_part):
            sorting_list[k] = second_part[j]
            j += 1
            k += 1

    return sorting_list


def shell_sort(array, n):
    """
    shellsort algorithm
    sort array with n elements which compare elements
    with interval n/2, n/4, ....
    """
    interval = n // 2
    m = 0
    global shell_c
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
                shell_c += 1

            array[j] = temp
        interval //= 2


def main():
    """
    experiment function
    """

    file_1 =  open('data_t.txt', 'w')
    file_2 = open('data_c.txt', 'w')
     
    for k in range(7, 16):
        insert_exp = [0, 0, 0, 0]
        select_exp = [0, 0, 0, 0]
        merge_exp = [0, 0, 0, 0]
        shell_exp = [0, 0, 0, 0]

        insert_com = [0, 0, 0, 0]
        select_com = [0, 0, 0, 0]
        merge_com = [0, 0, 0, 0]
        shell_com = [0, 0, 0, 0]

        
        for _ in range(5):
            array = []
            array_4 = []
            for _ in range(2**k):
                array.append(random.randint(0, 1000000))
                array_4.append(random.randint(1, 3))
            
            select_l = copy.deepcopy(array)
            select_l_4 = copy.deepcopy(array_4)
            insert_l = copy.deepcopy(array)
            insert_l_4 = copy.deepcopy(array_4)
            merge_l = copy.deepcopy(array)
            merge_l_4 = copy.deepcopy(array_4)
            shell_l = copy.deepcopy(array)
            shell_l_4 = copy.deepcopy(array_4)
            
            # insertion sort
            # 1 variant - random list
            time_0 = time.time()
            insertion_sort(insert_l)
            time_1 = time.time()
            insert_com[0] += insertion_c
            insertion_c = 0
            insert_exp[0] += time_1 - time_0
            # 2 variant - sorted from smaller to bigger
            time_0 = time.time()
            insertion_sort(insert_l)
            time_1 = time.time()
            insert_com[1] += insertion_c
            insertion_c = 0
            insert_exp[1] += time_1 - time_0
            # 3 variant - sorted from bigger to smaller
            insert_l.reverse()
            time_0 = time.time()
            insertion_sort(insert_l)
            time_1 = time.time()
            insert_com[2] += insertion_c
            insertion_c = 0
            insert_exp[2] += time_1 - time_0
            # 4 variant - list includes only {1, 2, 3}
            time_0 = time.time()
            insertion_sort(insert_l_4)
            time_1 = time.time()
            insert_com[3] += insertion_c
            insertion_c = 0
            insert_exp[3] += time_1 - time_0
            
            # selection sort
            # 1 variant - random list
            time_0 = time.time()
            selection_sort(select_l)
            time_1 = time.time()
            select_com[0] += selection_c
            selection_c = 0
            select_exp[0] += time_1 - time_0
            # 2 variant - sorted from smaller to bigger
            time_0 = time.time()
            selection_sort(select_l)
            time_1 = time.time()
            select_com[1] += selection_c
            selection_c = 0
            select_exp[1] += time_1 - time_0
            # 3 variant - sorted from bigger to smaller
            select_l.reverse()
            time_0 = time.time()
            selection_sort(select_l)
            time_1 = time.time()
            select_com[2] += selection_c
            selection_c = 0
            select_exp[2] += time_1 - time_0
            # 4 variant - list includes only {1, 2, 3}
            time_0 = time.time()
            selection_sort(select_l_4)
            time_1 = time.time()
            select_com[3] += selection_c
            selection_c = 0
            select_exp[3] += time_1 - time_0

            # merge sort
            # 1 variant - random list
            time_0 = time.time()
            merge_sort(merge_l)
            time_1 = time.time()
            merge_com[0] += merge_c
            merge_c = 0
            merge_exp[0] += time_1 - time_0
            # 2 variant - sorted from smaller to bigger
            time_0 = time.time()
            merge_sort(merge_l)
            time_1 = time.time()
            merge_com[1] += merge_c
            merge_c = 0
            merge_exp[1] += time_1 - time_0
            # 3 variant - sorted from bigger to smaller
            merge_l.reverse()
            time_0 = time.time()
            merge_sort(merge_l)
            time_1 = time.time()
            merge_com[2] += merge_c
            merge_c = 0
            merge_exp[2] += time_1 - time_0
            # 4 variant - list includes only {1, 2, 3}
            time_0 = time.time()
            merge_sort(merge_l_4)
            time_1 = time.time()
            merge_com[3] += merge_c
            merge_c = 0
            merge_exp[3] += time_1 - time_0

            # shell sort
            # 1 variant - random list
            time_0 = time.time()
            shell_sort(shell_l, len(shell_l))
            time_1 = time.time()
            shell_com[0] += shell_c
            shell_c = 0
            shell_exp[0] += time_1 - time_0
            # 2 variant - sorted from smaller to bigger
            time_0 = time.time()
            shell_sort(shell_l, len(shell_l))
            time_1 = time.time()
            shell_com[1] += shell_c
            shell_c = 0
            shell_exp[1] += time_1 - time_0
            # 3 variant - sorted from bigger to smaller
            shell_l.reverse()
            time_0 = time.time()
            shell_sort(shell_l, len(shell_l))
            time_1 = time.time()
            shell_com[2] += shell_c
            shell_c = 0
            shell_exp[2] += time_1 - time_0
            # 4 variant - list includes only {1, 2, 3}
            time_0 = time.time()
            shell_sort(shell_l_4, len(select_l_4))
            time_1 = time.time()
            shell_com[3] += shell_c
            shell_exp[3] += time_1 - time_0

        for i in range(4):
            insert_exp[i] = insert_exp[i]/5
            select_exp[i] = select_exp[i]/5
            merge_exp[i] = merge_exp[i]/5
            shell_exp[i] = shell_exp[i]/5

            insert_exp[i] = insert_exp[i] // 5
            select_exp[i] = select_exp[i] // 5
            merge_exp[i] = merge_exp[i] // 5
            shell_exp[i] = shell_exp[i] // 5
    
    file_1.write(f'2^{k}\nselection result: {select_exp}\ninsertion result: {insert_exp}\nmerge result: {merge_exp}\nshell result: {shell_exp}')
    file_2.write(f'selection {select_com}\ninsert {insert_com}\nmerge {merge_com}\nshell {shell_com}')

if __name__=="__main__":
    selection_c = 0
    insertion_c = 0
    merge_c = 0
    shell_c = 0
    main()