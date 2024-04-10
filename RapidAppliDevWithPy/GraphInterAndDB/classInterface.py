import tkinter as tk
from tkinter import ttk
import classAppDb as crud

class InterfaceDB():
    def __init__(self, win):
        self.objDB   = crud.AppDB()
        self.lbId    = tk.Label(win, text = 'Id of Product: ')
        self.lbName  = tk.Label(win, text = 'Name of Product: ')
        self.lbPrice = tk.Label(win, text = 'Price of Product: ')


        self.txtId  = tk.Entry (bd = 3)
        self.txtName  = tk.Entry()
        self.txtPrice = tk.Entry()
        
        self.buttonCadaster = tk.Button(win, text = 'Cadaster', command = 'self.fCadasterProduct')
        self.buttonUpdate   = tk.Button(win, text = 'Update'  , command = 'self.fUpdateProduct')
        self.buttonExclude  = tk.Button(win, text = 'Exclude' , command = 'self.fExcludeProduct')
        self.buttonClear    = tk.Button(win, text = 'Cadaster', command = 'self.fClearScreen')

        self.DataColumn = ('Id', 'Name', 'Price')

        self.treeProducts = ttk.Scrollbar(win, orient = 'vertical', command = self.treeProducts.yview)

        self.verscrlbar.pack(side = 'right', fill = 'x')
        self.treeProducts.configure(yscrollcommand = self.verscrlbar.set)

        self.treeProducts.heading('Id',    text = 'Id')
        self.treeProducts.heading('Name',  text = 'Name')
        self.treeProducts.heading('Price', text = 'Price')

        self.treeProducts.column('Id',    minwidth = 0, width = 100)
        self.treeProducts.column('Name',  minwidth = 0, width = 100)
        self.treeProducts.column('Price', minwidth = 0, width = 100)

        self.treeProducts.pack(padx = 10, pady = 10)

        self.treeProducts.bind('<<TreeViewSelect>>', self.PresentSelectedProducts)

        self.lbId.place( x = 100, y = 50)
        self.txtId.place(x = 250, y = 50)

        self.lbName.place( x = 100, y = 100)
        self.txtName.place(x = 250, y = 100) 

        self.lbPrice.place( x = 100, y = 150) 
        self.txtPrice.place(x = 250, y = 150) 
        
        self.buttonCadaster.place(x = 100, y = 200)
        self.buttonUpdate.place(  x = 200, y = 200)  
        self.buttonExclude.place( x = 300, y = 200)  
        self.buttonClear.place(   x = 400, y = 200)   

        self.treeProducts.place(x = 100, y = 300)
        self.verscrlbar.place(x = 805, y = 300, height = 225)
        self.LoadDataBegin()
    
    def PresentSelectedProducts(self, event):
        self.fClearScreen()
        for selection in self.treeProducts.selection():
            item = self.treeProducts.item(selection())
            id, name, price = item['values'] [0:3]
            self.txtId.insert(0, id)
            self.txtName.insert(0, name)
            self.txtPrice.insert(0, price)
    
    def LoadDataBegin(self):