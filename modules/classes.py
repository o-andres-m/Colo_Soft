class Register():

    def __init__(self,item:str,amount:float,observation:str,date:str) -> None:
        self.item       = item
        self.amount     = amount
        self.obsevation = observation
        self.date       = date

class Report():
    def __init__(self,data:str,amount:float,) -> None:
        self.data       = data
        self.amount     = amount

class GetReport():
    def __init__(self,case:int,item:str,init_date:int,final_date:int) -> None:
        self.case       = case
        self.item       = item
        self.init_date  = init_date
        self.final_date = final_date
