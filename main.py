import tkinter as tk
from tkinter.ttk import Combobox
from modules.actions import *
from modules.date import Date
from modules.interface import *
from modules.reports import Reports

#get list of items from Interface().get_items(), and if the list is epty, put
#an alert message to create items first
#restart the software to see the changes.. (fail..)
combolist = Interface().get_items()
if not combolist:
    messagebox.showinfo(title='Atencion!',message="""Recuerde que antes de registrar consumos debe crear al menos 1 rubro.
    Para crearlos ir a Archivo->Agregar Rubro
    """)
    combolist = ['REINICIAR SISTEMA PARA VER RUBROS']


def delete_entry():
    """delete entrys
    """
    entry_observations.delete(0,tk.END)
    entry_import.delete(0,tk.END)  

main_window = tk.Tk()
main_window.title('Colo_Soft Registros V0.1')

label_statement = tk.Label(text='Rubro: ')
label_statement.place(x=40,y=50)
#combolist
select_statement= Combobox(values=combolist)
select_statement.current(0)
select_statement.place(x=200,y=50)

label_import = tk.Label(text='Importe (€):')
label_import.place(x=40,y=100)
entry_import = tk.Entry()
entry_import.place(x=200,y=100)

label_observations = tk.Label(text='Observaciones:')
label_observations.place(x=40,y=150)
entry_observations = tk.Entry()
entry_observations.place(x=200,y=150)

#execute confirm_register() and delete_entry()
button_confirm = tk.Button(text='CONFIRMAR REGISTRO',
                            command=lambda:[
                                confirm_register(
                                select_statement.get(),
                                entry_import.get(),
                                entry_observations.get()
                            ),
                            delete_entry()
                            ])
                            
button_confirm.place(x=200,y=200)

label_date = tk.Label(text=f'Fecha {Date().today_esp()}')
label_date.place(x=40,y=250)

#calculate total expenses of the month
month_init = (str(Date().year())+str(Date().month())+str('01'))
month_init.replace(' ','')
month_end = Date().convert_to_db(Date().today_esp())
total_bills = Reports().get_with_date(month_init,month_end)[1]


#Reports().get_with_date(20220101,
label_total_month = tk.Label(text=f'Total Gastado en el mes {Date().month()} hasta la fecha: {total_bills}') 
label_total_month.place(x=40,y=270)

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

menu_file.add_command(label='Agregar Rubro',command=add_item)
menu_file.add_command(label='Salir',command=exit_program)
menu_config.add_command(label='Configurar Conexion',command=set_conection)
menu_reports.add_command(label='Reporte TOTAL de Gastos',command=reports)
menu_reports.add_command(label='Reporte TOTAL POR RUBRO',command=reports2)
menu_reports.add_command(label='Reporte TOTAL POR FECHA',command=reports3)
menu_reports.add_command(label='Reporte POR RUBRO Y FECHA',command=reports4)
#menu_reports.add_command(label='Reporte Consumo Combustible',command=reports_gas)
menu_about.add_command(label='Info..',command=info)
#------END MENU


main_window.configure(height=310,width=400,menu=menu_bar)
main_window.mainloop()