# Creating Txt Files

#food list txt file 
food_list = ['Avocado_toast',
            'Eggs',
            'Toast',
            'BLT',
            'Chicken Salad',
            'Grilled Cheese',
            'Tuna melt',
            'Plain croissant',
            'Cinnamon roll',
            'Carrot cake'] 


foodfile = open("food_list.txt","w+")
for food in food_list:
    foodfile.write(food + "\n")
foodfile.seek(0)
print(foodfile.read())
foodfile.close()



drinks_list = ['Espresso', 
            'Americano',  
            'Latte', 
            'Cappuccino', 
            'Macchiato', 
            'Matcha Latte',
            'Hot Chocolate',
            'Chai Latte',
            'Green Tea',
            'Black tea',
            'Still water',
            'Orange juice',]


drinkfile = open("drink_list.txt","w+")
for drink in drinks_list:
    drinkfile.write(drink + "\n")
drinkfile.seek(0)
print(drinkfile.read())
drinkfile.close()















#courier list txt file 

courier_list = ["Deliveroo", "Uber Eats", "Just Eat"]

courierfile = open("courier_list.txt","w+")
for courier in courier_list:
    courierfile.write(courier +"\n")
courierfile.seek(0)
print(courierfile.read())
courierfile.close()



