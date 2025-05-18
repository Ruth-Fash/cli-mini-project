import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week5') 
from rich import print
from rich.console import Console
console = Console()
import csv
import psycopg2 as psycopg
import os
from dotenv import load_dotenv




from modules.functions_module \
import display, \
        return_to_submenu, return_answer, delete_another, add_another, clear_screen

def product_menu_header():
    print( """[bold]Products Menu[/bold]
""")

product_menu = [
    '🏠 Return to Main Menu',
    '📜 Drinks Menu',
    '📜 Food Menu',
    '➕ Add New Drink',
    '➕ Add New Food',
    '✏️ Update Existing Drink ',
    '✏️ Update Existing Food',
    '❌ Remove Drink',
    '❌ Remove Food']

drinks_list = [{'Name':'Espresso','Price': 2.50},           
            {'Name':'Americano','Price': 3.00},  
            {'Name':'Latte','Price': 4.00}, 
            {'Name':'Cappuccino','Price': 4.00}, 
            {'Name':'Macchiato','Price': 3.50}, 
            {'Name':'Matcha Latte','Price': 4.50},
            {'Name':'Hot Chocolate','Price': 3.00},
            {'Name':'Chai Latte','Price': 4.00},
            {'Name':'Green Tea','Price': 3.50},
            {'Name':'Black tea','Price': 2.50},
            {'Name':'Still water','Price': 1.50},
            {'Name':'Orange juice','Price': 3.50},
            {'Name':'Coke','Price': 3.50}] 

food_list = [{'Name':'Avocado_toast','Price': 5.00},
            {'Name':'Eggs','Price': 3.00},
            {'Name':'Toast','Price': 2.00},
            {'Name':'BLT','Price': 6.00},
            {'Name':'Chicken Salad','Price': 7.50},
            {'Name':'Grilled Cheese','Price': 5.00},
            {'Name':'Tuna melt','Price': 7.00},
            {'Name':'Plain croissant','Price': 2.50},
            {'Name':'Cinnamon roll','Price': 2.50},
            {'Name':'Carrot cake','Price': 3.50}] 




# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
print("Host from env:", os.getenv("POSTGRES_HOST"))
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")



# GENERAL:


# Function to write(w) in the csv file. Must state what data you want to write (write_data), and for product file you want (csvname) also state filename. 
def write_product_csv(csvname,write_data):
    try:
        if not isinstance(write_data, list):  #checking if read(the csv) is a list
            print("[bold red]Error: Invalid data format. Expected a list of dictionaries.[/bold red]")
            return        
        
        with open (csvname+'_list.csv',"w") as file:
            fieldnames = ['Name','Price']
            writefile = csv.DictWriter(file,fieldnames=fieldnames)
            writefile.writeheader()
            writefile.writerows(write_data)
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")

# Function to read(r) the csv file. State the filename you want to use (csvname)
def read_product_db(table_name):
    try:

        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:


            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

                query = f'SELECT * FROM {table_name} ORDER BY id ASC'
                cursor.execute(query)
                product_rows = cursor.fetchall()
            
                for row in product_rows: 
                    print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")
    
    except Exception as ex:
        print('Failed to:', ex)

         

# Function to append(a) the csv file. State the filename you want to use (csvname) and what you are adding to it(append)
def append_product_db(table_name,value):

    try:
        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:


            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

                query = f"""INSERT INTO {table_name} (name, price)\
                            VALUES (%s, %s)"""
                cursor.execute(query, value)
                connection.commit()

    except Exception as ex:
        print('Failed to:', ex)


# Function to print out csv after reading, if reading doesn't already include print function in it like #2
# 'read' is based off what ever the variable name for reading the file is like readcsv in #2
def display_product_csv(read):
    if not isinstance(read, list):  #checking if read(the csv) is a list
        print("[bold red]Error: Invalid data format. Expected a list of dictionaries.[/bold red]")
        return
    
    if not read:  #checking if read(the csv) is empty
        print("[bold red]No products available.[/bold red]")
        return       
    
    for index, rows in enumerate(read):
        print(f"{index}:  {rows['Name']} - £{rows['Price']}")

# Function to read only, no printing
def read_only_product(csvname):
    try:     
        with open (csvname +'_list.csv','r') as file:
            read_csv = list(csv.DictReader(file))

            if not read_csv:  #checking if read(the csv) is empty
                print("[bold red]No products available.[/bold red]")
                return
            
            return read_csv
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")


# Product_menu = 3 & 4 (Adding a drink/food item).
# Functions to ask user for food/drink name, price
def modify_drinkname():
    return console.input("[bold]Add new product name \t[/bold]").title()

def modify_price():
    return console.input("[bold]Add price \t[/bold]")

def new_drinks():
    drink_name = modify_drinkname()
    drink_price = modify_price()

    # Check if either name or price is empty
    if not drink_name or not drink_price:
        print("[bold red]Name and price cannot be empty.[/bold red]")
        return None  # Return None if inputs are invalid
    # Check if price is a valid number
    try:
        drink_price = float(drink_price)
    except ValueError:
        print("[bold red]Invalid price. Please enter a valid number.[/bold red]")
        return None  # Return None if price is invalid
            
    return (drink_name, drink_price)    # Proceed if both name and price are valid


def modify_foodname():
    return console.input("[bold]Add new product name \t[/bold]").title()

