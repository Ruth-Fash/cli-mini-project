main_menu = ['Exit app','Products','Orders','Courier']

product_menu = ['Main menu',
            'Drinks',
            'Food',
            'Add New Drink',
            'Add New Food',
            'Update Exisiting Drink',
            'Update Exisiting Food', 
            'Remove Drink', 
            'Remove Food']



order_menu = ['Return to Main Memu', 
            'Print Orders Dictionary', 
            'Create New Order', 
            'Update Existing Order Status', 
            'Update Order Status', 
            'Delete Order']



courier_menu = ['Return to Main Menu','Courier','Add New Courier','Update Exisiting Courier','Delete Courier']




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

order_dictionary =[{'Customer name' : 'Jessica Smith','Customer address':'120 Chancery Lane, London', 
                 'Customer phone':'079054456543','Status': 'Preparing'},
        {'Customer name' : 'Ruth Fash','Customer address':'66 Bennets, London', 
               'Customer phone':'079054896541', 'Status': 'Order Confirmed'}]

order_status = ['Order Pending','Order Confirmed','Preparing','Out for Delivery', 'Delivered']


courier_list = ["Deliveroo", "Uber Eats", "Just Eat"]












#FUNCTIONS#
#function define to display all menus and lists
def display(menu):
    for index, options in enumerate(menu):
        print(f"{index} {options}")


def select_courier():               
    return int(input("Select courier number\t"))

def select_order():
    return int(input("Select order number\t"))

def select_staus():
    return int(input("Select a Status\t"))


# function to read each txt file i have  
def print_txt(filename):
    with open(filename +'_list.txt','r') as file:
        readfile = file.read()
        print(readfile) 


# function to amend and read  each txt file i have  
def amend_txt(filename,input_title):
    with open(filename +'_list.txt','a+') as file:
        file.write(input_title + "\n")
        file.seek(0)
        readfile = file.read()
        print(readfile)


        






#MAIN MENU ---------------------------------------------------------------------------

# main menu input - select option from main menu
display(main_menu)
main_menu_answer = int(input("Select an option: \t"))

# if they select 0 = exit which print goodbye; 1 = product menu
if main_menu_answer == 0 :
    with open ('food_list.txt',"w") as foodfile:
        for food in food_list:
            foodfile.write(food + "\n")
    
    with open ('drinks_list.txt',"w") as drinkfile:
        for drink in drinks_list:
            drinkfile.write(drink + "\n")

    with open('courier_list.txt','w') as courierfile:
        for courier in courier_list:
            courierfile.write(courier + "\n")

    print ('"Data saved. Exiting app...')
    exit()
    print("This will not print if the user exits.") # test to see if exit works 





#PRODUCT MENU ---------------------------------------------------------------------------

# if they select product menu(1) from the main menu, it will print options in product menu
elif main_menu_answer == 1 :
    for index, i in enumerate(product_menu):
        print(f"{index} {i}")
        
    selected_product_menu = int(input("Select an option: \t"))
    

# within product menu if they select options certain responses.     
    if selected_product_menu == 0 :
        display(main_menu)
        

#display drinks list
    elif selected_product_menu == 1:
        print_txt('drinks')

#display food list
    elif selected_product_menu == 2 :
       print_txt('food')


    elif selected_product_menu == 3 :
        print_txt('drinks')
        add_new_drink = input("Add a new drink item \t") #different ways of adding an input, either defien the input seperately in a vaiable and then add it to your append function or like with food below 
        amend_txt('food', add_new_drink)
        


    elif selected_product_menu == 4 :
        display(food_list)
        food_list.append(input("Add a new food item \t")) #differnet ways of adding an input, either difine the input within the append funtion or  fo like above with adding a new drink
        display(food_list)


    elif selected_product_menu == 5 :
        display(drinks_list)
        old_update_drink = int(input("Add number of drink to remove  \t"))
        new_update_drink = input("Please update with new name\t")
        del drinks_list[old_update_drink]
        drinks_list.insert(old_update_drink,new_update_drink)
        display(drinks_list)


    elif selected_product_menu == 6 :
        display(food_list)
        old_update_food = int(input("Add number of food to remove  \t"))
        new_update_food = input("Please update with new name\t")
        del drinks_list[old_update_food]
        drinks_list.insert(old_update_food,new_update_food)
        display(food_list)


    elif selected_product_menu == 7 :
        display(drinks_list)
        selected_del_drink = int(input("Select drink to delete\t"))
        del drinks_list[selected_del_drink]
        display(drinks_list)


    elif selected_product_menu == 8 :
        display(food_list)
        selected_del_food = int(input("Select food to delete\t"))
        del food_list[selected_del_food]
        display(food_list)
