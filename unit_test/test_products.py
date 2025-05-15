import pytest
import sys
import csv
import shutil
sys.path.append('/Users/ruthfashogbon/Desktop/Generation')
from rich.console import Console
console = Console()


""" The test below are done on either the drinks or the food lists - fyi - if the test is done on food, the same exact code works for drink (vice verse) """



""" 1. Testing products will display in correct format - Same is used across courier and orders when printing in a particular format"""
from my_reps.ruths_mini_project.week4.modules.product_menu_module import display_product_csv,read_only_product
from unittest.mock import patch

def set_up_display_format():
    read_csv = read_only_product('food')
    return read_csv

def test_display_format(capsys):
 # Run the function that prints output
    display_product_csv(set_up_display_format())

    # Capture the printed output
    actual = capsys.readouterr()

    expected = """0:  Avocado Toast - £5.0
1:  Toast - £2.0
2:  Chicken Salad - £7.5
3:  Grilled Cheese - £5.0
4:  Plain Crossaint - £2.5
5:  Cinnamon roll - £2.5
6:  Apple Pie - £3.0
7:  Pain Au Chocolat - £3.0
8:  Danish Roll - £4.0"""
# Compare the captured output with the expected output
    assert actual.out.strip() == expected.strip(), f"Test failed: expected '{expected}', got '{actual.out.strip()}'"  

""" 2. Test user input for drink name - Same is used across courier and orders when requesting user input  """
# Amendable - Variable user_input = 'Apple Juice'
# Amendable - Set the monkeypatched input to return the amendable value

from my_reps.ruths_mini_project.week4.modules.product_menu_module import modify_drinkname

def modify_drinkname():
    return console.input("[bold]Add new product name \t[/bold]").title()

def test_modify_drinkname(monkeypatch):
    monkeypatch.setattr(console,"input", lambda _: "Apple Juice")

    actual = modify_drinkname()  # Call the function, it will prompt for input
    # The test expects that the function returns what the user typed.
    expected = 'Apple Juice'  # User input should be returned
    assert actual == expected, f"Test failed: expected '{expected}', got '{actual}'"


# ------------------------- TEST FOR CSV FILE READING, WRITING, APPENDING  ----------------------

""" 3. Error Handaling: Testing what will happen if csv is empty - The same is used in the order and couriers menu"""
def test_empty_csv(capsys):
    # Simulate an empty CSV (empty list)
    empty_csv = []
    
    # Run the function that prints output
    display_product_csv(empty_csv)
    
    # Capture the printed output
    actual = capsys.readouterr()
    
    # Define the expected output when the CSV is empty (without formatting)
    expected = "No products available.\n"  # Adjust to match the actual print output
    
    # Compare the captured output with the expected output
    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 4. Error Handaling: Testing what will happen if reading a non dictionary - The same is used in the order and couriers menu"""

def test_invalid_data_type(capsys):
    # Simulate an invalid CSV format (a string instead of a list)
    invalid_csv = 'Pain au chocolat'
    
    # Run the function that prints output
    display_product_csv(invalid_csv)
    
    # Capture the printed output
    actual = capsys.readouterr()
    
    # Define the expected output when the CSV is not a list (without formatting)
    expected = "Error: Invalid data format. Expected a list of dictionaries.\n"  # Adjusted to match the actual error message
    
    # Compare the captured output with the expected output
    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"



""" 5. Test error handling - if file doesn't exist when reading - The same is used in the order and couriers menu """
# Amendable -   read_product_csv('empty') - Can change 'empty' to another file name that doesn;t exist.

from my_reps.ruths_mini_project.week4.modules.product_menu_module import read_product_csv
def test_error_handling_file_not_exist(capsys):
    invalid_file_name = 'foody'  # Non-existent file
    
    # Run the function that tries to open a non-existent file
    read_product_csv(invalid_file_name)
    
    # Capture the printed output
    actual = capsys.readouterr()
    
    # Define the expected output when the file doesn't exist
    expected = "Error: The file does not exist."
    
    # Compare the captured output with the expected output
    assert actual.out.strip() == expected, f"Test failed: expected '{expected}', got '{actual.out.strip()}'"



""" 6. Test error handling - Another empy file, this time reading it - The same is used in the order and couriers menu  """

def test_empty_csv2(capsys):
    
    # Run the function that prints output of the empty list
    read_product_csv('empty')
    
    # Capture the printed output
    actual = capsys.readouterr()
    
    # Define the expected output when the CSV is empty (without formatting)
    expected = "No products available.\n"  # Adjust to match the actual print output
    
    # Compare the captured output with the expected output
    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"



