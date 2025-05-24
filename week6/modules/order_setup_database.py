import sys
sys.path.append('/Users/ruthfashogbon/Desktop/Generation/ruths_mini_project/week6') 

from modules.order_menu_module \
import order_dictionary

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

        print('Inserting new order...')
        # Code here to insert a new record (use RETURNING)
        sql = """
                INSERT INTO order_list (customer_name, customer_address, customer_phone, courier_index, drinks_id, food_id, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id, customer_name, customer_address, customer_phone, courier_index, drinks_id, food_id, status"""
        
        for order in order_dictionary:
            customer_name = order["Customer name"]
            customer_address = order["Customer address"]
            customer_phone = order["Customer phone"]
            # Convert the 'Courier index' string from the order into a list of integers,
            # splitting by commas and ignoring any empty entries
            courier_index = int(order["Courier index"])
            drinks_id = [int(i) for i in order['Drink index'].split(",") if i ]
            food_id = [int(i) for i in order['Food index'].split(",") if i]
            status = order["Status"]
            data_values = (customer_name, customer_address, customer_phone, courier_index, drinks_id, food_id, status)
        

            cursor.execute(sql, data_values)
            inserted_row = cursor.fetchone()
            print('insert result id = ', inserted_row)


        print('Committing...')
        connection.commit()

        print('Selecting all orders...')
        # Select all the records
        cursor.execute('SELECT id, customer_name, customer_address, customer_phone, courier_index, drinks_id, food_id, status FROM order_list')
        order_rows = cursor.fetchall()
        print(order_rows)


        print('Displaying all records...')
        # Print out all the records
        for row in order_rows:
            print(f'Order ID: {row[0]}, Customer Name: {row[1]}, Customer Address: {row[2]}, Customer Phone: {row[3]}, Courier Index: {row[4]}, Drinks ID: {row[5]}, Food ID: {row[6]}, Status: {row[7]}')


        print('Closing cursor...')
        # Close the cursor
        cursor.close()
        
except Exception as ex:
    print('Failed to:', ex)



            



