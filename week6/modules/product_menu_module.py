import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week6') 
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
from modules.functions_module import (get_connection)
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


# Function to read(r) the csv file. State the filename you want to use (csvname)
def read_product_db(connection,table_name):
    try:
        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

            query = f'SELECT * FROM {table_name} ORDER BY id ASC'
            cursor.execute(query)
            product_rows = cursor.fetchall()
        
            for row in product_rows: 
                print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

    except Exception as ex:
        print('Failed to:', ex)


def new_product():
    product_name = console.input("[bold]Add new product name \t[/bold]").title()

    if not product_name:
        print("[bold red]Product name cannot be empty.[/bold red]")
        return None
       
    return product_name


def new_price():
    try:
        input_price = console.input("[bold]Add price \t[/bold]")
        price = float(input_price)

        # Check if either name or price is empty
        if not price:
            print("[bold red]Price cannot be empty and must be a number.[/bold red]")
            return None  # Return None if inputs are invalid
        # Check if price is a valid number           
        return price    # Proceed if both name and price are valid
    
    except ValueError:
        print("[bold red]Invalid input. Please enter a number.[/bold red]")
        return None


def select_index(table_name):

    while True:
        connection = get_connection()
        with connection.cursor() as cursor: 
            query = f'SELECT * FROM {table_name} ORDER BY id ASC'
            cursor.execute(query)
            product_rows = cursor.fetchall()

            try:
                user_input = console.input("[bold]Please select an index \t[/bold]")
                if not user_input or not user_input.isdigit():
                    print("[bold red]Error: Please enter a number.[/bold red]")
                    continue
                
                selected_id = int(user_input)
                product_ids = [int(row[0]) for row in product_rows]  # Extract just the IDs

                if selected_id not in product_ids:
                    print("[bold red]Error: Selected ID does not exist.[/bold red]")
                    continue

                return selected_id

            except ValueError:
                print("[bold red]Update unsuccessful. A valid ID was not entered.[/bold red]")
                continue
  

def updated_product():
        return str(console.input("[bold]Enter new name for (leave blank to keep current name): \t[/bold]")).title()


def updated_price():
    input_price = console.input("[bold]Enter new price (leave blank to keep current price): \t[/bold]")

    if not input_price:
        return None
    
    try:
        updated_price = float(input_price)
        return updated_price  
    except ValueError:
        print("[bold red]Invalid input. Please enter a number.[/bold red]")
        return None


def add_drink(connection):
    product = new_product()
    price = new_price()

    try:
        with connection.cursor() as cursor: 

            query = f"INSERT INTO drinks_list (name, price)\
                VALUES (%s, %s)"
        
            cursor.execute(query, (product,price))
            connection.commit()
            print("New product added")

    except Exception as ex:
        print('Failed to:', ex) 
        

def add_food(connection):
    product = new_product()
    price = new_price()

    try:
        with connection.cursor() as cursor: 

            query = f"INSERT INTO food_list (name, price)\
                VALUES (%s, %s)"
        
            cursor.execute(query, (product,price))
            connection.commit()
            print("New product added")

    except Exception as ex:
        print('Failed to:', ex) 
        

# Updating an exisiting drinks name and/or price: selected_product_menu == 5  
# Read and print csv; User inputs for drink index to update, and updates drink/price. If user leaves blank will stay as orginal
# If not it will update and write it back into the csv 
def update_drink(connection):
    index = select_index('drinks_list')
    drinkname = updated_product()
    price = updated_price()

    try:
        # Establishing a connection 

            with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

                if drinkname and price:
                    query = 'UPDATE drinks_list \
                            SET name = %s, price = %s WHERE id = %s'
                    cursor.execute(query, (drinkname, price, index))

                elif drinkname:
                    query = 'UPDATE drinks_list \
                            SET name = %s WHERE id = %s'
                    cursor.execute(query, (drinkname, index))

                elif price:
                    query = 'UPDATE drinks_list \
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
def update_food(connection):
    index = select_index('food_list')
    foodname = updated_product()
    price = updated_price()
    
    try:
        # Establishing a connection 
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
def del_drink(connection):
    index = select_index('drinks_list')

    try:
        # Establishing a connection 
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
def del_food(connection):

    index = select_index('food_list')

    try:
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





