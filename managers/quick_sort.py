from random import shuffle

from managers.utils import swap


class QuickSort:
    comparison_counter = 0
    swap_counter = 0
    
    def partition(self, given_list, start, end):
        left_border = start
        iterated_item = start
        right_border = end
        while iterated_item <= right_border:
            
            if given_list[iterated_item] < given_list[left_border]:
                self.comparison_counter += 1
                self.swap_counter += 1
                swap(given_list, iterated_item, left_border)
                left_border += 1
                iterated_item += 1
            
            elif given_list[iterated_item] > given_list[left_border]:
                self.comparison_counter += 2
                self.swap_counter += 1
                swap(given_list, iterated_item, right_border)
                right_border -= 1
            
            else:
                self.comparison_counter += 2
                iterated_item += 1
        
        return left_border, right_border
    
    def sort_util(self, given_list, start, end):
        if start >= end:
            return
        left_border, right_border = self.partition(given_list, start, end)
        self.sort_util(given_list, start, left_border - 1)
        self.sort_util(given_list, right_border + 1, end)
    
    def sort(self, given_list):
        shuffle(given_list)
        self.sort_util(given_list, 0, len(given_list) - 1)
        print(f'№ of compares = {self.comparison_counter}\n№ of swaps = {self.swap_counter}')
