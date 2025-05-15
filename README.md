# ruths-mini-project

## Project Background

The aim of this project was to create a ****CLI application** for a client to** **track and log orders** . Each week, we were introduced to new topics and had to implement them to enhance the app, expanding on previous requirements.

## Weekly Progress and Implementation

#### Week 1 – Fundementals

We covered basic concepts such as **operators, user inputs, lists, and if/else statements** . This formed the foundation of the project, where I:

* Created **lists** to store products, couriers, and orders.
* Allowed users to **view, add, update, and delete** items from these lists.
* Used **input** to allow user to input information

#### Week 2 – Loops, Dictionaries & Functions

This week, we learned about **loops, dictionaries, exception handling, functions, modules, and packages** . The key focus the mini project that week was on **dictionaries** , especially for orders, as each order contained multiple pieces of information (e.g., customer name, address, and phone number).

* I transitioned from using lists to **dictionaries** for orders.
* Updated my methods to match **dictionary mutations** (e.g., updating nested values within an order).
* Started using **functions** to avoid redundant code.

#### Week 3 – Data Persistence & Encoding

This week introduced **data persistence** , allowing the app to store data beyond a single session. My focus was:

* Writing **lists and dictionaries to a text file** .
* Ensuring that any changes (additions, updates, or deletions) were **saved to and loaded from the text file** .
* Creating functions to handle **read/write operations** , keeping the code clean and structured.

#### Week 4 – Transition to CSV & Improving Navigation

I switched from using a ****text file** to a** **CSV file** , as products, orders, and couriers would now need to stored in dictionaries.  I focused on this, aswell as other components that i had not implemented into my code yet:

* Updating all **file handling logic** to read from and write to CSVs.
* Improving app ****navigation** using** **`while` loops, ensuring users could** **return to the main menu and naviate else where from there.**
* Adding **better exception handling** to manage user input errors and unexpected issues.

#### Week 5 – Code Refactoring & Modules

After completing a **peer assessment** , I received feedback on improving code readability and organisation. My focus this week was:

* **Splitting code into modules** for better structure (e.g., separate files for products, orders, couriers, and functions).
* Moving large chunks of code into **relevant functions** within their respective modules.
* Enhancing **user-friendliness** by making the app easier to navigate and maintain.

#### Week 6 – Unit Testing and Refactoring

* The focus was working on my unit testing and refactoring any potential errors that may arise

## Client Requirement

A pop-up café requires an application to help track and log orders.

The application should be a ****command-line interface (CLI)** that is** **easy to navigate** , displaying menus and options for seamless interaction whilst using the app

App should allow them to store products they sell, couriers they use to deliver , and log orders made by customers. Each with its own sub-menu (products, courier, orders).

Users can **add, update, and delete** entries in each sub-menu (e.g., create a new order, update an order’s status, or remove a courier).

The app should provide navigation options to **return to the main menu** from **any sub-menu and** **exit** when needed.

All data need to be **persisted** upon exit, ensuring no changes are lost. When the app starts, it should display the most up-to-date information.

The app should be tested. The application should include **error handling** to ensure smooth operation.

The functionality will be **tested** to confirm the app works as expected and handles potential errors effectively.

## User Guide

All folders and app can be found in the week 4 folder in my repositary

#### Modules

- **`orders.py`** – Handles order-related functions (adding, updating, deleting orders), interacts with `orders_list.csv`
- **`couriers.py`** – Handles order-related functions (adding, updating, deleting orders), interacts with `courier_list.csv`
- **`drink.py`** – Handles order-related functions (adding, updating, deleting orders), interacts with `drinks_list.csv`
- **`food.py`** – Handles order-related functions (adding, updating, deleting orders), interacts with `food_list.csv`
- **`functions.py`** – Handles general functions.

#### Files

This project relies on CSV files to store and retrieve data. Ensure the following files are in the project directory before running the app:

- `drinks_list.csv` – Stores a list of dictionaries. Each containing drink names and their prices
- `food_list.csv` – Stores a list of dictionaries. Each containing food names and their prices
- `courier_list.csv` – Stores a list of dictionaries. Each containing courier company, drivers name and phone number
- `order_list.csv` –Stores a list of dictionaries. Each containing customer name, address, phone number, courier indes, order status, drink index and food index.

