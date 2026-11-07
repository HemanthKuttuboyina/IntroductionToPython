class IBM:
    def __init__(self,w: int,h: float):
        self.weight = w
        self.height = h
    def calculator(self)-> str:
        ibm = self.weight/self.height ** 2
        if ibm < 18.5:
            return f"{ibm:.1f} (UnderWeight)"
        elif ibm <= 25:
            return f"{ibm:.1f} (Normal)"
        elif ibm <= 30:
            return f"{ibm:.1f} (OverWeight)"
        else:
            return f"{ibm:.1f} (Obese)"
hemanth = IBM(50,1.63)
print(hemanth.calculator())