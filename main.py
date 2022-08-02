from email import message
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import DateEntry
from modules.conn import Conection
from modules.interface import *
from modules.date import Date


# Set the Conection instance:
conection = Conection()
# If have Conection problems, show config window 
if conection.conection() == False:
    messagebox.showerror(title='Error',message='Error al conectar la DB, verifique datos')
    window = ConfigWindow(error=True)
    exit()
# Set the Interface to get list for Combolist
interface = InterfaceItems(conection=conection)
# Set the combolist:
combolist = interface.get_items()
# If combolist is epty, show alert to register first the items
if not combolist:
    messagebox.showinfo(title='Atencion!',message="""Recuerde que antes de registrar consumos debe crear al menos 1 rubro.
    Para crearlos ir a Archivo->Agregar Rubro
    """)
    combolist = ['CLICK EN REFRESH ->']

# Date 
date = Date()

def delete_entry():
    """Delete info in Entry Labels
    """
    entry_observations.delete(0,tk.END)
    entry_import.delete(0,tk.END)

def reset_item_list():
    """Refresh combobox list of items
    """
    combolist = interface.get_items()
    select_statement.configure(values=combolist)
    select_statement.current(0)

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title('Colo_Soft Registros V1.1')

    label_statement = tk.Label(text='Rubro: ')
    label_statement.place(x=40,y=50)
    #combolist
    select_statement= Combobox(values=combolist)
    select_statement.current(0)
    select_statement.place(x=200,y=50)

    button_refresh = tk.Button(text='®',command=reset_item_list)
    button_refresh.place(x=360,y=50)


    label_import = tk.Label(text='Importe (€):')
    label_import.place(x=40,y=100)
    entry_import = tk.Entry()
    entry_import.place(x=200,y=100)

    label_observations = tk.Label(text='Observaciones:')
    label_observations.place(x=40,y=150)
    entry_observations = tk.Entry()
    entry_observations.place(x=200,y=150)

    label_calendar = tk.Label(text='Fecha:')
    label_calendar.place(x=40,y=200)

    calendar = DateEntry(main_window,selectmode='day')
    calendar.place(x=200,y=200)

    #execute confirm_register() and delete_entry()
    button_confirm = tk.Button(text='CONFIRMAR REGISTRO',
                                command=lambda:[
                                    confirm_register(
                                    select_statement.get(),
                                    entry_import.get(),
                                    entry_observations.get(),
                                    calendar.get_date()
                                ),
                                delete_entry()
                                ])

    button_confirm.place(x=150,y=250)

    label_date = tk.Label(text=f'Fecha {date.today_esp()}')
    label_date.place(x=40,y=300)

    #calculate total expenses of the month
    """
    month_init = (str(Date().year())+str(Date().month())+str('01'))
    month_init.replace(' ','')
    month_end = Date().convert_to_db(Date().today_esp())
    total_bills = Reports().get_with_date(month_init,month_end)[1]


    label_total_month = tk.Label(text=f'Total Gastado en el mes {Date().month()} hasta la fecha: {total_bills}') 
    label_total_month.place(x=40,y=270)
    """
    #---- START MENU
    menu_bar = tk.Menu()
    menu_file = tk.Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='Archivo', menu=menu_file)
    menu_config =tk.Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='Config', menu=menu_config)
    menu_reports=tk.Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='Reportes',menu=menu_reports)
    menu_about = tk.Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='Acerca De...',menu=menu_about)
    

    menu_file.add_command(label='Agregar Rubro',command=open_item_window)
    menu_file.add_command(label='Salir',command=exit_program)
    menu_config.add_command(label='Configurar Conexion',command=open_config_window)
    menu_reports.add_command(label='Reporte TOTAL de Gastos',command=open_report_window)
    menu_reports.add_command(label='Reporte TOTAL POR RUBRO',command=report_item_window)
    menu_reports.add_command(label='Reporte TOTAL POR FECHA',command=report_date_window)
    menu_reports.add_command(label='Reporte POR RUBRO Y FECHA',command=report_full_window)
    menu_about.add_command(label='Info..',command=info)
    #------END MENU
    

    main_window.configure(height=380,width=400,menu=menu_bar)
    main_window.mainloop()