from particula import Particula
import json


class AdminPartc:
    def __init__(self):
        self.__particulas = []
    
    def agregarFinal(self, particula:Particula):
        self.__particulas.append(particula)


    def agregarInicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)
    
    def __str__(self):
        return "".join(str(particula) + '\n' for particula in self.__particulas)
    
    def __len__(self):
        return len(self.__particulas)


    def __iter__(self):
        self.cont = 0;
        return self


    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration


    def hacerGrafo(self, x):
        grafo = dict()


        for particula in self.__particulas:
            origen = (particula.origenX, particula.origenY)
            destino = (particula.destinoX, particula.destinoY)
            if x == 1:
                peso = particula.distancia
            elif x == 2:
                peso = particula.velocidad


            aristaOD = (destino, peso)
            aristaDO = (origen, peso)


            if origen in grafo:
                grafo[origen].append(aristaOD)
            else:
                grafo[origen] = [aristaOD]
            
            if destino in grafo:
                grafo[destino].append(aristaDO)
            else:
                grafo[destino] = [aristaDO]


        return grafo


    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0


    def sort(self, op):
        if op == 1:
            return self.__particulas.sort()
        
        if op == 2:
            return self.__particulas.sort(key=sort_by_distancia, reverse=True)
        
        if op == 3:
            return self.__particulas.sort(key=lambda particula: particula.velocidad)
    
def sort_by_distancia(particula):
    return particula.distancia