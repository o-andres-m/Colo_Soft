from tabulate import tabulate
from modules.conn import Conection
import tkinter as tk


class Reports():
    """class Reports returns the obtained data of query in DB according to necesarie information.
        for this class need a conection, and need a tabulate module, for tabulate information.
        in each method there is an total_amount for print that information separated of general information
    1) get_all          : returns a tuple with tabulate table with all registers, and total amount
    2) get_with_item    : reciebes an item, and returns a tuple with tabulate table from that item, and total amount
    3) get_with_date    : reciebes init and final date, and returns a tuple with tabulate table from
    all items between that dates, and total amount
    4) get_with_date_and_item   : reciebes init and final date and item, and returns a tuple with tabulate table from
    that item between that dates, and total amount

    """
    def get_all(self):
        conection = Conection().conection()
        conection[1].execute('SELECT * FROM register')
        data = conection[1].fetchall()
        total_amount = 0
        for a in data:
            total_amount += float(a[2])
        conection[0].close()
        return tabulate(data,['ID','RUBRO', 'GASTO','FECHA','OBSERVACIONES'] ,tablefmt="pretty"),total_amount

    def get_with_item(self,item):
        conection = Conection().conection()
        conection[1].execute('SELECT * FROM register WHERE item LIKE (%s)',(item))
        data = conection[1].fetchall()
        total_amount = 0
        for a in data:
            total_amount += float(a[2])
        conection[0].close()
        return tabulate(data,['ID','RUBRO', 'GASTO','FECHA','OBSERVACIONES'] ,tablefmt="pretty"),total_amount

    def get_with_date(self,date_init,date_end):
        conection = Conection().conection()
        conection[1].execute('SELECT * FROM register WHERE date BETWEEN (%s) AND (%s)',(date_init,date_end))
        data = conection[1].fetchall()
        total_amount = 0
        for a in data:
            total_amount += float(a[2])
        conection[0].close()
        return tabulate(data,['ID','RUBRO', 'GASTO','FECHA','OBSERVACIONES'] ,tablefmt="pretty"),total_amount

    def get_with_date_and_item(self,item, date_init,date_end):
        conection = Conection().conection()
        conection[1].execute('SELECT * FROM register WHERE (item LIKE (%s) AND (date BETWEEN (%s) AND (%s)))',(item,date_init,date_end))
        data = conection[1].fetchall()
        total_amount = 0
        for a in data:
            total_amount += float(a[2])
        conection[0].close()
        return tabulate(data,['ID','RUBRO', 'GASTO','FECHA','OBSERVACIONES'] ,tablefmt="pretty"),total_amount

class Report_window(Reports):
    """its a class from Reports class, that is only for use the Reports methods.
    the use is for creat the windows of reports
    1) new_window_report : recieves an item, and create a new window in toplevel with the 
    information of "get_with_item" returns. its have a button to close the window
    2) new_window_report_dates : recieves init and final date, and create a new window in toplevel with the 
    information of "get_with_date" returns. its have a button to close the window
    3) new_window_report_complete : recieves an item,init and final date, and create a new window in toplevel with the 
    information of "get_with_date_and_items" returns. its have a button to close the window
    """
    def new_window_report(self,item):
        report_top_window = tk.Toplevel()
        report_top_window.config(height=550,width=600)

        text_box = tk.Text(report_top_window,height=25,width=63)
        text_box.place(x=10,y=50)
        text_box.insert(tk.END, super().get_with_item(item)[0])
        
        output = 'Total de gastos: €' + str(super().get_with_item(item)[1])
        total_label=tk.Label(report_top_window,text=output)
        total_label.place(x=10,y=480)
        
        button_exit = tk.Button(report_top_window,text='Regresar',command = report_top_window.destroy)
        button_exit.place(x=250,y=500)


    def new_window_report_dates(self,init_date,final_date):
        report_top_window = tk.Toplevel()
        report_top_window.config(height=550,width=600)

        text_box = tk.Text(report_top_window,height=25,width=63)
        text_box.place(x=10,y=50)
        text_box.insert(tk.END, super().get_with_date(init_date,final_date)[0])
        
        output = 'Total de gastos: €' + str(super().get_with_date(init_date,final_date)[1])
        total_label=tk.Label(report_top_window,text=output)
        total_label.place(x=10,y=480)
        
        button_exit = tk.Button(report_top_window,text='Regresar',command = report_top_window.destroy)
        button_exit.place(x=250,y=500)

    def new_window_report_complete(self,item,init_date,final_date):
        report_top_window = tk.Toplevel()
        report_top_window.config(height=550,width=600)

        text_box = tk.Text(report_top_window,height=25,width=63)
        text_box.place(x=10,y=50)
        text_box.insert(tk.END, super().get_with_date_and_item(item,init_date,final_date)[0])
        
        output = 'Total de gastos: €' + str(super().get_with_date_and_item(item,init_date,final_date)[1])
        total_label=tk.Label(report_top_window,text=output)
        total_label.place(x=10,y=480)
        
        button_exit = tk.Button(report_top_window,text='Regresar',command = report_top_window.destroy)
        button_exit.place(x=250,y=500)


#Reports().get_all()