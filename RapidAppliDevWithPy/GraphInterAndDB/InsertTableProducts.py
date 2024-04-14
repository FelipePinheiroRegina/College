import psycopg2

connect = psycopg2.connect(database = 'postgres',
                           user     = 'postgres',
                           password = '1',
                           host     = '127.0.0.1',
                           port     = '5432')
cursor = connect.cursor()

cursor.execute('''INSERT INTO products(id, name, price) VALUES(60, 'Product_60', 260.00);''')
print('Insert data success!')

connect.commit()

cursor.close()
connect.close()