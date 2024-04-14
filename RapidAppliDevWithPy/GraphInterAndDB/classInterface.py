import tkinter as tk
from tkinter import ttk
import classAppDb as crud

class InterfaceDB():
    def __init__(self, win):
        self.objDB = crud.AppDB()
        self.lbId = tk.Label(win, text='Id of Product: ')
        self.lbName = tk.Label(win, text='Name of Product: ')
        self.lbPrice = tk.Label(win, text='Price of Product: ')

        self.txtId = tk.Entry(bd=3)
        self.txtName = tk.Entry()
        self.txtPrice = tk.Entry()

        self.buttonCadaster = tk.Button(win, text='Cadaster', command=self.fCadasterProduct)
        self.buttonUpdate = tk.Button(win, text='Update', command=self.fUpdateProduct)
        self.buttonExclude = tk.Button(win, text='Exclude', command=self.fRemoveProduct)
        self.buttonClear = tk.Button(win, text='Clear', command=self.fClearScreen)

        self.DataColumn = ('Id', 'Name', 'Price')
        self.treeProducts = ttk.Treeview(win, columns=self.DataColumn, selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeProducts.yview)

        self.verscrlbar.pack(side='right', fill='y')
        self.treeProducts.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProducts.heading('Id', text='Id')
        self.treeProducts.heading('Name', text='Name')
        self.treeProducts.heading('Price', text='Price')

        self.treeProducts.column('Id', minwidth=0, width=100)
        self.treeProducts.column('Name', minwidth=0, width=100)
        self.treeProducts.column('Price', minwidth=0, width=100)

        self.treeProducts.pack(padx=10, pady=10)

        self.treeProducts.bind('<<TreeViewSelect>>', self.PresentSelectedProducts)

        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)

        self.lbName.place(x=100, y=100)
        self.txtName.place(x=250, y=100)

        self.lbPrice.place(x=100, y=150)
        self.txtPrice.place(x=250, y=150)

        self.buttonCadaster.place(x=100, y=200)
        self.buttonUpdate.place(x=200, y=200)
        self.buttonExclude.place(x=300, y=200)
        self.buttonClear.place(x=400, y=200)

        self.treeProducts.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)
        self.LoadDataBegin()

    def PresentSelectedProducts(self, event):
        self.fClearScreen()
        for selection in self.treeProducts.selection():
            item = self.treeProducts.item(selection)
            id, name, price = item['values'][0:3]
            self.txtId.insert(0, id)
            self.txtName.insert(0, name)
            self.txtPrice.insert(0, price)

    def LoadDataBegin(self):
        try:
            self.iid = 0
            registers = self.objDB.selectProducts()
            print('DATA AVAILABLE IN THE DATABASE')
            for item in registers:
                id, name, price = item[0], item[1], item[2]
                print('id =', id)
                print('name =', name)
                print('price =', price, '\n')

                self.treeProducts.insert('', 'end', iid=self.iid, values=(id, name, price))

                self.iid += 1
            print('Data in the base')
        except Exception as e:
            print('Error while loading data:', e)

    def fReadFields(self):
        try:
            print('DATA AVAILABLE')
            id = int(self.txtId.get())
            print('id', id)
            name = self.txtName.get()
            print('name', name)
            price = float(self.txtPrice.get())
            print('price', price)
            print('Reading of the data with success')
            return id, name, price
        except Exception as e:
            print('Error reading data:', e)
            return None, None, None

    def fCadasterProduct(self):
        try:
            print('DATA AVAILABLE')
            id, name, price = self.fReadFields()
            if id is not None and name is not None and price is not None:
                self.objDB.insertProducts(id, name, price)
                self.treeProducts.insert('', 'end', iid=self.iid, values=(id, name, price))

                self.iid += 1
                self.fClearScreen()
                print('Products casted with success')
        except Exception as e:
            print('Unable to cadaster:', e)

    def fUpdateProduct(self):
        try:
            print('DATA AVAILABLE')
            id, name, price = self.fReadFields()
            if id is not None and name is not None and price is not None:
                self.objDB.updateProducts(id, name, price)

                self.treeProducts.delete(*self.treeProducts.get_children())
                self.LoadDataBegin()
                self.fClearScreen()
                print('Product updated with success')
        except Exception as e:
            print('Unable to update:', e)

    def fRemoveProduct(self):
        try:
            print('DATA AVAILABLE')
            id, _, _ = self.fReadFields()
            if id is not None:
                self.objDB.deleteProduct(id)

                self.treeProducts.delete(*self.treeProducts.get_children())
                self.LoadDataBegin()
                self.fClearScreen()
                print('Product removed with success')
        except Exception as e:
            print('Unable to remove product:', e)

    def fClearScreen(self):
        try:
            print('DATA AVAILABLE')
            self.txtId.delete(0, tk.END)
            self.txtName.delete(0, tk.END)
            self.txtPrice.delete(0, tk.END)
            print('Fields cleaning')
        except:
            print('Unable clear fields')

window = tk.Tk()
main = InterfaceDB(window)
window.title("Welcome to the Pinheiro's DataBase Application")
window.geometry("820x600+10+10")
window.mainloop()