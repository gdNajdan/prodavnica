class prodavnica:
    def __init__(self, pro1, cena1, pro2, cena2):
        self.pro1=pro1
        self.cena1=cena1
        self.pro2=pro2
        self.cena2=cena2
    def IInventar(self):
        return (self.pro1*self.cena1+self.pro2*self.cena2)
pr1 = prodavnica(4,120,5,50)
Pr = pr1.IInventar()
pr2 = prodavnica(2,23,6,7)
Pr2 = pr2.IInventar()
pr3 = prodavnica(1,230,4,12)
Pr3 = pr3.IInventar()
print(max(Pr, Pr2, Pr3))
