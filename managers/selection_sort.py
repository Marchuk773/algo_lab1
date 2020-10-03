from managers.utils import swap


class SelectionSort:
    comparison_counter = 0
    swap_counter = 0
    
    def sort(self, given_list):
        for i in range(len(given_list)):
            biggest_element_index = i
            for j in range(i + 1, len(given_list)):
                self.comparison_counter += 1
                if given_list[biggest_element_index] < given_list[j]:
                    biggest_element_index = j
            if biggest_element_index != i:
                self.swap_counter += 1
                swap(given_list, i, biggest_element_index)
        
        print(f'№ of compares = {self.comparison_counter}\n№ of swaps = {self.swap_counter}')
