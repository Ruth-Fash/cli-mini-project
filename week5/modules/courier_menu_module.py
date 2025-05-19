import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 
import csv
from rich import print
from rich.console import Console
console = Console()

import psycopg2 as psycopg
import os
from dotenv import load_dotenv

from modules.functions_module \
import display, \
        return_to_submenu, return_answer, delete_another, add_another, clear_screen

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

def get_connection():
    return psycopg.connect(f"""
    host={host_name}
    dbname={database_name}
    user={user_name}
    password={user_password}
    """)


#GENERAL 
# Function to write(w) in the csv file 
# - Must state data you want to write into it ('write_data'), and for product nust also state filename. 

def select_courier():
    user_input = console.input("[bold]Select courier index\t[/bold]")

    if not user_input or not user_input.isdigit():  # Check if input is empty or not a digit
        print("[bold red]Error: Please enter a valid courier index (a number).[/bold red]")
        return None  # Return None to indicate invalid input

    return int(user_input)  # Return the input as an integer if it is valid


def write_courier_csv(write_data):
    try:
        with open ('courier_list.csv',"w") as file:
            fieldnames = ['Courier Name','Driver Name','Phone Number']
            writefile = csv.DictWriter(file,fieldnames=fieldnames)
            writefile.writeheader()
            writefile.writerows(write_data) 
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")

#2 Function to read(r) the csv file: 
def read_courier_db():
    try:

        # Establishing a connection 
        with psycopg.connect(f"""
            host={host_name}
            dbname={database_name}
            user={user_name}
            password={user_password}
            """) as connection:


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

    except Exception as ex:
        print('Failed to:', ex)

        



#5 Function to read only, no printing
def read_only_courier():
    try:
        with open ('courier_list.csv','r') as file:
            read_csv = list(csv.DictReader(file))
            return read_csv
    except PermissionError:
        print(f"Error: You don't have permission to read this file.")   
    except FileNotFoundError:
        print(f"Error: The file does not exist.")

def input_business_name():
    return console.input("[bold]Enter the courier company name \t[/bold]").title()
def input_driver_name():
    return console.input("[bold]Enter the courier drivers name \t[/bold]").title()
def input_phone_number():
    return console.input("[bold]Enter courier phone number \t[/bold]").title()



# ------------------------------------------------- Main components of mini project ------------------------------------------------------------- 


# When exiting, saves changes back into csv from what was read csv at the beginning 
def save_exit_courier():
    save_exit = read_only_courier()
    write_courier_csv(save_exit)

# Courier_menu_answer == 2:
def add_courier():
    while True:
        clear_screen()

        courier_name = input_business_name()
        driver_name = input_driver_name()
        phone_number = input_phone_number()

    # Check if any input field is empty
        if not courier_name or not driver_name or not phone_number:
            print("[bold red]Update Unsucessful: All fields (Courier Name, Driver Name, Phone Number) are required[/bold red]")
            return_to_submenu('courier')
            break  # Exit the loop if there's an invalid input


    # Store the valid data in the new_courier dictionary
        new_courier = {"Courier Name": courier_name, "Driver Name": driver_name, "Phone Number": phone_number}

    # Check if phone number is valid    
        if new_courier["Phone Number"].isdigit() and len(new_courier["Phone Number"]) == 11:
            append_courier_db(new_courier)
            print("[bold green]Courier changes have been saved[/bold green]")

            if add_another() != 'y':
                return_to_submenu('courier')
                break
        else:
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")
            return_to_submenu('courier')
            break                    

# Courier_menu_answer == 3: 
   # 3 = Update existing courier
    # • Print list, • Select index to update, • Insert new name, 
    # • Updates courier list based of index selected to = input in updated_courier
def update_courier():
            
    read_courier_db()
    
    courier_index = select_courier()
    business_name = input_business_name()
    driver_name = input_driver_name()
    phone_number = input_phone_number()

    clear_screen()

    if business_name:
        readcsv[courier_index]['Courier Name'] = business_name
        print("[bold green]Courier Name has been updated[/bold green]")
    else:
        print("[bold red]Courier Name not updated[/bold red]")


    if driver_name:  
        readcsv[courier_index]['Driver Name'] = driver_name
        print("[bold green]Driver name has been updated[/bold green]")
    else:
        print("[bold red]Driver name not updated[/bold red]")


    if phone_number:
        if phone_number.isdigit() and len(phone_number) == 11:
            readcsv[courier_index]['Phone Number'] = phone_number
            print("[bold green]Courier number has been updated[/bold green]")
        else:
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")
    else:
        print("[bold red]Courier number not updated[/bold red]")
    
    write_courier_csv(readcsv)

# Courier_menu_answer == 4: 
def del_courier():
    try:
        read_courier_db()

        courier_index = select_courier()
        del readcsv[courier_index]

        write_courier_csv(readcsv)
        
        print("[bold green]The courier has been succesfully deleted.[/bold green]")
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")




