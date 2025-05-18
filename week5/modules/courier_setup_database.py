import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week5') 

from modules.courier_menu_module \
import courier_list

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

        print('Inserting new courier...')
        # Code here to insert a new record (use RETURNING)
        sql = """
                INSERT INTO courier_list (courier_name, driver_name, phone_number )
                VALUES (%s, %s, %s)
                RETURNING courier_id, courier_name, driver_name, phone_number"""
        
        for courier in courier_list:
            courier_name = courier["Courier Name"]
            driver_name = courier["Driver Name"]
            phone_number = courier["Phone Number"]
            data_values = (courier_name, driver_name, phone_number)
        
            # Give me any row where the name matches this exact value.”
            cursor.execute("SELECT phone_number FROM courier_list WHERE phone_number = %s;", (phone_number,))
            number_exists = cursor.fetchone()

            if not number_exists:
                cursor.execute(sql, data_values)
                inserted_row = cursor.fetchone()
                print('insert result id = ', inserted_row)
            else:
                print(f"{courier_name},{driver_name},{phone_number},not update, Items already exists")

        print('Committing...')
        connection.commit()

        print('Selecting all courier records...')
        # Select all the records
        cursor.execute('SELECT courier_id, courier_name, driver_name, phone_number FROM courier_list')
        courier_rows = cursor.fetchall()
        print(courier_rows)

        for row in courier_rows:
            print (f"Courier ID: {row[0]}, Courier Name: {row[1]}, Driver Name: {row[2]}, Phone Number: {row[3]}")





    print('Closing cursor...')
    # Close the cursor
    cursor.close()
    
except Exception as ex:
    print('Failed to:', ex)
