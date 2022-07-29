from modules.conn import Conection

class Interface():
    """Returns a list of all items in DB 'items'
        Needs a Conection to DB to work...
    """
    def get_items(self):
        conection = Conection().conection()
        conection[1].execute('SELECT * FROM items')
        datos = conection[1].fetchall()
        lista=[]
        for a in datos:
            lista.append(a[1])
        conection[0].close()
        return lista

