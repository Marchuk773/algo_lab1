from random import shuffle

from managers.utils import swap


class QuickSort:
    
    def __init__(self):
        self.comparison_counter = 0
        self.swap_counter = 0
    
    def sort(self, given_list, key=lambda obj: obj):
        self.comparison_counter = 0
        self.swap_counter = 0
        shuffle(given_list)
        self.sort_util(given_list, 0, len(given_list) - 1, key)
    
    def sort_util(self, given_list, start, end, key):
        if end - start < 9:
            self.insertion_sort(given_list, start, end, key)
            return
        pivot = self.partition(given_list, start, end, key)
        self.sort_util(given_list, start, pivot - 1, key)
        self.sort_util(given_list, pivot + 1, end, key)
    
    def partition(self, given_list, start, end, key):
        pivot = key(given_list[start])
        left_border = start
        right_border = end
        while True:
            
            while key(given_list[left_border]) <= pivot and left_border != end:
                self.comparison_counter += 2
                left_border += 1
            
            while key(given_list[right_border]) >= pivot and right_border != start:
                self.comparison_counter += 2
                right_border -= 1
            
            self.comparison_counter += 1
            if right_border <= left_border:
                break
            
            swap(given_list, left_border, right_border)
            self.swap_counter += 1
        
        swap(given_list, right_border, start)
        self.swap_counter += 1
        return right_border
    
    def insertion_sort(self, given_list, start, end, key=lambda obj: obj):
        for i in range(start, end + 1):
            index = i
            while index > 0 and key(given_list[index - 1]) > key(given_list[index]):
                self.comparison_counter += 2
                self.swap_counter += 1
                swap(given_list, index - 1, index)
                index -= 1
    
    def print_info(self):
        print('\nQuick sort:\n'
              f'№ of compares in quick sort = {self.comparison_counter}\n'
              f'№ of swaps in quick sort = {self.swap_counter}')
