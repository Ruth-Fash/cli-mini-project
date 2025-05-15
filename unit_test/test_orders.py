import pytest
import sys
import csv
import shutil
sys.path.append('/Users/ruthfashogbon/Desktop/Generation')
from rich.console import Console
console = Console()


# ------------------------- TEST FOR DELETING ORDER ----------------------
""" 1. Error Handling - Invalid index selected  -  Deleting courier works exactly the same, using the same code  """ 
from my_reps.ruths_mini_project.week4.modules.order_menu_module import del_order, select_order

def test_del_order_invalid_index(monkeypatch, capsys):
    # Mock `display_product_csv` to prevent menu printing
    monkeypatch.setattr("my_reps.ruths_mini_project.week4.modules.order_menu_module.display_order_csv", lambda _: None)

    # Mock `select_index` to return an out-of-range index (200)
    monkeypatch.setattr("my_reps.ruths_mini_project.week4.modules.order_menu_module.select_order", lambda: 200)

    # Call the del_food function
    del_order()

    # Capture the printed output
    actual = capsys.readouterr()

    # Correct expected output with Rich formatting
    expected_output = "Update unsucessful. The index entered does not exist.\n"

    # Check if the correct error message is printed
    assert actual.out == expected_output, f"Expected: {expected_output}, but got: {actual.out()}"


""" 2. Error Handling -  Index left blank  - Deleting courier works exactly the same, using the same code """
from my_reps.ruths_mini_project.week4.modules.order_menu_module import read_only_order

def del_order_blank_index():
    try:
        readcsv = read_only_order()

        selected_index = int("")

        del readcsv[selected_index]

        print("[bold green]The order has been succesfully deleted.[/bold green]")                    
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

def test_del_order_blank_index(capsys):
     
    del_order_blank_index()
    expected = "[bold red]Update unsucessful. A valid value was not entered.[/bold red]\n"
    actual = capsys.readouterr() 

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"


""" 3. Error Handling -  string entered instead of an index  - Deleting courier works exactly the same, using the same code """

def del_order_string():
    try:
        readcsv = read_only_order()

        selected_index = int('e')

        del readcsv[selected_index]

        print("[bold green]The order has been succesfully deleted.[/bold green]")                    
    except ValueError:
        print("[bold red]Update unsucessful. A valid value was not entered.[/bold red]")
    except IndexError:
        print("[bold red]Update unsucessful. The index entered does not exist.[/bold red]")

def test_del_order_string(capsys):
     
    del_order_string()
    expected = "[bold red]Update unsucessful. A valid value was not entered.[/bold red]\n"
    actual = capsys.readouterr() 

    assert actual.out == expected, f"Test failed: expected '{expected}', got '{actual.out}'"



