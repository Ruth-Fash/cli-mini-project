
import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 

from rich import print
from rich.console import Console
console = Console()

from modules.courier_menu_module import courier_menu, courier_list,\
    read_courier_db, append_courier_db, update_courier_db, select_courier

from modules.product_menu_module import product_menu, drinks_list, select_index,\
      food_list,\
     read_product_db

from modules.functions_module \
import display, \
        return_to_submenu, return_answer, delete_another, add_another, clear_screen
import csv

def order_menu_header():
    print( """[bold]Order Menu[/bold]""")

order_menu = [
    '🏠 Return to Main Menu',
    '📜 Orders List',
    '➕ Create New Order',
    '🔄 Update Customer Order Status',
    '✏️ Update Customer Order Information',
    '❌ Delete Order'
]

order_dictionary = [
    {'Customer name': 'Jessica Smith', 'Customer address': '120 Chancery Lane, London',
     'Customer phone': '07905445654', 'Courier index': '1', 'Status': 'Preparing',
     'Drink index': '1', 'Food index': '1,3'},

    {'Customer name': 'Ruth Fash', 'Customer address': '66 Bennets, London',
     'Customer phone': '07905489654', 'Courier index': '2', 'Status': 'Order Confirmed',
     'Drink index': '', 'Food index': '1,5'},

    {'Customer name': 'Mark Taylor', 'Customer address': '88 Baker Street, London',
     'Customer phone': '07890345678', 'Courier index': '1', 'Status': 'Shipped',
     'Drink index': '2', 'Food index': '2,4'},

    {'Customer name': 'Emily Green', 'Customer address': '45 Elm Road, Manchester',
     'Customer phone': '07875432101', 'Courier index': '3', 'Status': 'Delivered',
     'Drink index': '3', 'Food index': '4,6'},

    {'Customer name': 'James White', 'Customer address': '76 High Street, Birmingham',
     'Customer phone': '07712345678', 'Courier index': '2', 'Status': 'Preparing',
     'Drink index': '4', 'Food index': '2,7'}
]

order_status = ['Order Pending','Order Confirmed','Preparing','Out for Delivery', 'Delivered']


    
#2 Function to read(r) the csv file: 
def read_order_db(connection):
    try:
        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
            query = "SELECT * FROM order_list"

            cursor.execute(query)
            order_rows = cursor.fetchall()

            for row in order_rows :
                print(f"ID:{row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone: {row[3]}, Courier Index: {row[4]}, Status: {row[5]}, Drink ID: {row[6]}, Food ID: {row[7]}")

    except Exception as ex:
        print('Failed to:', ex)

# Input for selection of an order number 
def select_order():
    return int(console.input("[bold]Select order index\t[/bold]"))

# Input for selection of an order status number
def select_order_status(connection):
    try:
        selection =  int(console.input("[bold]Select order status index\t[/bold]"))
    
        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
            query = "SELECT status FROM order_status WHERE id = %s"
            cursor.execute(query, (selection,))
            result = cursor.fetchone()

            if result:
                return result[0]  # Return the status string
            else:
                print("No status found for that ID.")
                return None
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    except Exception as ex:
        print("Failed to fetch order status:", ex)
        return None 




def customer_name():
    while True:
        name = console.input('[bold]Enter customer name\t[/bold]').title()

        if any(char.isdigit() for char in name):
            print("Invalid: Only letters are allowed.")
            continue

        return name

def address_street():   
    while True: 
        address = console.input('[bold]Enter street name and number\t[/bold]').title()

        if not address:
            print("Cannot leave empty. Please enter a address.")

        return address
    
def address_city():
    while True:
        city =  console.input('[bold]Enter city \t[/bold]').title()

        if any(char.isdigit() for char in city):
            print("Invalid: Only letters are allowed.")
            continue

        return city

def address_postcode():
    while True:
        postcode = console.input('[bold]Enter postcode \t[/bold]').capitalize()

        if not postcode:
            print("Postcode must be enterd")
        return postcode

def phone_number():
    while True:
        number = console.input('[bold]Enter number\t[/bold]')

        if number == "":
            print("Phone number cannot be empty. Please enter a valid number.")
            continue
        if not number.isdigit or not len(number) == 11:
            print("Invalid: Must be exactly 11 digits with no letters or symbols.")
            continue

        return number

