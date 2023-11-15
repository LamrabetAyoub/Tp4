class Point:
    def __init__ (self,x,y):
     self.__x=x
     self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,a):
        self.__x=a     
    def setY(self,a):
        self.__y=a  
    def __str__(self) :
        return f"les cordonnées de point :({self.__x},{self.__y})"
class Rectangle(Point):
    def __init__(self,x,y, lar, long):
        super().__init__(x, y)
        self.__lar=lar
        self.__long=long
    def getLar(self):
        return self.__lar
    def getLong(self):
        return self.__long
    def setLar(self,a):
        self.__lar=a
    def setLong(self,a):
        self.__long=a
    def aire(self):
        return self.__long*self.__lar
    def __str__(self) :
        return f"l'air de rectangle de cordonnées ({self.__x},{self.getY()}) et de largeur:{self.__lar}et de longuer:{self.__y} est :{self.aire()}"
class Paralilopipete(Rectangle):
    def __init__(self, x, y, lar, long,h):
        super().__init__(x,y,lar,long)
        self.__h=h
    def getH(self):
        return self.__h
    def setH(self,a):
         self.__h=a
    def aire(self):
        return 2*self.__h*self.__long +2*self.__h*self.__lar+2*self.__long*self.__lar
    def volume(self):
        return self.__h*self.__long*self.__lar
    def __str__(self):
        return f"parallélépipède de cordonnées ({self.__x},{self.__y})\nlongueur :{self.__long} \nlargeur:{self.__lar}\Surface:{self.aire(self)}\nVolume:{self.volume} "
        


