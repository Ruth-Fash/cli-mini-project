import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 
import csv
from rich import print
from rich.console import Console
console = Console()
import psycopg2 as psycopg
import os
from dotenv import load_dotenv

from modules.functions_module import (get_connection)


def courier_menu_header():
    print( """[bold]Courier Menu[/bold]""")

courier_menu = [
    '🏠 Back to Main Menu',
    '🚚 Courier List',
    '➕ Add New Courier',
    '✏️ Update Existing Courier',
    '❌ Delete Courier']


courier_list = [{"Courier Name" : "Deliveroo", "Driver Name" : "Juls", "Phone Number" : "07985739021"},
                {"Courier Name" : "Uber Eats", "Driver Name" : "Matt", "Phone Number" : "07985739345"},
              {"Courier Name" : "Just Eat", "Driver Name" : "Jodie", "Phone Number" : "07904594342"}]


# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
print("Host from env:", os.getenv("POSTGRES_HOST"))
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")



def input_business_name():
    while True:
        user_input = console.input("[bold]Enter the courier company name \t[/bold]").title()
        if not user_input:
            print("[bold red]Courier company name cannot be empty. Please enter a valid name.[/bold red]")
            continue
        return user_input

def input_business_name_optional():
    return console.input("[bold]Enter the courier company name \t[/bold]").title()

def input_driver_name():
    while True:
        user_input = console.input("[bold]Enter the courier driver's name: [/bold]").title()
        if any(char.isdigit() for char in user_input):
            print("Invalid: Only letters are allowed.")
            continue
        if user_input == "":
            print("Driver name cannot be empty. Please enter a valid name.")
            continue
        return user_input

def input_driver_name_optional():
    while True:
        user_input = console.input("[bold]Enter the courier drivers name \t[/bold]").title()
        if any(char.isdigit() for char in user_input): 
            print ("Invalid: Only letters are allowed.")
            continue

        return user_input

    
def input_phone_number():
    while True:
        user_input = console.input("[bold]Enter courier phone number \t[/bold]")

        if user_input == "":
            print("Driver name cannot be empty. Please enter a valid name.")
            continue

        if not user_input.isdigit() or not len(user_input) == 11:
            print("Invalid: Must be exactly 11 digits with no letters or symbols.")
            continue

        return user_input
    
def input_phone_number_optional():
    while True:
        user_input = console.input("[bold]Enter courier phone number (leave blank to keep current): [/bold]").strip()

        if user_input == "":
            return None  # blank allowed here

        if not user_input.isdigit() or len(user_input) != 11:
            print("[bold red]Invalid: Must be exactly 11 digits with no letters or symbols.[/bold red]")
            continue

        return user_input


def select_courier():
    connection = get_connection()
    with connection.cursor() as cursor:
        query = f'SELECT * FROM courier_list ORDER BY courier_id ASC'
        cursor.execute(query)
        courier_rows = cursor.fetchall()

        try:
            user_input = console.input("[bold]Select courier index: [/bold]")
            if not user_input or not user_input.isdigit():
                print("[bold red]Error: Please enter a number.[/bold red]")
                return None

            selected_id = int(user_input)
            courier_ids = [row[0] for row in courier_rows]  # Extract just the IDs

            if selected_id not in courier_ids:
                print("[bold red]Error: Selected courier ID does not exist.[/bold red]")
                return None

            return selected_id

        except ValueError:
            print("[bold red]Update unsuccessful. A valid number was not entered.[/bold red]")
            return None


# ------------------------------------------------- Main components of mini project ------------------------------------------------------------- 


# Function to read(r) the csv file: 
def read_courier_db(connection):
    try:

        with connection.cursor() as cursor:  # WITH - allows you to open cursor and automatically close the cursor.

            query = f'SELECT * FROM courier_list ORDER BY courier_id ASC'
            cursor.execute(query)
            courier_rows = cursor.fetchall()
        
            for row in courier_rows: 
                    print(f"ID: {row[0]}, Courier Name: {row[1]}, Driver Name: {row[2]}, Phone Number: {row[3]}")
    
    except Exception as ex:
        print('Failed to:', ex)

            

#3 Function to append(a) the csv file: 
def append_courier_db(connection):

    courier_name = input_business_name()
    driver_name = input_driver_name()
    phone_number = input_phone_number()

    try:
        
        with connection.cursor() as cursor:
            query = "INSERT INTO courier_list (courier_name, driver_name, phone_number)\
                    VALUES (%s, %s, %s)"
            
            cursor.execute(query, (courier_name, driver_name, phone_number))
            connection.commit()
            print("[bold green]Courier successfully added to the database.[/bold green]")


    except Exception as ex:
        print('Failed to:', ex)


# Courier_menu_answer == 3: 
   # 3 = Update existing courier
    # • Print list, • Select index to update, • Insert new name, 
    # • Updates courier list based of index selected to = input in updated_courier
def update_courier_db(connection):
    
    while True:
        courier_index = select_courier()
        if courier_index is None:
            continue
        courier_name = input_business_name_optional()
        driver_name = input_driver_name_optional()
        phone_number = input_phone_number_optional()
        break


    try:
        with connection.cursor() as cursor:

            updated_fields = []
            values = []       

            if courier_name:
                updated_fields.append("courier_name = %s")
                values.append(courier_name)

            if driver_name:
                updated_fields.append("driver_name = %s")
                values.append(driver_name)

            if phone_number:
                updated_fields.append("phone_number = %s")
                values.append(phone_number)

            if not updated_fields:
                print("[bold red]Nothing to update.[/bold red]")
                return
            
            values.append(courier_index)
            
            query =f"UPDATE courier_list SET {','.join(updated_fields)} WHERE courier_id = %s"
            cursor.execute(query,tuple(values))

            if cursor.rowcount == 0:
                print(f"[bold red]No courier found with ID {courier_index}. Nothing was updated.[/bold red]")
            else:
                connection.commit()
                print("[bold green]Courier updated successfully.[/bold green]")


    except Exception as ex:
        print('Failed to update courier:', ex)



# Courier_menu_answer == 4: 
def del_courier_db(connection):
    try:

        courier_index = select_courier()

        try:
            with connection.cursor() as cursor:
                query = "DELETE FROM courier_list WHERE COURIER_ID = %s"
                cursor.execute(query, (courier_index, ))

                connection.commit()
                print("[bold green]Courier deleted successfully.[/bold green]")


        except Exception as ex:
            print('Failed to delete courier:', ex)

    
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")




