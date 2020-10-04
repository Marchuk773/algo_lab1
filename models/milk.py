class MilkPacket:
    def __init__(self, manufacturer, fat_percentage, volume_in_milliliters, calories_in_100_grams):
        self.manufacturer = manufacturer
        self.fat_percentage = fat_percentage
        self. volume_in_milliliters = volume_in_milliliters
        self.calories_in_100_grams = calories_in_100_grams
    
    def __repr__(self):
        return f'Manufacturer:{self.manufacturer}, fat:{self.fat_percentage}%, milliliters:' \
               f'{self.volume_in_milliliters}, calories:{self.calories_in_100_grams}'
