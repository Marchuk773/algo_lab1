import csv
import random

if __name__ == '__main__':
    with open('values.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['manufacturer', 'fat_percentage', 'volume_in_milliliters', 'calories_in_100_grams'])
        for i in range(3000):
            csv_writer.writerow(
                [random.randint(0, 2000), random.randint(0, 2000), random.randint(0, 2000), random.randint(0, 2000)])
