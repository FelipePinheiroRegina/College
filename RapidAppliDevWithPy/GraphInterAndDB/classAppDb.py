import psycopg2


class AppDB:
    def __init__(self):
        print('Method constructor')

        # TRY CONNECTING
        def openConnect(self):
            try:
              self.connect = psycopg2.connect( database = "postgres", 
                                               user     = "postgres", 
                                               password = "1", 
                                               host     = "127.0.0.1", 
                                               port     = "5432")
            except (Exception, psycopg2.Error) as error:
                if(self.connect):
                    print('connect failed')
        
        # SELECT PRODUCTS
        def selectProducts(self):
            try:
                self.openConnect()
                cursor = self.connect.cursor()

                querySelectAllProducts = '''SELECT * FROM products;'''

                cursor.execute(querySelectAllProducts)
                registers = cursor.fetchall()
                print(registers)
            
            except (Exception, psycopg2.Error) as error:
                print('Error select from products', error)
            
            finally:
                if (self.connect):
                    cursor.close()
                    self.connect.close()
                    print('connection closed')
            return registers
        
        # INSERT PRODUCTS
        def insertProducts(self, id, name, price):
            try:
                self.openConnect()
                cursor = self.connect.cursor()

                queryInsertOneProduct = '''INSERT INTO products(id, name, price) VALUES(%s, %s, %s);'''
                product = (id, name, price)
                cursor.execute(queryInsertOneProduct, product)
                self.connect.commit()
                count = cursor.rowcount
                print(count, 'Product inserted with success in the table products')
            
            except (Exception, psycopg2.Error) as error:
                print('Error insert in the table products', error)
            
            finally:
                if (self.connect):
                    cursor.close()
                    self.connect.close()
                    print('Connection closed')

        # UPDATE PRODUCTS
        def updateProducts(self, id, name, price):
            try:
                self.openConnect()
                cursor = self.connect.cursor()
                
                print('Before update')
                querySelectProduct = '''SELECT * FROM products WHERE "id" = %s;'''
                cursor.execute(querySelectProduct, (id,))
                record = cursor.fetchone()
                print(record)

                queryUpdateProduct = '''UPDATE products SET "name" = %s', "price" = %s WHERE "id" = %s;'''
                cursor.execute(queryUpdateProduct, (name, price, id))
                self.connect.commit()
                count = cursor.rowcount
                print(count, 'Register Update success')

                print('After update')
                querySelectProduct = '''SELECT * FROM products WHERE "id" = %s;'''
                cursor.execute(querySelectProduct, (id,))
                record = cursor.fetchone()
            
            except (Exception, psycopg2.Error) as error:
                print('Error update products', error)
            
            finally:
                if (self.connect):
                    cursor.close()
                    self.connect.close()
                    print('Connection closed')
        
        # DELETE PRODUCTS
        def deleteProduct(self, id):
            try:
                self.openConnect()
                cursor = self.connect.cursor()

                queryDeleteProduct = '''DELETE FROM products WHERE "id" = %s;'''
                cursor.execute(queryDeleteProduct, (id))

                self.connect.commit()
                count = cursor.rowcount
                print(count, 'Product deleted success')
            
            except (Exception, psycopg2.Error) as error:
                print('Error delete product', error)
            
            finally:
                if (self.connect):
                    cursor.close()
                    self.connect.close()
                    print('Connection closed')



