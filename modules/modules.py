from modules.conn import Conection
from datetime import date

# Date: have the methods for work with the different dates
class Date():
    """Date class have 2 functionalities, one is for return dates in different formats, another is
    for change format of date:

    1) today_esp        : dd/mm/yyyy
    2) today_eng        : yyyymmdd
    3) today            : dd
    4) month            : mm
    5) year             : yyyy

    6) convert_to_esp : recieves -> yyyymmdd  ; return -> dd/mm/yyyy
    7) convert_to_eng : recieves -> dd/mm/yyyy  ; return -> yyyymmdd
    8) convert_calendar_to_db : recieves -> yyyy-mm-dd  ; return -> yyyymmdd

    """
    _date = date.today()

    def today_esp(self) -> str:
        return (str(f'{self._date.day:02d}')+'/'+str(f'{self._date.month:02d}')+'/'+str(self._date.year))

    def today_eng(self):
        return (str(self._date.year)+str(f'{self._date.month:02d}')+str(f'{self._date.day:02d}'))

    def today(self) -> int:
        return f'{self._date.day:02d}'

    def month(self) -> int:
        return f'{self._date.month:02d}'

    def year(self) -> int:
        return f'{self._date.year}'

    def convert_to_esp(self,dates):
        return (f'{dates[-2:]}/{dates[4:6]}/{dates[:4]}')

    def convert_to_db(self,dates):
        return (f'{dates[-4:]}{dates[3:5]}{dates[0:2]}')
    
    def convert_calendar_to_db(self,dates):
        return (f'{dates[:4]}{dates[5:7]}{dates[8:]}')

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

# Function to validate Float number
def float_validate(amount:str) -> bool:
    if amount.find(',') != -1:
        amount = amount.replace(',','.')
    try:
        amount=float(amount)
        return amount
    except:
        return False