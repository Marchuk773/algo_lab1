from random import randint

from managers import selection_sort, quick_sort

if __name__ == '__main__':
    list = []
    for i in range (3000):
        list.append(randint(0, 150))
    new_list = list
    quick = quick_sort.QuickSort()
    quick.sort(new_list)
    print(new_list)
    selection = selection_sort.SelectionSort()
    selection.sort(new_list)
    print(new_list)
