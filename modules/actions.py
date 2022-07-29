import tkinter as tk
from tkinter import messagebox
from modules.conn import *
from modules.register import Save
from modules.reports import *
from modules.interface import *
from tkinter.ttk import Combobox
import sys
from modules.date import *

# get list of items from iterface
combolist = Interface().get_items()


def confirm_register(statement:str,amount:str,observations:str) -> None:
    """save the register in DB
    all of recieved dates from tkinter are strings
    first, search ',' in the amount, if have the character change to '.' for make a casting to float
    try to cast, if can cast, save the register with class Save
    else show a messagebox error type

    """
    if amount.find(',') != -1:
        amount = amount.replace(',','.')
    try:
        amount=float(amount)
        Save().save_register(statement,amount,observations)
    except: #faltaria ponerle el tipo de error, que si no me equivoco es TypeError
        messagebox.showerror(title='Error',message='El importe debe ser numerico')

def exit_program():
    """Use sys module to exit program
    """
    sys.exit()

def set_conection():
    """create a new window in toplevel with conection settings getted from Config.get_conection_config
    from here can change the conection config and save changes pressing button
    the button execute the save_config_changes function with the new information of config getted
    from entry boxes in the config_window
    """
    conection_info = Config().get_conection_config()

    config_window = tk.Toplevel()
    config_window.title('Configurar conexion...')

    host_label=tk.Label(config_window,text='host:')
    host_label.place(x=10,y=10)

    host_entry=tk.Entry(config_window)
    host_entry.insert(0,str(conection_info[0]))
    host_entry.place(x=70,y=10)

    port_label=tk.Label(config_window,text='port:')
    port_label.place(x=10,y=40)

    port_entry=tk.Entry(config_window)
    port_entry.insert(0,str(conection_info[1]))
    port_entry.place(x=70,y=40)
    
    usr_label=tk.Label(config_window,text='usr:')
    usr_label.place(x=10,y=70)

    usr_entry=tk.Entry(config_window)
    usr_entry.insert(0,str(conection_info[2]))
    usr_entry.place(x=70,y=70)
    
    pass_label=tk.Label(config_window,text='pass:')
    pass_label.place(x=10,y=100)

    pass_entry=tk.Entry(config_window)
    pass_entry.insert(0,str(conection_info[3]))
    pass_entry.place(x=70,y=100)
    
    db_label=tk.Label(config_window,text='db:')
    db_label.place(x=10,y=130)

    db_entry=tk.Entry(config_window)
    db_entry.insert(0,str(conection_info[4]))
    db_entry.place(x=70,y=130)

    button_save=tk.Button(config_window,
                        text='Guardar Cambios',
                        command=lambda:save_config_changes(
                            host_entry.get(),
                            port_entry.get(),
                            usr_entry.get(),
                            pass_entry.get(),
                            db_entry.get()
                        ))
    button_save.place(x=20,y=160)

    button_cancel=tk.Button(config_window,text='Cancelar',command=config_window.destroy)
    button_cancel.place(x=140,y=160)

def save_config_changes(host,port,usr,passw,db):
    """recieves the new config settings and save with Config().set_conection_config() method
    """
    Config().set_conection_config(host,port,usr,passw,db)

def add_item():
    """create a new toplevel window with an entry box to put the name of the new item in DB
    when press the button, close the window and execute Save().save_item()  with the name of new item
    """
    item_window = tk.Toplevel()
    item_window.title('Agregar nuevo Rubro')
    item_window.config(height=120,width=250)

    item_label = tk.Label(item_window,text='Nombre: ')
    item_label.place(x=10,y=10)

    item_entry = tk.Entry(item_window)
    item_entry.place(x=100,y=10)

    button_confirm = tk.Button(item_window,text='Agregar',command=lambda:[item_window.destroy,Save().save_item((item_entry.get()))])
    button_confirm.place(x=20,y=50)

    button_cancel = tk.Button(item_window,text='Cancelar',command = item_window.destroy)
    button_cancel.place(x=90,y=50)

