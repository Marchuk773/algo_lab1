from managers.utils import swap


class SelectionSort:
    
    def __init__(self):
        self.comparison_counter = 0
        self.swap_counter = 0
    
    def sort(self, given_list, key):
        self.comparison_counter = 0
        self.swap_counter = 0
        for i in range(len(given_list)):
            biggest_element_index = i
            for j in range(i + 1, len(given_list)):
                self.comparison_counter += 1
                if key(given_list[biggest_element_index]) < key(given_list[j]):
                    biggest_element_index = j
            if biggest_element_index != i:
                self.swap_counter += 1
                swap(given_list, i, biggest_element_index)
        
        print(f'Selection sort, '
              f'№ of compares in selection sort = {self.comparison_counter}\n'
              f'№ of swaps in selection sort = {self.swap_counter}')
