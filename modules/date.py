from abc import ABC, abstractmethod
from datetime import date

class Date():
    """Date class have 2 functionalities, one is for return dates in different formats, another is
    for change format of date:

    1) today_esp        : dd/mm/yyyy
    2) today_eng        : yyyymmdd
    3) today            : dd
    4) month            : mm
    5) year             : yyyy

    5) convert_to_esp : recieves -> yyyymmdd  ; return -> dd/mm/yyyy
    5) convert_to_eng : recieves -> dd/mm/yyyy  ; return -> yyyymmdd

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

