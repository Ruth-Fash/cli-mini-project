import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation') 
import csv
from rich.console import Console
console = Console()


# Function to print all menus and lists given input where menu is stated
def display(menu):
    for index, options in enumerate(menu):
        print(f"{index}:  {options}")


# While loop to return to a menu (product, courier or order).
def return_to_submenu(submenu):
    while True:
        try:
            if return_answer() == 0:
                break
            else:
                console.print(f"[bold red]Invalid input. Please enter 0 to return to the {submenu} menu.[/bold red]")
        except ValueError:
            console.print(f"[bold red]Invalid input. Please enter 0 to return to the {submenu} menu.[/bold red]")

# Input to return to a menu (product, courier or order). If enter 0 will send back. Relates back to to above function.
def return_answer():
    return int(console.input("[bold]ENTER 0 TO RETUN TO THE PREVIOUS MENU\t[/bold]"))


# Input to for user option to delete another product/courier/order
def delete_another():
    return console.input("[bold]Would you like to delete another? (y/n)\t[/bold]").lower() # if the anser noes not = y, so is n. then should continue as normal if, is y then will loop back unitil answer does not = y

# Input to for user option to add another product/courier/order
def add_another():
    return console.input("[bold]Would you like to add another? (y/n)\t[/bold]").lower()


# Clears the screen as you naviagate through the app
def clear_screen():
    print("\033c", end="")













