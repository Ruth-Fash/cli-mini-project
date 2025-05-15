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


#FUNCTIONS#
#function define to get lists for all menus and lists
def listing(menu):
    for index, options in enumerate(menu):
        print(f"{index} {options}")


                
    


#def customer_stuff(customer):
 #   customer_name = input("add new name \t")
  #  new_customer_info = {(customer): customer_name}
   # order_dictionary.append(customer_name)


    





#instead of always typeong out my code like the for index stuff, can i maybe put it in a function?



# main menu input - select option from main menu
listing(main_menu)
main_menu_answer = int(input("Select an option: \t"))

# if they select 0 = exit which print goodbye; 1 = product menu
if main_menu_answer == 0 :
 print ('Goodbye!')

# if they select product menu(1) from the main menu, it will print options in product menu
elif main_menu_answer == 1 :
    for index, i in enumerate(product_menu):
        print(f"{index} {i}")
    product_menu_answer = int(input("Select an option: \t"))
    

# within product menu if they select options certain responses.     
    if product_menu_answer == 0 :
        listing(main_menu)

    elif product_menu_answer == 1:
        listing(drinks_list)


    elif product_menu_answer == 2 :
       listing(food_list)


    elif product_menu_answer == 3 :
        listing(drinks_list)
        add_new_drink = input("Add a new drink item \t") #different ways of adding an input, either defien the input seperately in a vaiable and then add it to your append function or like with food below 
        drinks_list.append(add_new_drink)
        listing(drinks_list)


    elif product_menu_answer == 4 :
        listing(food_list)
        food_list.append(input("Add a new food item \t")) #differnet ways of adding an input, either difine the input within the append funtion or  fo like above with adding a new drink
        listing(food_list)


    elif product_menu_answer == 5 :
        listing(drinks_list)
        drinks_list.remove(input("add name of drink to remove  \t"))
        drinks_list.append(input("add new name to replace \t")) # should i user insert, so that i can replace with new updated item in the spefic place i removed the last one?
        listing(drinks_list)


    elif product_menu_answer == 6 :
        listing(food_list)
        food_list.remove(input("add name of food to remove \t"))
        food_list.append(input("add new name to replace \t"))
        listing(food_list)


    elif product_menu_answer == 7 :
        listing(drinks_list)
        drinks_list.remove(input("add name of drink to remove \t"))
        listing(drinks_list)


    elif product_menu_answer == 8 :
        listing(food_list)
        food_list.remove(input("add name of drink to remove \t"))
        listing(food_list)
# in product menu section, if they select soemthign not in list they will get below print message.
    else :
        print ("the option you entered doesn't exist, please choose from the available options")


# if they select order menu(2) from the main menu, it will print options in order menu
elif main_menu_answer == 2:
        listing(order_menu)

 # then it will ask to select an option from the order menu     ---    if you select 0, it send you back to the main menu 
        order_menu_answer = int(input("Select an option from the order menu \t"))    
        if order_menu_answer == 0:
            listing(main_menu)

 # if you select 1 it should preint out all the orders ()               
        elif order_menu_answer == 1:
                print(order_dictionary)
        

        elif order_menu_answer == 2:
                print(order_dictionary)
                new_customer = {'Customer name' : input('Add name\t'),
                             'Customer address':input('Add address\t'), 
                             'Customer phone':input('Add number\t')}
                new_status = {'Status': 'Preparing'}

                order_dictionary.append(new_customer,new_status)
                print(order_dictionary)
                '''stuck here, hwo do i add a new name to a dictionary tha's within a list. 
                i've managed to add it to the list, but it's not in the dictionary to add to dictionary would be order_dictionary['customer name'] = input("add customer name ")
                print(order_dictionary)''' """i've done it now, but i want to try make it in a function """

# if order menu abnswer is update existing order status (3)
# then i am defining a new inout to a variable called order_number. whenever i use order_number the user will have to type order number(index) of the person they want to amend
# to get the index number and information in order_dictionary(my list of orders), i use enumerate. labelling index as index and orders as the information in the list
# if my index number is the same as my order number(which is the input i type in)
# it will update the status in the order_dictionary for that order number i typed. - another inout function askign what to update the status to. 
# 2 print func - 1 to see the updated persons info with updated order status, 2nd to see everyone
        elif order_menu_answer == 3:
            listing(order_dictionary)
            order_dictionary_index = int(input("Add Order Number\t"))

            listing(order_status)
            order_status_index = int(input("Add Status Number\t"))

# this is bascally how to updae a dictionary in a list -----   List_name[index value in list]'[dictionary key name'] = new value   
            order_dictionary[order_dictionary_index]['Status'] = order_status[order_status_index]
            print(f" All Orders: {order_dictionary}")
            #for index, orders in enumerate(order_dictionary):
                #if index == order_dictionary_index:
                    #orders['Status'] = input("add new status \t") # is it better for me to define my variable and then add the variable? 

        elif order_menu_answer == 4:
            listing(order_dictionary)


                    



        
     


 # in the main menu section, if they select things other than 0 or 1 or 2, below message will appear.        
else :
   print ("the option you entered doesn't exist, please choose from the available options")
        
                    
                            
    




