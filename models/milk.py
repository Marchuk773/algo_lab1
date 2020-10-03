class MilkPacket:
    def __init__(self, manufacturer, fat_percentage, volume_in_milliliters, calories_in_100_grams):
        self.manufacturer = manufacturer
        self.fat_percentage = fat_percentage
        self. volume_in_milliliters = volume_in_milliliters
        self.calories_in_100_grams = calories_in_100_grams
    
    def __str__(self):
        return f'Manufacturer is {self.manufacturer}, {self.fat_percentage}% fat, {self.volume_in_milliliters} ' \
               f'milliliters, {self.calories_in_100_grams} calories in 100 grams of milk'
