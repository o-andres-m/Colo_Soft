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