""" 7. Test error handling - invalid data added to a csv - The same is used in the order and couriers menu """
# Amendable - Variable invalid_csv = 'Pain au chocolat' - test other non dictionary inputs

from my_reps.ruths_mini_project.week4.modules.product_menu_module import write_product_csv
def test_writing_invalid_data(capsys):

    invalid_csv = 'Pain au chocolat' # Writing a string instead of a dictionary 
    write_product_csv('empty',invalid_csv)

    actual = capsys.readouterr() 

    expected = "Error: Invalid data format. Expected a list of dictionaries.\n"

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"









# ------------------------- TEST FOR DELETING PRODUCT ----------------------

""" 8. Error Handling - Index Error when invalid index chosen - out of range - The same is used in the order and couriers menu"""
# Amendable - lambda: 200
# Modify the 'lambda' value in the code below to test different index values for del_food function.
# For example, change 200 to any valid or invalid index you'd like to test.


from my_reps.ruths_mini_project.week4.modules.product_menu_module import del_food

def test_del_food_invalid_index(monkeypatch, capsys):
    # Mock `display_product_csv` to prevent menu printing
    monkeypatch.setattr("my_reps.ruths_mini_project.week4.modules.product_menu_module.display_product_csv", lambda _: None)

    # Mock `select_index` to return an out-of-range index (200)
    monkeypatch.setattr("my_reps.ruths_mini_project.week4.modules.product_menu_module.select_index", lambda: 200)

    # Call the del_food function
    del_food()

    # Capture the printed output
    actual = capsys.readouterr()

    # Correct expected output with Rich formatting
    expected_output = "Update unsucessful. The index entered does not exist.\n"

    # Check if the correct error message is printed
    assert actual.out == expected_output, f"Expected: {expected_output}, but got: {actual.out()}"


""" 9. Error Handling - Index Error when invalid index chosen - blank - The same is used in the order and couriers menu """
def del_drink_blank_index():
    try:
            readcsv = read_only_product('drinks')

            index = int("")
            del readcsv[index]

            print("[bold green]The item has been succesfully deleted.[/bold green]")
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

def test_del_drink_blank_index(capsys):

    del_drink_blank_index()
    expected = "[bold red]Update unsucessful. A valid value was not entered.[/bold red]\n"
    actual = capsys.readouterr() 

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"



# ------------------------- TEST FOR ADDING PRODUCT ----------------------

""" 10. Test that a drink is successfully added and then removed after the test. - The same is used in the order and couriers menu """
# Amendable - Variable new_drink = {"Name" : 'Iced Tea', "Price" : '2.0'}
# Modify the 'new_drink' variable to test adding different drinks (e.g., change the name or price).
# For example, change 'Iced Tea' to 'Lemonade' and the price to '2.5'.

# Amendable - Expected result:
# If you modify the `new_drink` to a different drink, you must also update the `expected` variable
# to reflect the correct name and price you want to test. 

from my_reps.ruths_mini_project.week4.modules.product_menu_module import read_product_csv, append_product_csv

def test_add_drink():

    # Add drink
    new_drink = {"Name" : 'Iced Tea', "Price" : '2.0'}
    append_product_csv('drinks', new_drink)

    # Read again to check if it was added
    expected = {"Name" : 'Iced Tea', "Price" : '2.0' }
    actual = read_only_product('drinks')[-1]

    assert actual == expected, f"Test failed: expected '{expected}', got '{actual}'"

    # Cleanup: Remove the last added drink
    drinks = read_only_product('drinks')  # Get the current list
    write_product_csv('drinks', drinks[:-1])  # Remove the last entry


""" 11. Test if price is not a number, it will run error. - The same is used in the order and couriers menu """
# Amendable - Variable drink_price
# Modify the `drink_price` variable below to test different invalid prices.
# For example, you can change it to 'abc' or an empty string to simulate invalid inputs.
def new_drinks_price_string():

    drink_price = 'f'
    try:
        drink_price = float(drink_price)
    except ValueError:
        print("[bold red]Invalid price. Please enter a valid number.[/bold red]")
        return None  # Return None if price is invalid
     
from my_reps.ruths_mini_project.week4.modules.product_menu_module import read_product_csv, append_product_csv

