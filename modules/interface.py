from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from modules.conn import *
from modules.register import Register
from modules.reports import Reports
from modules.save import Save
from modules.date import Date
import tkinter as tk
import sys

# Create Conection
conection = Conection()

# Create Save object
save = Save(conection=conection)


# Exit Program Function
def exit_program():
    """Use sys module to exit program
    """
    sys.exit()

# Info Program Function
def info():
    messagebox.showinfo(title='Info',message="""Colo soft, desarrollado por Andres.
    Registro y reporte de gastos por categorias.
    Gracias por curiosear la info!
    Andres""")

# InterfaceItems: Get items from DB
class InterfaceItems():
    """Returns a list of all items in DB 'items'
        Needs a Conection to DB to work...
    """
    def __init__(self,conection:Conection) -> None:
        self.conection = conection

    def get_items(self) -> list:
        self.conection.conection()
        mysql_message = """SELECT item FROM items"""
        self.conection.cursor.execute(mysql_message)
        db_data = self.conection.cursor.fetchall()
        list_of_items=[]
        for a in db_data:
            list_of_items.append(a[0])
        self.conection.conn.close()
        return list_of_items

# Class ItemWindow
class ItemWindow():
    def __init__(self) -> None:
        """create a new toplevel window with an entry box to put the name of the new item in DB
        when press the button, close the window and the new item
        """
        self.item_window = tk.Toplevel()
        self.item_window.title('Agregar nuevo Rubro')
        self.item_window.config(height=120,width=250)

        self.item_label = tk.Label(self.item_window,text='Nombre: ')
        self.item_label.place(x=10,y=10)

        self.item_entry = tk.Entry(self.item_window)
        self.item_entry.place(x=100,y=10)

        self.button_confirm = tk.Button(self.item_window,text='Agregar',command= self.add_item)
        self.button_confirm.place(x=20,y=50)

        self.button_cancel = tk.Button(self.item_window,text='Cancelar',command = self.item_window.destroy)
        self.button_cancel.place(x=100,y=50)

    def add_item(self):
        if not self.item_entry.get():
            messagebox.showerror(title='Error',message='Debe ingresar un nombre')
            return None
        response = save.save_item(self.item_entry.get())
        if response == True:
            messagebox.showinfo(title='Info',message=f'Categoria "{self.item_entry.get()}" agregada!')
        else:
            messagebox.showerror(title='Error',message=f'Hubo un error al agregar la categoria.')
        self.item_window.destroy()

# Class ConfigWindow
class ConfigWindow():
    """create a new window in toplevel with conection settings getted from Config.get_conection_config
        from here can change the conection config and save changes pressing button
        the button execute the save_config_changes function with the new information of config getted
        from entry boxes in the config_window
        """
    def __init__(self,error:bool) -> None:
        self.error = error
        self.connect_data = Config()

        if error == True:
            self.config_window = tk.Tk()
        else:
            self.config_window = tk.Toplevel()
        self.config_window.title('Configurar conexion...')

        self.host_label=tk.Label(self.config_window,text='host:')
        self.host_label.place(x=10,y=10)

        self.host_entry=tk.Entry(self.config_window)
        self.host_entry.insert(0,self.connect_data.host)
        self.host_entry.place(x=70,y=10)

        self.port_label=tk.Label(self.config_window,text='port:')
        self.port_label.place(x=10,y=40)

        self.port_entry=tk.Entry(self.config_window)
        self.port_entry.insert(0,self.connect_data.port)
        self.port_entry.place(x=70,y=40)

        self.usr_label=tk.Label(self.config_window,text='usr:')
        self.usr_label.place(x=10,y=70)

        self.usr_entry=tk.Entry(self.config_window)
        self.usr_entry.insert(0,self.connect_data.user)
        self.usr_entry.place(x=70,y=70)

        self.pass_label=tk.Label(self.config_window,text='pass:')
        self.pass_label.place(x=10,y=100)

        self.pass_entry=tk.Entry(self.config_window)
        self.pass_entry.insert(0,self.connect_data.passw)
        self.pass_entry.place(x=70,y=100)

        self.db_label=tk.Label(self.config_window,text='db:')
        self.db_label.place(x=10,y=130)

        self.db_entry=tk.Entry(self.config_window)
        self.db_entry.insert(0,self.connect_data.db)
        self.db_entry.place(x=70,y=130)

        self.button_save=tk.Button(self.config_window,
                            text='Guardar Cambios',
                            command=self.save_config_changes)
        self.button_save.place(x=20,y=160)

        self.button_cancel=tk.Button(self.config_window,text='Cancelar',command=self.config_window.destroy)
        self.button_cancel.place(x=140,y=160)
        if error == True:
            self.config_window.mainloop()

    def save_config_changes (self):
        self.connect_data.set_conection_config( self.host_entry.get(),
                                                self.port_entry.get(),
                                                self.usr_entry.get(),
                                                self.pass_entry.get(),
                                                self.db_entry.get()
                                                )
        messagebox.showinfo(title='Info',message=f'Configuracion Actualizada!')
        self.config_window.destroy()

