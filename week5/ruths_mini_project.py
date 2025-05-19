import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 

from rich import print
from rich.console import Console
console = Console()
import csv

main_menu_header = """[bold]☕☕☕ Welcome to the Main Menu ☕☕☕[/bold]"""

main_menu = [
    'Exit App ❌',
    'Products 🍽',
    'Courier 🚚',
    'Orders 📝']

# ----------------------------------------------------------------- PRODUCT/COURIER/ORDER MODULE -------------------------------------------------------------------  


from modules.product_menu_module import (product_menu, drinks_list,\
      food_list, new_drinks, new_food,\
       write_product_csv, append_product_db, read_product_db, display_product_csv, del_food, del_drink,\
       update_food, update_drink, read_only_product, save_exit_food, save_exit_drinks, add_drink, add_food, product_menu_header)

from modules.order_menu_module import (order_menu, order_dictionary, order_status,\
    write_order_csv, read_order_csv, append_order_csv, display_order_csv, new_customer_order, update_order, del_order,\
    update_order_status, read_only_order, save_exit_order, order_menu_header)
from modules.courier_menu_module import (courier_menu, courier_list,\
    read_courier_db, append_courier_db, write_courier_csv, update_courier, select_courier, read_only_courier,\
    save_exit_courier, add_courier, del_courier, courier_menu_header, get_connection)


# ---------------------------------------------------------------------  FUNCTION MODULE -------------------------------------------------------------------  

from modules.functions_module \
import display,\
        return_to_submenu, return_answer, delete_another, add_another, clear_screen


# ------------------------------------------------------------------------  MAIN MENU -------------------------------------------------------------------  
read_only_product('drinks')
read_only_product('food')
read_only_order()
read_only_courier()
clear_screen()
# main menu input - select option from main menu
while True:
    print(main_menu_header)
    display(main_menu)
    main_menu_answer = int(console.input("[bold]Please enter an option from the main menu\t[/bold]"))


# Select 0 = reads drink,food,courier,order dictionaries to csv file with r mode and exits printing a message; 
    if main_menu_answer == 0 :
        save_exit_drinks()
        save_exit_food()
        save_exit_courier()
        save_exit_order()

        print ('"[bold green]Data saved. Exiting app...[/bold green]')
        exit()
        print("This will not print if the user exits.") # test to see if exit works 


# ----------------------------------------------------------------- PRODUCT MENU ----------------------------------------------------------------------

# Select 1 from main menu = navigates to order menu in the module py
# Asks for user input to make a seleection in the product menu
    elif main_menu_answer == 1:
        while True:
            clear_screen()
            product_menu_header()
            display(product_menu)                
            selected_product_menu = int(console.input("[bold]Please enter an index from the product menu\t[/bold]"))         

        # Within product menu if/elif statements to make a selection  (0-7)

# 0 = Back to main menu, Prints main menu list with function. this is the point where the while loop stops with break.
            if selected_product_menu == 0 :
                clear_screen()
                break
                
# 1 = Prints the drinks dictionary from the csv using the function 
            
            elif selected_product_menu == 1:
                clear_screen()
                read_product_db('drinks_list')
                return_to_submenu('product')         # User input to go back to sub-menu; While loop - if 0 breaks loop back to the product menu, else if you don't it will print error message and loop back to user input to go to sub menu 



# 2 = Prints the food dictionary from the csv using the function 
            elif selected_product_menu == 2 :
                clear_screen()
                read_product_db('food_list')  
                return_to_submenu('product') 

# 3 = Adding a new drink to csv. 
            elif selected_product_menu == 3 :
                while True:
                    clear_screen()
                    add_drink()

                    if add_another() != 'y':
                        return_to_submenu('products')
                        break
                    

# 4 = Adding a new food to csv. 
# Same as above from food

            elif selected_product_menu == 4 :
                while True:
                    add_food()
                    if add_another() != 'y':
                        return_to_submenu('products')
                        break 

# 5 = Updating an exisiting drinks name and/or price

            elif selected_product_menu == 5 :
                while True:
                    clear_screen()
                    try:
                        update_drink()

                    except ValueError:
                        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]") 
                                    
                    if add_another() != 'y':
                        return_to_submenu('products')
                        break


# 6 = Updating an exisiting food name and/or price

            elif selected_product_menu == 6 :
                while True:    
                    clear_screen()
                    try:
                        update_food()

                    except ValueError:
                        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")
                    
                    if add_another() != 'y':
                        return_to_submenu('products')
                        break


