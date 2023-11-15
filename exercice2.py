class Batiment:
    def __init__(self, adresse):
        self.__adresse = adresse
    def getAdress(self):
        return self.__adresse
    def setAdress(self, a):
        self.__adresse=a
    def __str__(self):
        return f"L'adresse de la batiment est :{self.getAdress()}"
class Maison(Batiment):
    def __init__(self,adresse ,nbPieces):
        super().__init__(adresse)
        self.__nbPieces=nbPieces
    def getNPieces(self):
        return self.__nbPieces
    def setNbPieces(self,a):
        self.__nbPieces=a
    def __str__(self):

        return f"{super().__str__()}\nle nombre de pieces est :{self.getNPieces()} "
class Immeuble(Maison):
    def __init__(self ,adresse ,nbPieces ,nbAppart):
        super().__init__(adresse ,nbPieces)
        self.__nbAppart=nbAppart
    def getnbAppart(self):
        return self.__nbAppart
    def setnbAppart(self,a):
        self.__nbAppart=a
    def __str__(self):
        return f"{super().__str__()}\nle nombre d'appartements est :{self.getnbAppart()}"
Immeuble1=Immeuble("Hay Moulay youssef",10,4)
print(Immeuble1)