#### How to run the app

The app starts with the main menu:

A prompt appears to enter a valid number from the available options (selction from 0. Exit App; 1. Products, 2. Couriers, 3. Orders).

0. **Exit app** - This option will shut the programme down, before shutting down it will read the data from the 3 sub-menus (products, orders and couriers).
1. **Products**
   Contains all options related to the products sold at the cafe.
   A prompt appears to enter a valid number from the options avaibale to navigate to them.

   0. Return to main menu - this will direct back to the the main menu
   1. Drinks - This will list the most up to date available drinks and prices on the menu. Reading from the drinks csv file
   2. Food - This will list the most up to date available food and prices on the menu. Reading from the food csv file
   3. Add New Drink - This allows you to add a new drink and it's price to the drinks list. A prompt requesting the new name and price will appear. Both must be filled in. This will be added and saved to the bottom of the csv, permenately updating it.
   4. Add New Food - This allows you to add a new food and it's price to the food list. A prompt requesting the new name and price will appear. Both must be filled in. This will be added and saved to the bottom of the csv, permenately updating it.
   5. Update exisiting drink  - A prompt for the drink you want to update will appear. This allows you to enter the updated name and/or price of a drink already in the list (i.e. in case of errors when orginally added, or update in name/pricing ). Given a valid index is selected, this will update the name and /or price into the csv for the selected index, or leaving as the orginal if input is left blank.
   6. Update exisiting food  - A prompt for the food you want to update will appear. This allows you to enter the updated name and/or price of a food already in the list (i.e. in case of errors when orginally added, or update in name/pricing ). Given a valid index selected, This will update the name and /or price into the csv for the selected index, or leaving as the orginal if input is left blank.
   7. Remove drink - Allows you to delete a drink from the current drinks selection. A prompt requesting you to enter you chosen index will appear. Given a valid index is selected this will be permenately removed from the csv file.
   8. Remove food - Allows you to delete a food from the current drinks selection. A prompt requesting you to enter you chosen index will appear. Given a valid index is selected this will be permenately removed from the csv file.
2. **Courier**

   Contains all options related to the couriers.
   A prompt appears to enter a valid number from the options available to navigate to them.

   0. Return to main menu - Refer to **Product 1.0**
   1. Courier - This will list the most up to date information on the courier.
   2. Add New Courier - This allows you to add a new courier to the list. When prompted you must enter information relating to the courier company name, drivers name and phone number. All information must be filled in.
   3. Update Exisiting Courier - To update the information of an exisiting courier. When prompted you must enter a valid index of the courier you wish to update. A prompt for courier company name, drivers name and phone number will appear. If you wish to update the prompted info you should fill it in, if not please leve blank and it will remain as the orginal.
   4. Delete Courier - To permenatly delete an exisitng courier. A prompt for the couriers index you want to remove will appear. Given a valid index is selected the order information relating to that index will be permently deleted.
3. **Orders**

   Contains all options related to the Orders.
   A prompt appears to enter a valid number from the options available to navigate to them.

   0. Return to main menu - Refer to **Product** **1.0**
   1. Print Orders Dictionary - This will list the most up to date order information. including customer info, courier info. Reading from the orders_list csv file
   2. Create a New order - This allows you to add a new order to the order list. When prompted, you will be expected to enter information on customer info (i.e name, address, number ), enter a courier from the courier list and ordered items from drinks and/or food list. The order status will be automatically filled as "Preparing" as a default, with the assumption that the order is being prepared at that point (If this is not the case, you will have the oppurtinty to amend order status at point **2.3**)All information must be filled in. This will be added and saved to the bottom of the csv, permenately updating it.
   3. Update Customer Order Status - To update the status of an exisiting order. You must enter a valid index of the order you wish to update, when prompt appears and enter the index of the status you wish to amend it to. New info will be permentaely re-written in to the csv.
   4. Update Customer Order Infromation - To update any other information about an exisiting order. A prompt for the order index you want to update will appear. Given a valid index is selected, a prompt for customer, courtier and order info will appear. If you wish to update the prompted info you should fill it in, if not please leve blank and it will remain as the orginal.
   5. Delete Order - To permenatly delete an exisitng order. A prompt for the order index you want to remove will appear. Given a valid index is selected the order information relating to that index will be permently deleted.

