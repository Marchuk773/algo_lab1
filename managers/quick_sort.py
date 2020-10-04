from random import shuffle

from managers.utils import swap


class QuickSort:
    
    def __init__(self):
        self.comparison_counter = 0
        self.swap_counter = 0
    
    def sort(self, given_list, key):
        self.comparison_counter = 0
        self.swap_counter = 0
        shuffle(given_list)
        self.sort_util(given_list, 0, len(given_list) - 1, key)
        print(f'Quick sort, '
              f'№ of compares in quick sort = {self.comparison_counter}\n'
              f'№ of swaps in quick sort = {self.swap_counter}')
    
    def sort_util(self, given_list, start, end, key):
        if start >= end:
            return
        left_border, right_border = self.partition(given_list, start, end, key)
        self.sort_util(given_list, start, left_border - 1, key)
        self.sort_util(given_list, right_border + 1, end, key)
    
    def partition(self, given_list, start, end, key):
        left_border = start
        iterated_item = start
        right_border = end
        while iterated_item <= right_border:
            
            if key(given_list[iterated_item]) < key(given_list[left_border]):
                self.comparison_counter += 1
                self.swap_counter += 1
                swap(given_list, iterated_item, left_border)
                left_border += 1
                iterated_item += 1
            
            elif key(given_list[iterated_item]) > key(given_list[left_border]):
                self.comparison_counter += 2
                self.swap_counter += 1
                swap(given_list, iterated_item, right_border)
                right_border -= 1
            
            else:
                self.comparison_counter += 2
                iterated_item += 1
        
        return left_border, right_border
