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



#  --------------------------------------------------  FUNCTIONS --------------------------------------------------  

# Function define to display all menus and lists index form
def display(menu):
    for index, options in enumerate(menu):
        print(f"{index} {options}")

# Input Functions 
def select_courier():               
    return int(input("Select courier number\t"))

def select_order():
    return int(input("Select order number\t"))

def select_staus():
    return int(input("Select a Status\t"))


# Function to read(r) each txt file i have  
def read_txt(filename):
    with open(filename +'_list.txt','r') as file:
        readfile = file.readlines()
        for index,option in enumerate(readfile):
            print(f"{index} {option.strip()}")
        



# Function to amend and read(a+) each txt file i have  
def amend_txt(txtname,input_title):
    with open(txtname +'_list.txt','a+') as file:
        file.writelines(input_title)
        file.seek(0)
        readfile = file.readlines()
        for index,option in enumerate(readfile):
            print(f"{index} {option.strip()}")


# Function to print out txt lists.
def display_txt(menu):
    for index, options in enumerate(menu):
        print(f"{index} {options.strip()}")

 







# --------------------------------------------------  MAIN MENU --------------------------------------------------  

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





# --------------------------------------------------  PRODUCT MENU --------------------------------------------------  

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
        read_txt('drinks')

#display food list
    elif selected_product_menu == 2 :
       read_txt('food')


    elif selected_product_menu == 3 :
        read_txt('drinks')
        add_new_drink = input("Add a new drink item \t") #different ways of adding an input, either defien the input seperately in a vaiable and then add it to your append function or like with food below 
        amend_txt('drinks', add_new_drink)
        


    elif selected_product_menu == 4 :
        read_txt('food')
        add_new_food = input("Add a new food item \t") #differnet ways of adding an input, either difine the input within the append funtion or  fo like above with adding a new drink
        amend_txt('food',(add_new_food))


# replacing product through selecting index in updatefile = new drink name ; and then writing out(w) the updated 'update_file'  to update it (writing updated contect back to the file)
    elif selected_product_menu == 5 :
        read_txt('drinks')

        old_update_drink = int(input("Add number of drink to remove  \t"))
        new_update_drink = input("Please update with new name\t")

        with open('drinks_list.txt','r+') as file:
            update_file = file.readlines()

            file.seek(0)
            update_file[old_update_drink] = new_update_drink + '\n'

            file.writelines(update_file)
            display_txt(update_file)


# Same as above comment but for food list.
    elif selected_product_menu == 6 :
        read_txt('food')
       
        old_update_food = int(input("Add number of food to remove  \t"))
        new_update_food = input("Please update with new name\t")

        with open('food_list.txt','r+') as file:
            update_file = file.readlines()

            file.seek(0)            #if i do not use. file pointer will stay at the end of the file after reading itwhen you try to write back to the file using file.writelines(update_file), Python will append the updated content at the end of the file rather than overwriting the original content
            update_file[old_update_food] = new_update_food + '\n' #\n adds to a new line

            file.writelines(update_file)
            display_txt(update_file)


#  Deleting a drink - read txt file & print usinf display func...Input drink index...Del index selected from txt...update and read txt with overiding(w+) it with new file minus del
    elif selected_product_menu == 7 :
        with open('drinks_list.txt', 'r+') as file:
            readfile = file.readlines()
            display_txt(readfile)
        
            selected_del_drink = int(input("Select item to delete\t"))

            del readfile[selected_del_drink]

            file.seek(0)
            file.writelines(readfile)
            display_txt(readfile)
            

#same as above for food list now

    elif selected_product_menu == 8:
        with open('food_list.txt', 'r+') as file:
            readfile = file.readlines()
            display_txt(readfile)
        
            selected_del_drink = int(input("Select item to delete\t"))

            del readfile[selected_del_drink]

            file.seek(0)
            file.writelines(readfile)

            display_txt(readfile)
   
# in product menu section, if they select soemthign not in list they will get below print message.
    else :
        print ("the option you entered doesn't exist, please choose from the available options")







# --------------------------------------------------  ORDER MENU --------------------------------------------------  

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
        
          
                            
    