def new_food():   
    food_name = modify_foodname()
    food_price = modify_price()

    if not food_name or not food_price:
        print("[bold red]Name and price cannot be empty.[/bold red]")
        return None  # Return None if inputs are invalid

    try:
        food_price = float(food_price)
    except ValueError:
        print("[bold red]Invalid price. Please enter a valid number.[/bold red]")
        return None  # Return None if price is invalid

    return (food_name, food_price )


def select_index():
    return console.input("[bold]Please select an index \t[/bold]")

def updated_product():
    return str(console.input("[bold]Enter new name for (leave blank to keep current name): \t[/bold]")).title()

def updated_price():
    return console.input("[bold]Enter new price (leave blank to keep current price): \t[/bold]")



# ------------------------------------------------- Main components of mini project ------------------------------------------------------------- 


# When exiting, saves changes back into csv from what was read csv at the beginning 
def save_exit_food():
    save_exit = read_only_product('food')
    write_product_csv('food',save_exit)

def save_exit_drinks():
    save_exit = read_only_product('drinks')
    write_product_csv('drinks',save_exit)



# Selected_product_menu == 3
# Prints list, appends given user inputs into the csv; user input if to add another
# While loop - if n return to product menu, other wise loop back to top and ask to addd new product
def add_drink():
        read_product_db('drinks_list')
        newdrink = new_drinks() 
        
        if newdrink:
            append_product_db('drinks_list',newdrink)
            print("[bold green]Drinks menu changes have been saved.[/bold green]")
        else:
             print("[bold red]Failed to add the drink due to invalid input.[/bold red]")


# Selected_product_menu == 4
# Same as above
def add_food():
        read_product_db('food_list')
        newfood = new_food() 
        
        if newfood:
            append_product_db('food_list',newfood)
            print("[bold green]Drinks menu changes have been saved.[/bold green]")
        else:
             print("[bold red]Failed to add the drink due to invalid input.[/bold red]")   

        

# Updating an exisiting drinks name and/or price: selected_product_menu == 5  
# Read and print csv; User inputs for drink index to update, and updates drink/price. If user leaves blank will stay as orginal
# If not it will update and write it back into the csv 
def update_drink():
    read_product_db('drinks_list')

    index = select_index()
    drinkname = updated_product()
    price = updated_price()

    try:
        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:


            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

                if drinkname and price:
                    query = f'UPDATE drinks_list \
                            SET name = %s, price = %s WHERE id = %s'
                    cursor.execute(query, (drinkname, price, index))

                elif drinkname:
                    query = f'UPDATE drinks_list \
                            SET name = %s WHERE id = %s'
                    cursor.execute(query, (drinkname, index))

                elif price:
                    query = f'UPDATE drinks_list \
                            SET price = %s WHERE id = %s'
                    cursor.execute(query, (price, index))
                
                else:
                    print("[bold red]Nothing to update.[/bold red]")
                    return
                
                if cursor.rowcount == 0:
                    print(f"[bold red]No food found with ID {index}. Nothing was deleted.[/bold red]")

                else:
                    connection.commit()
                    print("[bold green]Food updated successfully.[/bold green]")


    except Exception as ex:
        print('Failed to:', ex)





# Selected_product_menu == 6
# Same as above but for food
def update_food():
    read_product_db('food_list')

    index = select_index()
    foodname = updated_product()
    price = updated_price()
    
    try:
        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:


            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.


                if foodname and price:
                    query = f'UPDATE food_list \
                            SET name = %s, price = %s WHERE id = %s'
                    cursor.execute(query, (foodname, price, index))

                elif foodname:
                    query = f'UPDATE food_list \
                            SET name = %s WHERE id = %s'
                    cursor.execute(query, (foodname, index))

                elif price:
                    query = f'UPDATE food_list \
                            SET price = %s WHERE id = %s'
                    cursor.execute(query, (price, index))
                
                else:
                    print("[bold red]Nothing to update.[/bold red]")
                    return

                if cursor.rowcount == 0:
                    print(f"[bold red]No food found with ID {index}. Nothing was deleted.[/bold red]")

                else:
                    connection.commit()
                    print("[bold green]Food updated successfully.[/bold green]")

    except Exception as ex:
        print('Failed to:', ex)



# Deleting an exisiting drinks name and/or price: selected_product_menu == 7 
# Read and print csv; User inputs for drink index to delete, and updates drink/price. 
# It will update and write it back into the csv 
def del_drink():

    read_product_db('drinks_list')
    index = select_index()

    try:
        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:

            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
                query = " DELETE FROM drinks_list WHERE id = %s"
                cursor.execute(query,(index,))

                if cursor.rowcount == 0:
                    print(f"[bold red]No drink found with ID {index}. Nothing was deleted.[/bold red]")

                else:
                    connection.commit()
                    print("[bold green]The item has been succesfully deleted.[/bold green]")

    except Exception as ex:
        print('Failed to:', ex)


        
# Selected_product_menu == 8
# Same as above but for food
def del_food():

    read_product_db('food_list')
    index = select_index()

    try:
        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:

            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.
                query = " DELETE FROM food_list WHERE id = %s"
                cursor.execute(query,(index,))

                if cursor.rowcount == 0:
                    print(f"[bold red]No drink found with ID {index}. Nothing was deleted.[/bold red]")

                else:
                    connection.commit()
                    print("[bold green]The item has been succesfully deleted.[/bold green]")

    except Exception as ex:
        print('Failed to:', ex)