def reports():
    """create a new toplevel window with te returned information of Reports().get_all()
    """
    report = Reports().get_all()
    reports_window = tk.Toplevel()
    reports_window.title('Reportes')
    reports_window.config(height=550,width=680)

    text_box = tk.Text(reports_window,height=25,width=75)
    text_box.place(x=10,y=50)
    text_box.insert(tk.END, report[0])

    output = 'Total de gastos: €' + str(report[1])
    total_label=tk.Label(reports_window,text=output)
    total_label.place(x=10,y=480)

    button_exit = tk.Button(reports_window,text='Regresar',command = reports_window.destroy)
    button_exit.place(x=250,y=500)



def reports2():
    """create new toplevel window , with a combobox item list to select, and execute 
    Report_window().new_window_report() with the item selected when press confirm button
    """
    reports2_window = tk.Toplevel()
    reports2_window.title('Reportes')
    reports2_window.config(height=250,width=300)

    label_statement_reports = tk.Label(reports2_window,text='Rubro: ')
    label_statement_reports.place(x=10,y=10)

    select_statement_reports= Combobox(reports2_window,values=combolist)
    select_statement_reports.current(0)
    select_statement_reports.place(x=100,y=10)

    button_confirm = tk.Button(reports2_window,text='Generar Reporte',command =
                                                                        lambda:Report_window().new_window_report(select_statement_reports.get())
                                )
    button_confirm.place(x=10,y=100)

    button_exit = tk.Button(reports2_window,text='Regresar',command = reports2_window.destroy)
    button_exit.place(x=150,y=100)

def reports3():
    """create new toplevel window , with two entry labels for put init date and end date, and execute 
    Report_window().new_window_report_dates() with the information of dates writed
    """
    reports3_window = tk.Toplevel()
    reports3_window.title('Reportes')
    reports3_window.config(height=250,width=300)

    label_statement_date1 = tk.Label(reports3_window,text='Fecha Inicio: ')
    label_statement_date1.place(x=10,y=40)

    entry_date1 = tk.Entry(reports3_window)
    entry_date1.place(x=100,y=40)  

    label_statement_date2 = tk.Label(reports3_window,text='Fecha Fin: ')
    label_statement_date2.place(x=10,y=70)   

    entry_date2 = tk.Entry(reports3_window)
    entry_date2.place(x=100,y=70)

    button_confirm = tk.Button(reports3_window,text='Generar Reporte',command=
                                                                        lambda:Report_window().new_window_report_dates(
                                                                            Date().convert_to_db(entry_date1.get()),Date().convert_to_db(entry_date2.get())))
    button_confirm.place(x=10,y=100)

    button_exit = tk.Button(reports3_window,text='Regresar',command = reports3_window.destroy)
    button_exit.place(x=150,y=100)


def reports4():
    """create new toplevel window , with two entry labels for put init date and end date and
    combobox list for select an item, and execute Report_window().new_window_report_complete()
     with the information of dates and item selected
    """

    reports2_window = tk.Toplevel()
    reports2_window.title('Reportes')
    reports2_window.config(height=250,width=300)

    label_statement_reports = tk.Label(reports2_window,text='Rubro: ')
    label_statement_reports.place(x=10,y=10)

    select_statement_reports= Combobox(reports2_window,values=combolist)
    select_statement_reports.current(0)
    select_statement_reports.place(x=100,y=10)

    label_statement_date1 = tk.Label(reports2_window,text='Fecha Inicio: ')
    label_statement_date1.place(x=10,y=40)

    entry_date1 = tk.Entry(reports2_window)
    entry_date1.place(x=100,y=40)  

    label_statement_date2 = tk.Label(reports2_window,text='Fecha Fin: ')
    label_statement_date2.place(x=10,y=70)   

    entry_date2 = tk.Entry(reports2_window)
    entry_date2.place(x=100,y=70)  

    button_confirm = tk.Button(reports2_window,text='Generar Reporte',command =
                                                                        lambda:Report_window().new_window_report_complete(
                                                                            select_statement_reports.get(),
                                                                            Date().convert_to_db(entry_date1.get()),
                                                                            Date().convert_to_db(entry_date2.get())
                                                                            )
                                )
    button_confirm.place(x=10,y=100)

    button_exit = tk.Button(reports2_window,text='Regresar',command = reports2_window.destroy)
    button_exit.place(x=150,y=100)


def reports_gas():
    pass

def info():
    messagebox.showinfo(title='Info',message="""Colo soft, desarrollado por Andres.
    Registro y reporte de gastos por categorias.
    Gracias por curiosear la info!
    Andres""")