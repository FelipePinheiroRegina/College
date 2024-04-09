import psycopg2

connect = psycopg2.connect( database = "postgres", 
                            user     = "postgres", 
                            password = "1", 
                            host     = "127.0.0.1", 
                            port     = "5432")
cursor = connect.cursor()
print('connect success')

cursor.execute('''CREATE TABLE products(
                                        id INT NOT NULL PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        price REAL NOT NULL);''')
print('Create table with success!')
connect.commit()

cursor.close()
connect.close()