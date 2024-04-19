import psycopg2

def insert_data(sep_length, sep_width, pet_length, pet_width, result):
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user="postgres",
            password="12345678",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        sql = """INSERT INTO public."IRIS_table" (sepal_length, sepal_width, petal_length, petal_width, result)
                 VALUES (%s, %s, %s, %s, %s);"""
        
        # Convert the result parameter to a list to represent an array value
        values = (sep_length, sep_width, pet_length, pet_width, result)
        
        cur.execute(sql, values)
        
        conn.commit()
        print("Data inserted successfully!")
        
    except psycopg2.Error as e:
        print("Error inserting data into PostgreSQL:", e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
