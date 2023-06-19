from algoritmos import distanciaEuclidiana


class Particula:
    def __init__(self, id = 0, origenX = 0, origenY = 0, destinoX = 0, destinoY = 0,
                velocidad = 0, red = 0, green = 0, blue = 0):
        self.__id = id
        self.__origenX = origenX
        self.__origenY = origenY
        self.__destinoX = destinoX
        self.__destinoY = destinoY
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distanciaEuclidiana(origenX, destinoX, origenY, destinoY)


    def __str__(self):
        return ('Id: ' + str(self.__id) + '\n' + 'Origen en X: ' + str(self.__origenX) + '\n' + 
            'Origen en Y: ' + str(self.__origenY) + '\n' + 'Destino en X: ' + str(self.__destinoX) + '\n' + 
            'Destino en Y: ' + str(self.__destinoY) + '\n' + 'Velocidad: ' + str(self.__velocidad) + '\n' + 
            'Red: ' + str(self.__red) + '\n' + 'Green: ' + str(self.__green) + '\n' + 'Blue: ' + str(self.__blue) + '\n' + 
            'Distancia: ' + str(self.__distancia) + '\n')


    def __lt__(self, other):
        return self.id < other.id


    @property
    def id(self):
        return self.__id
        
    @property
    def origenX(self):
        return self.__origenX
    
    @property
    def origenY(self):
        return self.__origenY
    
    @property
    def destinoX(self):
        return self.__destinoX
    
    @property
    def destinoY(self):
        return self.__destinoY
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red
    
    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue
    
    @property
    def distancia(self):
        return self.__distancia
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origenX": self.__origenX,
            "origenY": self.__origenY,
            "destinoX": self.__destinoX,
            "destinoY": self.__destinoY,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
