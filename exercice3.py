class Employe:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    def getNom(self):
            return self.__nom
    def getPrenom(self):
            return self.__prenom
    def setNom(self,a):
            self.__nom = a
    def setPrenom(self,a):
            self.__prenom = a
    def __str__(self):
            return f"le nom complet de l'employe est :{self.__nom} {self.__prenom}"
    def gains(self):
            pass
class Patron(Employe):
    def __init__(self,nom,prenon,salaire):
        super().__init__(nom,prenon)
        self.__salaire=salaire
    def getSalaire(self):
        return self.__salaire
    def setSalaire(self,a):
        self.__salaire=a
    def __str__(self):
        return f"{super().__str__()}\nSalire:{self.getSalaire()}"
    def gains(self):
        return self.getSalaire()

class Travaialleur(Employe):
    def __init__(self,nom,prenom,salaire_mensuel,commission,quantite,):
        super().__init__(nom,prenom)
        self.__salaire_mensuel=salaire_mensuel
        self.commission=commission
        self.quantite=quantite
    def getSalaire_Mensuel(self):
        return self.__salaire_mensuel
    def setSalaire_Mensuel(self,a):
         self.__salaire_mensuel=a
    def getCommission(self):
        return self.commission
    def setCommission(self,a):
        self.commission=a
    def getQuantite(self):
        return self.quantite
    def setQuantite(self,a):
        self.quantite=a
    def __str__(self):
        return f"{super().__str__()}\nSalire Mensuel:{self.getSalaire_Mensuel()}\nCommission:{self.getCommission()}\nQuantite:{self.getQuantite()}"

    def gains(self):
        return self.getCommission()*self.getQuantite()+self.getSalaire_Mensuel()
class TravailleurHoraire(Employe):
    def __init__(self,nom,prenom,retribution,heures):
        super().__init__(nom,prenom)
        self.__retribution=retribution
        self.__heures=heures
    def getretribution(self):
        return self.__retribution
    def setretribution(self,a):
        self.__retribution=a
    def getHeures(self):
        return self.__heures
    def setHeures(self,a):
        self.__heures=a
    def __str__(self):
        return f"{super().__str__()}\nretribution:{self.getretribution()}\nle nombre d'heures:{self.getHeures()}"
    def gains(self):
        return self.getretribution()*self.getHeures()


Patron1=Patron("Lamrabet","Ayoub",90000)
Travailleur1=Travaialleur("Lamrabet","Youssef",30000,200,4)
TravailleurHoraire1=TravailleurHoraire("Lamrabet","Youssra",50,80*3)
print(Patron1,f"\nle salire de l'employe est :{Patron1.gains()}\n")
print(Travailleur1,f"\nle salaire de l'employe est : {Travailleur1.gains()}\n")
print(TravailleurHoraire1,f"\nle salaire de l'employe est : {TravailleurHoraire1.gains()}")





