from restaurant import Restaurant, IceCreamStand

johns = IceCreamStand("John's", "Ice Cream", "Chocolate")
johns.describe_flavours

harvester = Restaurant('Harvester', 'general')
harvester.describe_restaurant()
harvester.increment_number_served(3)
print(f"{harvester.number_served}")

