import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week5') 

from modules.product_menu_module \
import drinks_list

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

        print('Inserting new record...')
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
            print("NOT UPDATED: Item already exists")


    print('Committing...')
    connection.commit()
    
except Exception as ex:
    print('Failed to:', ex)



        



