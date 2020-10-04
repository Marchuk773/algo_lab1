import time
import csv

from managers import selection_sort, quick_sort
from models import milk

if __name__ == '__main__':
    milk_packet_list = []
    with open('values.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        for line in csv_reader:
            milk_packet_list.append(milk.MilkPacket(manufacturer=line[0], fat_percentage=line[1],
                                                    volume_in_milliliters=line[2], calories_in_100_grams=line[3]))
    
    quick = quick_sort.QuickSort()
    selection = selection_sort.SelectionSort()
    
    selection_start_time = time.time()
    selection.sort(milk_packet_list, key=lambda milk_packet: milk_packet.fat_percentage)
    selection_end_time = time.time()
    print(f'List after select sort: {milk_packet_list}')
    print(f'--- {selection_end_time - selection_start_time} seconds for selection sort ---')
    
    quicksort_start_time = time.time()
    quick.sort(milk_packet_list, key=lambda milk_packet: milk_packet.calories_in_100_grams)
    quicksort_end_time = time.time()
    print(f'List after quick sort: {milk_packet_list}')
    print(f'--- {quicksort_end_time - quicksort_start_time} seconds for quick sort ---')
