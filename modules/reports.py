from tabulate import tabulate
from modules.conn import Conection
from modules.date import Date
from modules.register import Report


class Reports():
    """
    """
    conection = Conection()

    def __init__(self,mysql_qery) -> None:
        self.mysql_qery = mysql_qery

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
