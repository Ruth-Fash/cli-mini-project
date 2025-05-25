
import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 

from rich import print
from rich.console import Console
console = Console()

from modules.courier_menu_module import courier_menu, courier_list,\
    read_courier_db, append_courier_db, update_courier_db, select_courier, select_courier_optional

from modules.product_menu_module import product_menu, drinks_list, select_index, select_index_optional,\
      food_list,\
     read_product_db

from modules.functions_module \
import display, \
        return_to_submenu, return_answer, delete_another, add_another, clear_screen, get_connection
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
            query = "SELECT * FROM order_list ORDER BY id ASC"

            cursor.execute(query)
            order_rows = cursor.fetchall()

            for row in order_rows :
                print(f"ID: {row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone: {row[3]}, Courier Index: {row[4]}, Status: {row[5]}, Drink ID: {row[6]}, Food ID: {row[7]}")

    except Exception as ex:
        print('Failed to:', ex)

# Input for selection of an order number 
def select_order():

    while True:
        connection = get_connection()

        with connection.cursor() as cursor: 
            query = f'SELECT * FROM order_list ORDER BY id ASC'
            cursor.execute(query)
            order_rows = cursor.fetchall()

            try:
                user_input = console.input("[bold]Select Order index\t[/bold]")
                if not user_input or not user_input.isdigit():
                    print("[bold red]Error: Please enter a number.[/bold red]")
                    continue
                
                selected_id = int(user_input)
                order_ids = [int(row[0]) for row in order_rows]  # Extract just the IDs

                if selected_id not in order_ids:
                    print("[bold red]Error: Selected ID does not exist.[/bold red]")
                    continue

                return selected_id

            except ValueError:
                print("[bold red]Update unsuccessful. A valid ID was not entered.[/bold red]")
                continue

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

        if not name:
            print("Invalid: Cannot leave blank")

        return name
    
def customer_name_optional():
    while True:
        name = console.input('[bold]Enter customer name\t[/bold]')

        if not name:
            return None

        if any(char.isdigit() for char in name):
            print("Invalid: Only letters are allowed.")
            continue

        return name.title()

def address_street():   
    while True: 
        address = console.input('[bold]Enter street name and number\t[/bold]').title()

        if not address:
            print("Cannot leave empty. Please enter a address.")
            continue

        return address
    
def full_address_optional():
    street = console.input('[bold]Enter street name and number (leave blank to skip)\t[/bold]').strip()

    if not street:
        return None  # User wants to skip updating address

    while True:
        city = console.input('[bold]Enter city\t[/bold]').strip()
        if city:
            break
        print("City cannot be blank if street is provided.")

    while True:
        postcode = console.input('[bold]Enter postcode\t[/bold]').strip()
        if postcode:
            break
        print("Postcode cannot be blank if street is provided.")

    return f"{street.title()}, {city.title()}, {postcode.capitalize()}"

def address_city():
    while True:
        city =  console.input('[bold]Enter city \t[/bold]').title()

        if any(char.isdigit() for char in city):
            print("Invalid: Only letters are allowed.")
            continue
        if not city:
            print("Invalid: cannot leave blank")

        return city

def address_city_optional():
    while True:
        city =  console.input('[bold]Enter city \t[/bold]')

        if any(char.isdigit() for char in city):
            print("Invalid: Only letters are allowed.")
            continue

        return city.title()

def address_postcode():
    while True:
        postcode = console.input('[bold]Enter postcode \t[/bold]').capitalize()

        if not postcode:
            print("Postcode must be enterd")
        return postcode
    
def address_postcode_optional():
    while True:
        postcode = console.input('[bold]Enter postcode \t[/bold]')
        
        return postcode.capitalize()

def phone_number():
    while True:
        number = console.input('[bold]Enter number\t[/bold]')

        if not number:
            print("Phone number cannot be empty. Please enter a valid number.")
            continue
        if not number.isdigit or not len(number) == 11:
            print("Invalid: Must be exactly 11 digits with no letters or symbols.")
            continue

        return number
    
def phone_number_optional():
    while True:
        number = console.input('[bold]Enter number\t[/bold]')

        if not number:
            return None

        try:
            if len(number) != 11 or not number.isdigit():
                raise ValueError("Must be exactly 11 digits with no letters or symbols.")
            return number  # only happens if input is valid
        
        except ValueError as e:
            print(f"Invalid: {e}")
            continue  # input was invalid → go back to the top of the loop

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

def update_order(connection):
        
    read_order_db(connection)
    selected_order = select_order()
    update_name = customer_name_optional()
    updated_address = full_address_optional()     
    update_number = phone_number_optional()  

    read_courier_db(connection)
    selected_courier_index = select_courier_optional()

    read_order_status(connection)
    updated_status = select_order_status(connection)

    drinks_index_list = []
    read_product_db(connection,'drinks_list')
    while True:

        updated_drink_index = select_index_optional('drinks_list')
        drinks_index_list.append(updated_drink_index)

        if add_another() != "y":          
            break


    food_index_list = []
    read_product_db(connection, 'food_list')
    while True:
        updated_food_index = select_index_optional('food_list')
        food_index_list.append(updated_food_index)

        if add_another() != "y":          
            break


    try:
        values = []
        updated_fields = []

        if update_name:
            values.append(update_name)
            updated_fields.append("customer_name = %s")
        if updated_address:
            values.append(updated_address)
            updated_fields.append("customer_address = %s")
        if update_number:
            values.append(update_number)
            updated_fields.append("customer_phone = %s")
        if selected_courier_index:
            values.append(selected_courier_index)
            updated_fields.append("courier_index = %s")
        if updated_status:
            values.append(updated_status)
            updated_fields.append("status = %s")
        if updated_drink_index:
            values.append(drinks_index_list)
            updated_fields.append("drinks_id = %s")
        if updated_food_index:
            values.append([food_index_list])
            updated_fields.append("food_id = %s")
        
        values.append(selected_order)

        with connection.cursor() as cursor:
            query = f"UPDATE order_list SET {','.join(updated_fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))

            connection.commit()
            print("[bold green]Order updated successfully.[/bold green]")

    except Exception as ex:
        print('Failed to:', ex)

def del_order(connection):

    read_order_db(connection)
    selected_order = select_order()

    with connection.cursor() as cursor:
        query = "DELETE FROM order_list WHERE id = %s"
        cursor.execute(query, (selected_order,))

        connection.commit()
        print("[bold green]Order deleted successfully.[/bold green]")

    




  








