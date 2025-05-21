
import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 

from rich import print
from rich.console import Console
console = Console()

from modules.courier_menu_module import courier_menu, courier_list,\
    read_courier_db, append_courier_db, update_courier_db, select_courier

from modules.product_menu_module import product_menu, drinks_list,\
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
     'Customer phone': '079054456543', 'Courier index': courier_list[2], 'Status': 'Preparing',
     'Drink index': '1', 'Food index': '1,3'},

    {'Customer name': 'Ruth Fash', 'Customer address': '66 Bennets, London',
     'Customer phone': '079054896541', 'Courier index': courier_list[1], 'Status': 'Order Confirmed',
     'Drink index': '', 'Food index': '1,5'},

    {'Customer name': 'Mark Taylor', 'Customer address': '88 Baker Street, London',
     'Customer phone': '078903456789', 'Courier index': courier_list[0], 'Status': 'Shipped',
     'Drink index': '2', 'Food index': '2,4'},

    {'Customer name': 'Emily Green', 'Customer address': '45 Elm Road, Manchester',
     'Customer phone': '078754321012', 'Courier index': courier_list[2], 'Status': 'Delivered',
     'Drink index': '3', 'Food index': '4,6'},

    {'Customer name': 'James White', 'Customer address': '76 High Street, Birmingham',
     'Customer phone': '077123456789', 'Courier index': courier_list[2], 'Status': 'Preparing',
     'Drink index': '4', 'Food index': '2,7'}
]

order_status = ['Order Pending','Order Confirmed','Preparing','Out for Delivery', 'Delivered']

#GENERAL 
# Function to write(w) in the csv file 
# - Must state data you want to write into it ('write_data'), and for product nust also state filename. 
def write_order_csv(write_data):
    try:
        with open ('order_list.csv',"w") as file:
            fieldnames = ['Customer name','Customer address','Customer phone','Courier index','Status','Drink index','Food index']
            writefile = csv.DictWriter(file,fieldnames=fieldnames)
            writefile.writeheader()
            writefile.writerows(write_data)
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")

    
#2 Function to read(r) the csv file: 
def read_order_csv():
    try:
        with open ('order_list.csv','r') as file:
            read_csv = list(csv.DictReader(file))
            for index, rows in enumerate(read_csv):
                print(f"{index}:  \nCustomer Info: {rows['Customer name']} , {rows['Customer address']} , {rows['Customer phone']} , \nCourier Info: {rows['Courier index']}, \nOrder Info: {rows['Status']}, Drink Number: {rows['Drink index']}, Food Number: {rows['Food index']}")
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")
    except FileNotFoundError:
        print(f"Error: The file does not exist.")
        
#3 Function to append(a) the csv file: 
def append_order_csv(new_order_details):
    try:
        with open('order_list.csv','a') as file:
            fieldnames = ['Customer name','Customer address','Customer phone','Courier index','Status','Drink index','Food index']
            write = csv.DictWriter(file, fieldnames=fieldnames)
            write.writerow(new_order_details)
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")


#4 Function to print out csv after reading, if reading doesn;t already include print function in it like #1
def display_order_csv(read):
    for index, rows in enumerate(read):
        print(f"{index}:  \nCustomer Info: {rows['Customer name']} , {rows['Customer address']} , {rows['Customer phone']} , \nCourier Info: {rows['Courier index']}, \nOrder Info: {rows['Status']}, Drink Number: {rows['Drink index']}, Food Number: {rows['Food index']}")

#4 Function to read only, no printing
def read_only_order():
    try:
        with open ('order_list.csv','r') as file:
            read_csv = list(csv.DictReader(file))
            return read_csv
    except FileNotFoundError:
        print(f"Error: The file does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")

    

# Input for selection of an order number 
def select_order():
    return int(console.input("[bold]Select order index\t[/bold]"))

# Input for selection of an order status number 
def select_status():
    return int(console.input("[bold]Please enter a status number \t[/bold]"))

def customer_name():
    return console.input('[bold]Enter customer name\t[/bold]').title()
def address_street():    
    return console.input('[bold]Enter street name and number\t[/bold]').title()
def address_city():
    return console.input('[bold]Enter city \t[/bold]').title()
def address_postcode():
    return console.input('[bold]Enter postcode \t[/bold]').capitalize()
    new_address_full = f"{new_address_street}, {new_address_city}, {new_address_postcode}"
def phone_number():
    return console.input('[bold]Enter number\t[/bold]')

def product_index():
    return str(console.input("[bold]Please enter the product index you wish to add\t[/bold]"))

# ------------------------------------------------- Main components of mini project ------------------------------------------------------------- 


# When exiting, saves changes back into csv from what was read csv at the beginning 
def save_exit_order():
    save_exit = read_only_order()
    write_order_csv(save_exit)

 
# New order = order_menu_answer == 2

def new_customer_order():
        
        new_customer_name = customer_name().title()
        new_address_street = address_street().title()
        new_address_city = address_city().title()
        new_address_postcode = address_postcode().capitalize()
        new_address_full = f"{new_address_street}, {new_address_city}, {new_address_postcode}"
        new_customer_number = phone_number()

        read_product_db('drinks_list')
        drink_index = product_index()

        read_product_db('food_list')
        food_index = product_index()

        readcsv = read_only_courier()
        read_courier_db(readcsv)

        selected_courier = select_courier()           # Selecting courier from the courier csv

        if selected_courier is None:
            return  # If invalid input, return early to avoid further processing
        courier = readcsv[selected_courier]  # Selecting courier from the courier CSV


        # Check if any required field is empty
        if not new_address_street or not new_address_city or not new_address_postcode or not new_customer_number or not courier:
            print("[bold red]Error: All required fields must be filled in.[/bold red]")
        # Check if at least one of drink_index or food_index is filled
        elif not drink_index and not food_index:
            print("[bold red]Error: Either a drink or food must be selected.[/bold red]")
              
        elif not new_customer_number.isdigit() or len(new_customer_number) != 11:  # Phone number validation
            print("[bold red]Error: Please ensure the phone number contains exactly 11 digits.[/bold red]") 
            
        else:
            new_customer = {'Customer name': new_customer_name,
            'Customer address': new_address_full, 
            'Customer phone': new_customer_number,
            'Courier index': courier,
            'Status': 'Preparing',
            'Drink index': drink_index, 
            'Food index': food_index}

            append_order_csv(new_customer)
            print("[bold]Order changes have been saved.[/bold]")
        

# Updating order status: order_menu_answer == 3
def update_order_status():
        
        readcsv = read_only_order()
        display_order_csv(readcsv)

        order_index = select_order()

        display(order_status)
        status_index = select_status()

        readcsv[order_index]['Status'] = order_status[status_index]

        write_order_csv(readcsv)
        print("[bold]Order status has been updated[/bold]")
    

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



  








