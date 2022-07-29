from modules.conn import Conection
from modules.date import *
from tkinter import messagebox

class Save():
    """Save class is for save registers and items. needs a conection to work
    1) save_register : recieves item,amount,obs   and execute the qery to insert data in DB
    2) save_idem     : recieves item  and execute the qery to insert data in DB. show a messagebox witg confirmation
    both methods close the conection.

    ********** en save_item pongo el Try y el except por si falla... no en el save_register... 
                faltaria mejorarlo para capturar bien el error, y no que sea general
    """

    def save_register(self,item,amount,obs):
        conection = Conection().conection()
        conection[1].execute('INSERT INTO register VALUES (%s,%s,%s,%s,%s)',(None,item,amount,Date().today_eng(),obs))
        conection[0].commit()
        conection[0].close()

    def save_item(self,item):
        try:
            conection = Conection().conection()
            conection[1].execute('INSERT INTO items VALUES (%s,%s)',(None,item))
            conection[0].commit() 
            conection[0].close()
            messagebox.showinfo(title='Agregar Categoria',message=f'Categoria {item} agregada con exito!')
        except:
            messagebox.showerror(title='Error',message='Error inesperado...')