# 7 = Deleting a drink
            elif selected_product_menu == 7 :
                while True:
                    clear_screen()

                    del_drink()

                    if delete_another() != 'y':
                        return_to_submenu('products')
                        break


# 7 = Deleting a product food
            elif selected_product_menu == 8:
                while True:
                    clear_screen()

                    del_food()
                        
                    if delete_another() != 'y':
                        return_to_submenu('product')
                        break
                    

            
# In product menu section, if they select soemthign not in list they will get below print message.
            else:
                clear_screen()
                print ("[bold red]the option you entered doesn't exist, please choose from the available options[/bold red]")
                return_to_submenu('product')
              

    # ------------------------------------------------------------------ ORDER MENU ---------------------------------------------------------------------  

# Select 3 from main menu = navigates to order menu in the module py
    elif main_menu_answer == 3:
        while True:
            clear_screen()
            order_menu_header()
            display(order_menu) 
            order_menu_answer = int(console.input("[bold]Please enter an index from the order menu\t[/bold]"))  


# 0 = Back to main menu      
            if order_menu_answer == 0:
                clear_screen()
                break


# 1 = Prints the orders from the csv using the function               
            elif order_menu_answer == 1:
                clear_screen()
                read_order_csv()
                return_to_submenu('order')


# 2 = Adding a new order
            elif order_menu_answer == 2:
                while True:
                    clear_screen()
                    try:
                        new_customer_order()

                        if add_another() != 'y':
                            return_to_submenu('order')
                            break

                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

    
 # 3 = Updating existing order status
            elif order_menu_answer == 3:
                while True:
                    clear_screen()
                    try:
                        update_order_status()

                    except ValueError:
                        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

                    if add_another() != 'y':
                        return_to_submenu('order')
                        break


# 4 = Updating existing name, address, etc 
            elif order_menu_answer == 4:
                while True:
                    clear_screen()
                    try:
                        update_order()
                      
                    except ValueError:
                        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

                    if add_another() != 'y':
                        return_to_submenu('order')
                        break    
# 5 = Deleting order
            elif order_menu_answer == 5:
                while True:
                    clear_screen()
                    del_order()

                    if delete_another() != 'y':
                        return_to_submenu('order')
                        break
                    
# In the sub menu section, if they select things other than 0 or 1 or 2, below message will appear. 
            else: 
                clear_screen()
                print ("[bold red]the option you entered doesn't exist, please choose from the available options[/bold red]")
                return_to_submenu('order')



    #------------------------------------------------------------------ COURIER MENU ---------------------------------------------------------------------------
# Select 2 from main menu = navigates to order menu in the module py
    elif main_menu_answer == 2:
        while True:
            clear_screen()
            courier_menu_header()
            display(courier_menu)
            courier_menu_answer = int(console.input("[bold]Select an option from the order menu \t[/bold]"))


# 0 = Back to main menu
            if courier_menu_answer == 0:
                clear_screen()
                break


# 1 = Print courier list
            elif courier_menu_answer == 1:
                clear_screen()
                read_courier_db()
                return_to_submenu('courier')


 # 2 = Add new courier
            elif courier_menu_answer == 2:
                clear_screen()
                try:
                    conn = get_connection()
                    append_courier_db(conn)
                    conn.close()

                    if add_another() != 'y':
                        return_to_submenu('courier')

                except ValueError:
                    print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")






# 3 = Update existing courier
            elif courier_menu_answer == 3:
                while True:
                    clear_screen()
                    try:
                        update_courier()

                        if add_another() != 'y':
                            return_to_submenu('courier')


                    except IndexError:
                        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")
                    except ValueError:
                        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")




# 4 = Deleting an existing courier
            elif courier_menu_answer == 4:
                while True:
                    clear_screen()
                    del_courier()

                    if delete_another() != 'y':
                        return_to_submenu('courier')
                        break


# In the sub menu section, if they select things other than 0 or 1 or 2, below message will appear.                     
            else: 
                clear_screen()
                print ("[bold red]the option you entered doesn't exist, please choose from the available options[/bold red]")
                return_to_submenu('courier')
   


# In the main menu section, if they select things other than 0 or 1 or 2, below message will appear.        
    else:
        while True:
            clear_screen()
            print ("[bold red]the option you entered doesn't exist, please choose from the available options[/bold red]")
            break     
            
                                
        




