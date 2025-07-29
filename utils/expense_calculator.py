class Calculator:

    @staticmethod  ## defining an static emthod that beloings to teh class
    def multiply(a: int,b:int)->int:
        return a*b
    
    @staticmethod
    def calculate_total(*x:float)->float:
        return sum(x)
    
    @staticmethod
    def calcualte_daily_budget(total:float,days:int)->float:
        return total / days if days > 0 else 0