def add_order(connection):
    try:
        
        new_customer_name = customer_name()
        new_address_street = address_street()
        new_address_city = address_city()
        new_address_postcode = address_postcode()
        new_address_full = f"{new_address_street}, {new_address_city}, {new_address_postcode}"
        new_customer_number = phone_number()


        drinks_index_list = []        
        read_product_db(connection, 'drinks_list')
        
        while True:
            drink_index = select_index('drinks_list')
            drinks_index_list.append(drink_index)

            if add_another() != "y":          
                break
        
        food_index_list = []
        read_product_db(connection, 'food_list')

        while True:
            food_index = select_index('food_list')
            food_index_list.append(food_index)

            if add_another() != "y":          
                break

        read_courier_db(connection)
        selected_courier = select_courier()

        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
            query = "INSERT INTO order_list (customer_name, customer_address, customer_phone, courier_index, status, drinks_id, food_id) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s )"
            cursor.execute(query, (new_customer_name, new_address_full, new_customer_number, selected_courier, '1', drinks_index_list, food_index_list ))
            
            connection.commit()
            print("[bold]Order changes have been saved.[/bold]")

    except Exception as ex:
        print('Failed to:', ex) 
    

def read_order_status(connection):
    try:
        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
            query = "SELECT * FROM order_status"

            cursor.execute(query)
            order_status = cursor.fetchall()

            for row in order_status :
                print(f"ID:{row[0]}, Status: {row[1]}")

    except Exception as ex:
        print('Failed to:', ex)

# Updating order status: order_menu_answer == 3
def update_order_status(connection):

    read_order_db(connection)
    selected_order = select_order()
        
    read_order_status(connection)
    selected_order_status = select_order_status(connection)

    with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
        query = "UPDATE order_list SET status = (%s) WHERE id = (%s)"
        cursor.execute(query, (selected_order_status, selected_order))
        connection.commit()
        print("[bold]Order status has been updated.[/bold]")

    

# Updating order: order_menu_answer == 4
# Updating existing name, address, etc 
def update_order():
        
    readcsv = read_only_order()
    display_order_csv(readcsv)

    selected_order_index = select_order() #order from dict you want to select
    update_name = customer_name().title()
    update_street = address_street().title()
    update_city = address_city().title()
    update_postcode = address_postcode().capitalize()
    update_address = f"{update_street}, {update_city}, {update_postcode}"        
    update_number = phone_number()

    # Construct the full address from the parts
    if update_street and update_city and update_postcode:
        update_address = f"{update_street}, {update_city}, {update_postcode}"


    read_courier_db

    selected_courier = select_courier()   

    read_product_db('drinks_list')
    drink_index = product_index()

    read_product_db('food_list')
    food_index = product_index()

    if update_street and update_city and update_postcode:
        update_address = f"{update_street}, {update_city}, {update_postcode}"
        readcsv[selected_order_index]['Customer address'] = update_address
        print("[bold green]Customer address has been updated[/bold green]")
    else:
        print("[bold red]Customer number not updated[/bold red]")


    if update_name:# If they update inpput then do the below, and if not leave as is
        readcsv[selected_order_index]['Customer name'] = update_name   # • Selecting customer name with selected index updating to = input
        print("[bold green]Customer name has been updated[/bold green]")

    else:
        print("[bold red]Customer name has not updated[/bold red]")

    if update_number:
        if update_number.isdigit() and len(update_number) == 11:
            readcsv[selected_order_index]['Customer phone'] = update_number
            print("[bold green]Customer number has been updated[/bold green]")
        else: 
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")
    else:
        print("[bold red]Customer number not updated[/bold red]")

    if selected_courier: 
        readcsv[selected_order_index]['Courier index'] = read_courier_csv[selected_courier]          
        print("[bold green]Courier has been updated[/bold green]")
    else:
        print("[bold red]Courier has not updated[/bold red]")

    if drink_index: 
        readcsv[selected_order_index]['Drink index'] = drink_index          
        print("[bold green]Drink index has been updated[/bold green]")
    else:
        print("[bold red]Drink index has not updated[/bold red]")

    if food_index: 
        readcsv[selected_order_index]['Food index'] = food_index          
        print("[bold green]Food index has been updated[/bold green]")
    else:
        print("[bold red]Food index has not updated[/bold red]")

    write_order_csv(readcsv)


# Deleting order: order_menu_answer == 5
# Print, •Input to select index from order dict, •Deleting index from order, •Print 

def del_order():
    try:
        readcsv = read_only_order()
        display_order_csv(readcsv)
        selected_index = select_order()

        del readcsv[selected_index]
        
        write_order_csv(readcsv)
        print("[bold green]The order has been succesfully deleted.[/bold green]")                    
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")



  








