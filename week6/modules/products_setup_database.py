import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week6') 

from modules.product_menu_module \
import drinks_list, food_list

import psycopg2 as psycopg
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
print("Host from env:", os.getenv("POSTGRES_HOST"))
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:
    print("Opening connection....")

    # Establishing a connection 
    with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()

        print('Inserting new drink...')
        # Code here to insert a new record (use RETURNING)
        sql = """
                INSERT INTO drinks_list (name, price)
                VALUES (%s, %s)
                RETURNING drink_id, name, price"""
        
        for drinks in drinks_list:
            name = drinks["Name"]
            price = drinks["Price"]
            data_values = (name, price)
        
            # Give me any row where the name matches this exact value.”
            cursor.execute("SELECT name FROM drinks_list WHERE name = %s;", (name,))
            name_exists = cursor.fetchone()

            if not name_exists:
                cursor.execute(sql, data_values)
                inserted_row = cursor.fetchone()
                print('insert result id = ', inserted_row)
            else:
                print(f"{name} not update, Items already exists")



        print('Inserting new food...')
        # Code here to insert a new record (use RETURNING)
        sql = """
                INSERT INTO food_list (name, price)
                VALUES (%s, %s)
                RETURNING food_id, name, price"""
        
        for food in food_list:
            name = food["Name"]
            price = food["Price"]
            food_data_values = (name, price)
        
            # Give me any row where the name matches this exact value.”
            cursor.execute("SELECT name FROM food_list WHERE name = %s;", (name,))
            name_exists = cursor.fetchone()

            if not name_exists:
                cursor.execute(sql, food_data_values)
                inserted_row = cursor.fetchone()
                print('insert result id = ', inserted_row)
            else:
                print(f"{name} not update, Items already exists")
  


  

    print('Committing...')
    connection.commit()

    print('Selecting all drink records...')
    # Select all the records
    cursor.execute('SELECT drink_id, name, price FROM drinks_list')
    drinks_rows = cursor.fetchall()
    print(drinks_rows)

    print('Selecting all food records...')
    # Select all the records
    cursor.execute('SELECT food_id, name, price FROM food_list')
    food_rows = cursor.fetchall()
    print(food_rows)



    print('Displaying all records...')
    # Print out all the records
    for row in drinks_rows:
        print(f'Drink ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    print('Displaying all records...')
    # Print out all the records
    for row in food_rows:
        print(f'Food ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')


    print('Closing cursor...')
    # Close the cursor
    cursor.close()
    
except Exception as ex:
    print('Failed to:', ex)



        