# Class Reports Window
class ReportWindow():
    mysql_query = 'SELECT item,value,date,observations FROM register'
    def __init__(self,qery) -> None:
        self.mysql_query = qery
        report = Reports(self.mysql_query)
        report_data = report.get_all()
        self.reports_window = tk.Toplevel()
        self.reports_window.title('Reportes')
        self.reports_window.config(height=550,width=680)

        self.text_box = tk.Text(self.reports_window)
        self.text_box.pack(expand=True)
        self.text_box.place(x=10,y=50)
        self.text_box.tag_configure("center",justify='center')
        self.text_box.insert(tk.END, report_data.data,"center")

        output = 'Total de gastos: € ' + str(report_data.amount)
        self.total_label=tk.Label(self.reports_window,text=output)
        self.total_label.place(x=10,y=480)

        self.button_exit = tk.Button(self.reports_window,text='Regresar',command = self.reports_window.destroy)
        self.button_exit.place(x=250,y=500)

# Class Select Report (Window)
class SelectReport():

    def __init__(self) -> None:
        self.window = tk.Toplevel()
        self.window.title('Reportes')
        self.window.config(height=250,width=300)


        self.button_confirm = tk.Button(self.window,text='Generar Reporte',command = self.report_window)
        self.button_confirm.place(x=20,y=200)

        self.button_exit = tk.Button(self.window,text='Regresar',command = self.window.destroy)
        self.button_exit.place(x=150,y=200)
        
    def report_by_item(self):
        # Set the Interface to get list for Combolist
        interface = InterfaceItems(conection)
        # Set the combolist:
        combolist = interface.get_items()

        self.label_statement_reports = tk.Label(self.window,text='Rubro: ')
        self.label_statement_reports.place(x=10,y=10)

        self.select_statement_reports= Combobox(self.window,values=combolist)
        self.select_statement_reports.current(0)
        self.select_statement_reports.place(x=100,y=10)

    def report_by_date(self):
        self.label_statement_date1 = tk.Label(self.window,text='Fecha Inicio: ')
        self.label_statement_date1.place(x=10,y=80)

        self.init_date = DateEntry(self.window,selectmode='day')
        self.init_date.place(x=100,y=80)  

        self.label_statement_date2 = tk.Label(self.window,text='Fecha Fin: ')
        self.label_statement_date2.place(x=10,y=100)   

        self.final_date = DateEntry(self.window,selectmode='day')
        self.final_date.place(x=100,y=100)
        
    def report_window(self):
        date_converter = Date()
        try:
            self.select_statement_reports.get()
            case = 1
        except:
            pass
        try:
            init_date = date_converter.convert_calendar_to_db(str(self.init_date.get_date()))
            final_date = date_converter.convert_calendar_to_db(str(self.final_date.get_date()))
            case = 2
        except:
            pass
        try:
            self.select_statement_reports.get()
            init_date = date_converter.convert_calendar_to_db(str(self.init_date.get_date()))
            final_date = date_converter.convert_calendar_to_db(str(self.final_date.get_date()))
            case =3
        except:
            pass
        if case == 1:
            self.mysql_qery = f"""SELECT item,value,date,observations 
                                FROM register WHERE item LIKE 
                                ('{self.select_statement_reports.get()}') ORDER BY date ASC"""
        elif case == 2:
            self.mysql_qery = f"""SELECT item,value,date,observations
                             FROM register WHERE date BETWEEN 
                             ('{init_date}') AND ('{final_date}') ORDER BY date ASC"""
        elif case == 3:
            self.mysql_qery = f"""SELECT item,value,date,observations
                             FROM register WHERE 
                             (item LIKE ('{self.select_statement_reports.get()}') 
                             AND (date BETWEEN ('{init_date}') 
                             AND ('{final_date}'))) ORDER BY date ASC"""

        window = ReportWindow(self.mysql_qery)

# Windows Openers
def open_item_window():
    window = ItemWindow()

def open_config_window():
    window = ConfigWindow(error=False)

def open_report_window():
    window = ReportWindow('SELECT item,value,date,observations FROM register ORDER BY date ASC')

def report_item_window():
    window = SelectReport()
    window.report_by_item()

def report_date_window():
    window = SelectReport()
    window.report_by_date()

def report_full_window():
    window = SelectReport()
    window.report_by_item()
    window.report_by_date()

# Operational Functions
def confirm_register(item:str,amount:float,observation:str,date:str):
    # Convert Date Format:
    date_converter = Date()
    date = date_converter.convert_calendar_to_db(str(date))
    register = Register(item=item,amount=amount,observation=observation,date=date)
    # if amount is epty, error message
    if not register.amount:
        messagebox.showerror(title='Error',message='Debe ingresar un importe')
        return None
    response = register.amount = float_validate(register.amount)
    if response == False:
        messagebox.showerror(title='Error',message='El importe debe ser numerico')
        return None
    response = save.save_register(register)
    if response == True:
        messagebox.showinfo(title='Info',message=f'Registro agregado!')
    else:
        messagebox.showerror(title='Error',message=f'Hubo un error al agregar el registro.')

def float_validate(amount:str) -> bool:
    if amount.find(',') != -1:
        amount = amount.replace(',','.')
    try:
        amount=float(amount)
        return amount
    except:
        return False

