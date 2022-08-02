from modules.conn import Conection
from modules.register import Register


class Save():
    """Save class is for save registers and items. needs a conection to work
    1) save_register : recieves an Register objetct and execute the qery to insert data in DB
    2) save_idem     : recieves item  and execute the qery to insert data in DB. 
¡       both methods returns "True" if the save is correct, or "false" if something happened
    """
    def __init__(self,conection : Conection) -> None:
        self.conection = conection

    def save_register(self,register:Register) -> bool:
        try:
            self.conection.conection()
            mysql_qery ='INSERT INTO register VALUES (%s,%s,%s,%s,%s)'
            self.conection.cursor.execute((mysql_qery),(None,register.item,register.amount,register.date,register.obsevation))
            self.conection.conn.commit()
            self.conection.conn.close()
            return True
        except:
            return False

    def save_item(self,item:str)-> bool:
        try:
            self.conection.conection()
            mysql_qery = 'INSERT INTO items VALUES (%s,%s)'
            self.conection.cursor.execute((mysql_qery),(None,item))
            self.conection.conn.commit()
            self.conection.conn.close()
            return True
        except:
            return False