import psycopg2

class AppDB:
    def __init__(self):
        print('Method constructor')

    def openConnect(self):
        try:
            connect = psycopg2.connect(database="postgres", 
                                       user="postgres", 
                                       password="1", 
                                       host="127.0.0.1", 
                                       port="5432")
            return connect
        except (Exception, psycopg2.Error) as error:
            print('connect failed')
            return None

    def selectProducts(self):
        try:
            conn = self.openConnect()
            if conn is not None:
                cursor = conn.cursor()
                querySelectAllProducts = '''SELECT * FROM products;'''
                cursor.execute(querySelectAllProducts)
                registers = cursor.fetchall()
                print(registers)
                cursor.close()
                conn.close()
                print('connection closed')
                return registers
            else:
                print("Connection failed.")
                return []
        except (Exception, psycopg2.Error) as error:
            print('Error select from products', error)
            return []

    def insertProducts(self, id, name, price):
        try:
            conn = self.openConnect()
            if conn is not None:
                cursor = conn.cursor()
                queryInsertOneProduct = '''INSERT INTO products(id, name, price) VALUES(%s, %s, %s);'''
                product = (id, name, price)
                cursor.execute(queryInsertOneProduct, product)
                conn.commit()
                count = cursor.rowcount
                print(count, 'Product inserted with success in the table products')
                cursor.close()
                conn.close()
                print('Connection closed')
            else:
                print("Connection failed.")
        except (Exception, psycopg2.Error) as error:
            print('Error insert in the table products', error)

    def updateProducts(self, id, name, price):
        try:
            conn = self.openConnect()
            if conn is not None:
                cursor = conn.cursor()
                print('Before update')
                querySelectProduct = '''SELECT * FROM products WHERE "id" = %s;'''
                cursor.execute(querySelectProduct, (id,))
                record = cursor.fetchone()
                print(record)
                queryUpdateProduct = '''UPDATE products SET "name" = %s, "price" = %s WHERE "id" = %s;'''
                cursor.execute(queryUpdateProduct, (name, price, id))
                conn.commit()
                count = cursor.rowcount
                print(count, 'Register Update success')
                print('After update')
                querySelectProduct = '''SELECT * FROM products WHERE "id" = %s;'''
                cursor.execute(querySelectProduct, (id,))
                record = cursor.fetchone()
                cursor.close()
                conn.close()
                print('Connection closed')
            else:
                print("Connection failed.")
        except (Exception, psycopg2.Error) as error:
            print('Error update products', error)

    def deleteProduct(self, id):
        try:
            conn = self.openConnect()
            if conn is not None:
                cursor = conn.cursor()
                queryDeleteProduct = '''DELETE FROM products WHERE "id" = %s;'''
                cursor.execute(queryDeleteProduct, (id,))
                conn.commit()
                count = cursor.rowcount
                print(count, 'Product deleted success')
                cursor.close()
                conn.close()
                print('Connection closed')
            else:
                print("Connection failed.")
        except (Exception, psycopg2.Error) as error:
            print('Error delete product', error)
