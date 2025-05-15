import pytest
import sys
import csv
import shutil
sys.path.append('/Users/ruthfashogbon/Desktop/Generation')
from rich.console import Console
console = Console()

# ------------------------- TEST FOR ADDING COURIER ----------------------

""" 1. Test that a courier is successfully added and then removed after the test. - Adding orders works exactly the same, using the same code"""
from my_reps.ruths_mini_project.week4.modules.courier_menu_module import read_only_courier, append_courier_csv,write_courier_csv

def test_add_courier():
    # Add drink
    new_courier = {"Courier Name" : 'Quick Food', "Driver Name" : 'Jacob Stylo', "Phone Number" : '07784757687'}
    append_courier_csv(new_courier)

    # Read again to check if it was added
    expected = {"Courier Name" : 'Quick Food', "Driver Name" : 'Jacob Stylo', "Phone Number" : '07784757687'}
    actual = read_only_courier()[-1]

    assert actual == expected, f"Test failed: expected '{expected}', got '{actual}'"

    # Cleanup: Remove the last added drink
    courier = read_only_courier()  # Get the current list
    write_courier_csv(courier[:-1])  # Remove the last entry

""" 2.  Error handling: Test that max phone number digits = if phone number is over 11 - Adding orders works exactly the same, using the same code"""

def add_courier_numberlen():
        new_courier = {"Courier Name" : 'Foodie Fast',\
                        "Driver Name": 'Liz Smith',\
                        "Phone Number": '079389485859500'}

        if new_courier["Phone Number"].isdigit() and len(new_courier["Phone Number"]) == 11:
            print("[bold green]Courier changes have been saved[/bold green]")

        else:
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")

def test_add_courier_numberlen(capsys):
    
    expected = "[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]\n"

    add_courier_numberlen()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"
     
""" 3.  Error handling: Test that max phone number digits = if phone number is less than 11 - Adding orders works exactly the same, using the same code """

def add_courier_numberlen_less():
        new_courier = {"Courier Name" : 'Foodie Fast',\
                        "Driver Name": 'Liz Smith',\
                        "Phone Number": '0793'} #invalid length of numbers

        if new_courier["Phone Number"].isdigit() and len(new_courier["Phone Number"]) == 11:
            print("[bold green]Courier changes have been saved[/bold green]")

        else:
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")

def test_add_courier_numberlen_less(capsys):
    
    expected = "[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]\n"

    add_courier_numberlen()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 4.  Error handling: When entry left blank - Testing on driver_name. - Adding orders works exactly the same, using the same code"""

def add_courier_entry_blank():
    courier_name = 'Good Food'
    driver_name = ""
    phone_number = '09758698759'

# Check if any input field is empty
    if not courier_name or not driver_name or not phone_number:
        print("[bold red]Update Unsucessful: All fields (Courier Name, Driver Name, Phone Number) are required[/bold red]")

def test_add_courier_entry_blank(capsys):

    expected = "[bold red]Update Unsucessful: All fields (Courier Name, Driver Name, Phone Number) are required[/bold red]\n"

    add_courier_entry_blank()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 5.  Error handling: If phone number includes letters - Adding orders works exactly the same, using the same code"""

def add_courier_number_value():
        new_courier = {"Courier Name" : 'Foodie Fast',\
                        "Driver Name": 'Liz Smith',\
                        "Phone Number": '0798475876e'}

        if new_courier["Phone Number"].isdigit() and len(new_courier["Phone Number"]) == 11:
            print("[bold green]Courier changes have been saved[/bold green]")

        else:
            print("[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]")

def test_add_courier_number_value(capsys):
    
    expected = "[bold red]Update unsuccessful: Please ensure the phone number contains exactly 11 digits[/bold red]\n"

    add_courier_number_value()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


# ------------------------- TEST FOR UPDATING COURIER ----------------------
from my_reps.ruths_mini_project.week4.modules.courier_menu_module import update_courier, read_only_courier

""" 6. Test invalid index  - out of range - Updating orders works exactly the same, using the same code"""
def update_courier_blank_index():
    business_name = 'Eat Good'
    driver_name = 'Jack'
    phone_number = '07985738940'
    courier_index = 25
    readcsv = read_only_courier()

    try:
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
                readcsv[courier_index]['Number'] = phone_number
                print("[bold green]Courier number has been updated[/bold green]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")

def test_update_courier_blank_index(capsys):

    update_courier_blank_index()

    expected = "[bold red]Update unsucessful. The index entered does not exist.[/bold red]\n"

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 7. Test if user inout left blank, will leave as orginal - test on phone number - Updating orders works exactly the same, using the same code"""
def update_input_blank():
    business_name = 'Eat Good'
    driver_name = 'Jack'
    phone_number = ''
    courier_index = 0
    readcsv = read_only_courier()

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
            readcsv[courier_index]['Number'] = phone_number
            print("[bold green]Courier number has been updated[/bold green]")
    else:
        print("[bold red]Courier number not updated[/bold red]")
    write_courier_csv(readcsv)

def backup_file():
    # Create a backup of the original file
    shutil.copy('courier_list.csv', 'courier_backup.csv')

def restore_file():
    # Restore the file from the backup
    shutil.copy('courier_backup.csv', 'courier_list.csv')

def test_update_input_blank():
    backup_file()
    update_input_blank()

    expected = {"Courier Name" : 'Eat Good', "Driver Name" : 'Jack', "Phone Number" : '07985739021' }
    actual = read_only_courier()[0]

    assert actual == expected, f"Test failed: expected '{expected}', got '{actual}'"
    restore_file()

""" 8. Test phone number is digits only  """

""" 9. Test phone number is 11 only  """



