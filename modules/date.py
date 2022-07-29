from datetime import date

class Date():
    """Date class have 2 functionalities, one is for return dates in different formats, another is
    for change format of date:

    1) today_esp : dd/mm/yyyy
    2) today_eng : yyyymmdd
    3) today     : dd
    4) month     : mm
    5) year      : yyyy

    5) convert_to_esp : recieves -> yyyy/mm/dd  ; return -> dd/mm/yyyy
    6) convert_to_eng : recieves -> dd/mm/yyyy  ; return -> yyyy/mm/dd
    6) convert_to_db : recieves -> dd/mm/yyyy  ; return -> yyyymmdd

    """

    def today_esp(self) -> str:
        _date = date.today()
        final_date = str(f'{_date.day:02d}')+'/'+str(f'{_date.month:02d}')+'/'+str(_date.year)
        return final_date

    def today_eng(self):
        _date = date.today()
        final_date = str(_date.year)+str(f'{_date.month:02d}')+str(f'{_date.day:02d}')
        return final_date

    def today(self) -> int:
        _date = date.today()
        return f'{_date.day:02d}'

    def month(self) -> int:
        _date = date.today()
        return f'{_date.month:02d}'

    def year(self) -> int:
        _date = date.today()
        return f'{_date.year}'

    def convert_to_esp(self,dates):
        return (f'{dates[-2:]}/{dates[4:6]}/{dates[:4]}')

    def convert_to_eng(self,dates):
        return (f'{dates[:4]}/{dates[4:6]}/{dates[-2:]}')

    def convert_to_db(self,dates):
        return (f'{dates[-4:]}{dates[3:5]}{dates[0:2]}')

