from faker import Faker
import psycopg2

connect = psycopg2.connect( database = "postgres", 
                            user     = "postgres", 
                            password = "1", 
                            host     = "127.0.0.1", 
                            port     = "5432")
cursor = connect.cursor()
print('connect success')

fake = Faker('pt_BR')

n = 10
for i in range(n):
    id = i + 10
    name = 'product_'+str(i+1)
    price = fake.pyfloat(left_digits  = 3, 
                         right_digits = 2, 
                         positive     = True, 
                         min_value    = 5, 
                         max_value    = 1000)
    query = '''INSERT INTO products(id, name, price) VALUES(%s, %s, %s)'''
    product = (id, name, price)
    cursor.execute(query, product)

connect.commit()
print('products inserts successful')

cursor.close()
connect.close()