from tabulate import tabulate
from modules.conn import Conection
from modules.modules import Date
from modules.classes import Report


class Reports():
    """Class Reports recieves 4 atributes:
    case   - >  case = 1 select all registers
                case = 2 select registers filter by item
                case = 3 select registers between dates
                case = 4 selec registers filter by item and between dates
    item  - > defines the item category
    init_date and final_date - > defines the range of search
    """
    conection = Conection()

    def __init__(self,case:int,item:str,init_date:int,final_date:int) -> None:
        self.case = case
        self.item = item
        self.init_date = init_date
        self.final_date = final_date

        if self.case == 1:
            self.mysql_qery = """SELECT item,value,date,observations FROM register ORDER BY date ASC"""
        elif case == 2:
            self.mysql_qery =f"""SELECT item,value,date,observations 
                                FROM register WHERE item LIKE 
                                ('{self.item}') ORDER BY date ASC"""
        elif case == 3:
            self.mysql_qery = f"""SELECT item,value,date,observations
                             FROM register WHERE date BETWEEN 
                             ('{self.init_date}') AND ('{self.final_date}') ORDER BY date ASC"""
        elif case == 4:
            self.mysql_qery = f"""SELECT item,value,date,observations
                             FROM register WHERE 
                             (item LIKE ('{self.item}') 
                             AND (date BETWEEN ('{self.init_date}') 
                             AND ('{self.final_date}'))) ORDER BY date ASC"""

    def get_all(self) -> Report:
        self.conection.conection()
        self.conection.cursor.execute(self.mysql_qery)
        data = self.conection.cursor.fetchall()
        self.conection.conn.close()
        # Change the TUPLE to LIST
        data = list(data)
        for a in range(len(data)):
            data[a] = list(data[a])
        # Sumarize total Amount
        total_amount = 0
        for a in data:
            total_amount += float(a[1])
        # Total amount set 2 decimals
        total_amount = "{:.2f}".format(total_amount)
        # Change format of date:
        for a in data:
            a[2]=Date().convert_to_esp(a[2])
        # Creare Object to return
        data_final = Report(tabulate(data,['RUBRO', 'GASTO','FECHA','OBSERVACIONES'] ,tablefmt="pretty"),total_amount)
        return data_final