## How to run any unit tests

1. Make sure pytest has been installed and is running
2. There a 3 main test i have ran with the 'unit_test' folder - 'test_products.py', 'test_order.py' and test_courier.py'
3. Load one of the files and run 'pytest - v <file_name>.py'. For example to run test_product.py use 'pytest -v test_courier.py
4. Some tests have **amendable inputs** that allow you to easily test different scenarios. These are clearly indicated in the test files. You can change the values of these inputs at the top of the test files to try out different conditions and validate different outcomes.

## Project reflections

**How did your design go about meeting the project's requirements?**

* **Command-Line Interface (CLI)** : I designed the app to function through a user-friendly CLI, which was simple to navigate. Each section (products, couriers, and orders) had its own sub-menu, providing a straightforward way to manage different parts of the system.
* **Modular Structure** : I split the application into separate modules based on functionality (e.g., product management, order management, courier management), making it easier to maintain and extend. Each module had clearly defined responsibilities (e.g., handling products, adding new orders, managing courier data).
* **Data manipulation** : I ensured that users could easily  ***add** , ***update** , and**  **delete** entries in each of the sub-menus. This functionality was implemented for products, couriers, and orders. For example, users could add a new order, update the order status, or remove a product from the menu.
* **Navigation Options** : I added navigation options within the app to ensure that users could easily return to the main menu from any sub-menu and exit the application when needed.
* **Data Persistence** : I implemented persistent storage using CSV files so that when the app exits, all data is saved. When the app is restarted, it loads the most up-to-date information from these files, ensuring no data is lost between sessions.
* **Error Handling** : I incorporated error handling to ensure smooth operation. For example, when a user tries to update an order with an invalid index, an error message is displayed instead of the app crashing.
* **Testing** : I wrote unit tests for various functionalities to ensure that the app works as expected. This included testing data manipulation operations, data persistence, and cases, such as entering invalid input.

**How did you guarantee the project's requirements?**

To guarantee that the project met the requirements, I took the following steps:

1. **Clear Requirements Breakdown** : I started by breaking down the client requirements into actionable tasks. This allowed me to identify the core functionalities (e.g., managing orders, handling courier data, ensuring data persistence) and ensure each was tackled independently.
2. **Regular Code Refactoring** : I regularly refactored my code to improve readability and maintainability. This was particularly important as I added new features to ensure that the app would remain scalable and organided.
3. **User-Focused Design** : I kept the user in mind at every stage of development. This meant designing a simple and intuitive CLI, ensuring that users would be able to interact with the app without confusion.
4. **Non-TDD Testing Approach:** Instead of writing tests before implementation, I developed the features first and then created unit tests to validate their functionality. These tests ensured that key features worked correctly, covering edge cases such as handling invalid data or incorrect user input.
5. **Automated Testing** : I used automated testing (via tools like `pytest`) to ensure that the app's functionality remained intact as I made changes or added new features. This helped catch potential issues early and maintain stability across releases.

**If you had more time, what is one thing you would improve upon?**

If I had more time, I would have worked on integrating a database, specifically PostgreSQL, into my application. While the current implementation relies on CSV files for data persistence, using a relational database like PostgreSQL would offer better scalability and management of the data over time. I would be able to easily manage data for products, orders, and couriers in a structured way, making it more robust and easier to maintain.

If I had more time, I would have planned the project better. I feel that my approach was quite chaotic, and I needed a clearer structure. I would have worked on improving the readability of my code. I would have made sure to break down larger functions into smaller, more manageable ones, and added more meaningful comments

**What did you most enjoy implementing?**

I think what I enjoyed most was tackling the things that weren’t working. Although it was frustrating at first, I later realised how much I learned from those challenges, particularly the importance of error handling.