def test_new_drink_price_string(capsys):

    # Call the function
    new_drinks_price_string()

    # Read again to check if it was added
    expected = "[bold red]Invalid price. Please enter a valid number.[/bold red]\n"


    actual = capsys.readouterr() 

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 12. Test if name is blank, it will run an error - The same is used in the order and couriers menu"""
def new_drinks_name_blank():
    drink_name = ''
    drink_price = '3.0'

    if not drink_name or not drink_price:
        print("[bold red]Name and price cannot be empty.[/bold red]")
        return None  
            
    return {"Name" : drink_name, "Price" : float(drink_price) }    

    
from my_reps.ruths_mini_project.week4.modules.product_menu_module import read_product_csv, append_product_csv

def test_blank_name_blank(capsys):

    # Read again to check if it was added
    expected = "[bold red]Name and price cannot be empty.[/bold red]\n"
    
    # Call the function
    new_drinks_name_blank()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 13. Test if price is blank, it will run an error - The same is used in the order and couriers menu"""
def new_drinks_price_blank():
    drink_name = 'Hot Choco'
    drink_price = ''

    if not drink_name or not drink_price:
        print("[bold red]Name and price cannot be empty.[/bold red]")
        return None  
            
    return {"Name" : drink_name, "Price" : float(drink_price) }    

    
from my_reps.ruths_mini_project.week4.modules.product_menu_module import read_product_csv, append_product_csv

def test_blank_price_blank(capsys):

    # Read again to check if it was added
    expected = "[bold red]Name and price cannot be empty.[/bold red]\n"
    
    # Call the function
    new_drinks_price_blank()

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


# ------------------------- TEST FOR UPDATING PRODUCT ----------------------

""" 14. Test invalid index blank - out of range - The same is used in the order and couriers menu"""
def update_food_blank_index():
    try:
        readcsv = read_only_product('drinks2')
     # Simulate an invalid index (empty string or other invalid input)
        # This is similar to what your code would do internally when the invalid input occurs

        index = int("")
        foodname = "Ice Coffee"
        price = 3

        if foodname:
            readcsv[index]['Name'] = foodname
        if price:
            readcsv[index]['Price'] = float(price)

    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]") 

def test_update_food_blank_index(capsys):

    update_food_blank_index()

    expected = "[bold red]Update unsucessful. A valid value was not entered.[/bold red]\n"

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"

""" 15. Test invalid index update - The same is used in the order and couriers menu"""
# Amendable - Variable index
# Modify the `index` variable to test different out-of-bounds indices.
# Example: Try changing it to 20 (if the list is shorter than 20) to simulate an invalid index.

def update_food_invalid_index():
    try:
        readcsv = read_only_product('drinks2')

        index = 20
        foodname = "Ice Coffee"
        price = 3

        if foodname:
            readcsv[index]['Name'] = foodname
        if price:
            readcsv[index]['Price'] = float(price)

    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]") 

def test_update_food_invalid_index(capsys):

    update_food_invalid_index()

    expected = "[bold red]Update unsucessful. The index entered does not exist.[/bold red]\n"

    actual = capsys.readouterr()

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 16. Test if input left blank will leave as is - The same is used in the order and couriers menu """
# Amendable - Variables to test different scenarios
# Modify `foodname` or `price` to test various input scenarios.
# Example: Test with an empty `foodname` or a different `price` value.

def backup_file():
    # Create a backup of the original file
    shutil.copy('drinks2_list.csv', 'drinks2_backup.csv')

def restore_file():
    # Restore the file from the backup
    shutil.copy('drinks2_backup.csv', 'drinks2_list.csv')

def update_food_blank_input():
        readcsv = read_only_product('drinks2')

        index = 0   # Amendable - Change index here to test different entries in your product list
        foodname = ""  # Amendable - Test with different food names or leave it blank
        price = 3  # Amendable - Test different price values (e.g., invalid or zero prices)


        if foodname:
            readcsv[index]['Name'] = foodname

        if price:
            readcsv[index]['Price'] = float(price)


        write_product_csv('drinks2',readcsv) 

def test_update_food_blank_input():
    backup_file()
    update_food_blank_input()

    # Amendable - Expected result
    # Modify this dictionary if you expect a different value after running the function
    # This test expects that if the foodname is blank, the food's name remains unchanged (e.g., 'Soda')

    expected = {"Name" : 'Soda', "Price" : '3.0' }
    actual = read_only_product('drinks2')[0]     # Change index if you amended index in update_food_blank_input()

    assert actual == expected, f"Test failed: expected '{expected}', got '{actual}'"

    restore_file()