# in product menu section, if they select soemthign not in list they will get below print message.
    else :
        print ("the option you entered doesn't exist, please choose from the available options")







#ORDER MENU ---------------------------------------------------------------------------
# if they select order menu(2) from the main menu, it will print options in order menu
elif main_menu_answer == 2:
        display(order_menu)

 # then it will ask to select an option from the order menu     ---    if you select 0, it send you back to the main menu 
        order_menu_answer = int(input("Select an option from the order menu \t"))    
        if order_menu_answer == 0:
            display(main_menu)

 # if you select 1 it should print out all the orders ()               
        elif order_menu_answer == 1:
                display(order_dictionary)
        

        elif order_menu_answer == 2:
            new_customer = {'Customer name' : input('Add name\t'),
                             'Customer address':input('Add address\t'), 
                             'Customer phone':input('Add number\t')}
            display(courier_list)
            selected_index = select_courier()
            new_status = {'Status': 'Preparing'}

            order_dictionary.append(new_customer)
            order_dictionary.append(new_status)
            order_dictionary.append(courier_list[selected_index])
            display(order_dictionary)
                

 
        elif order_menu_answer == 3:
            display(order_dictionary)
            selected_order_index = select_order()

            display(order_status)
            selected_status_index = select_staus()

# this is bascally how to updae a dictionary in a list -----   List_name[index value in list]'[dictionary key name'] = new value   
            order_dictionary[selected_order_index]['Status'] = order_status[selected_status_index]
            print(f" Current Orders: {order_dictionary}")
            #for index, orders in enumerate(order_dictionary):
                #if index == order_dictionary_index:
                    #orders['Status'] = input("add new status \t") # is it better for me to define my variable and then add the variable? 

        elif order_menu_answer == 4:
            display(order_dictionary)
            selected_order_index = select_order()
            update_name = input("Add updated name\t")
            if update_name:
                order_dictionary[selected_order_index]['Customer name'] = update_name   
            
            update_address = input("Add updated address\t")
            if update_address:
                order_dictionary[selected_order_index]['Customer address'] = update_address   

            update_number = input("Add updated number\t")
            if update_number:
                order_dictionary[selected_order_index]['Customer phone'] = update_number   
            display(order_dictionary)



        elif order_menu_answer == 5:
            display(order_dictionary)
            selected_index = select_order()
            del order_dictionary[selected_index]
            display(order_dictionary)



#COURIER MENU ---------------------------------------------------------------------------

elif main_menu_answer == 3:
        display(courier_menu)
        courier_menu_answer = int(input("Select an option from the order menu \t"))

        if courier_menu_answer == 0:
            display(main_menu)

        elif courier_menu_answer == 1:
            display(courier_list)

        elif courier_menu_answer == 2:
            add_new_courier = input("Add new courier \t")
            courier_list.append(add_new_courier)
            display(courier_list)

        elif courier_menu_answer == 3:
            display(courier_list)
            courier_index = select_courier()

            updated_courier = input("Input new courier name\t")

            courier_list[courier_index] = updated_courier
            display(courier_list)

        elif courier_menu_answer == 4:
            display(courier_list)
            courier_index = select_courier()

            del courier_list[courier_index]
            display(courier_list)

 # in the main menu section, if they select things other than 0 or 1 or 2, below message will appear.        
else :
   print ("the option you entered doesn't exist, please choose from the available options")
        
          
                            
    




