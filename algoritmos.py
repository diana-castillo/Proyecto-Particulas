import math
from collections import deque
from queue import PriorityQueue


def distanciaEuclidiana(x1, x2, y1, y2):
    resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return math.floor(resultado)


def busquedaProfundidad(grafo, origen):
    visitados = []
    pila = deque()
    recorrido = []


    visitados.append(origen)
    pila.append(origen)


    while len(pila) > 0:
        vertice = pila[-1]
        recorrido.append(vertice)
        pila.pop()
        adyacentes = grafo.get(vertice)


        for i in range (len(adyacentes)):
            ady = adyacentes[i][0]


            if ady not in visitados:
                visitados.append(ady)
                pila.append(ady)
    return recorrido


def busquedaAmplitud(grafo, origen):
    visitados = []
    cola = deque()
    recorrido = []


    visitados.append(origen)
    cola.append(origen)


    while len(cola) > 0:
        vertice = cola[0]
        recorrido.append(vertice)
        cola.popleft()
        adyacentes = grafo.get(vertice)


        for i in range (len(adyacentes)):
            ady = adyacentes[i][0]


            if ady not in visitados:
                visitados.append(ady)
                cola.append(ady)
    return recorrido


def aristaAGrafo(arista, grafoResultante):
    origen = arista[1][0]
    destino = arista[1][1]
    peso = arista[0]


    aristaOD = (destino, peso)
    aristaDO = (origen, peso)


    if origen in grafoResultante:
        grafoResultante[origen].append(aristaOD)
    else:
        grafoResultante[origen] = [aristaOD]
    if destino in grafoResultante:
        grafoResultante[destino].append(aristaDO)
    else:
        grafoResultante[destino] = [aristaDO]


def algoritmoPrim(grafo, nodoInicial):
    grafoResultante = dict()
    visitados = []
    pq = PriorityQueue()


    visitados.append(nodoInicial)
    adyacentes = grafo.get(nodoInicial)


    for i in range (len(adyacentes)):
        origen = nodoInicial
        destino = adyacentes[i][0]
        distancia = adyacentes[i][1]
        arista = (distancia, (origen, destino))
        pq.put(arista)


    while not pq.empty():
        arista = pq.get()
        destino = arista[1][1]


        if destino not in visitados:
            visitados.append(destino)
            adyacentes = grafo.get(destino)


            for i in range (len(adyacentes)):
                origenD = destino
                destinoD = adyacentes[i][0]
                distancia = adyacentes[i][1]
                aristaD = (distancia, (origenD, destinoD))
                ady = aristaD[1][1]
                if ady not in visitados:
                    pq.put(aristaD)
            
            aristaAGrafo(arista, grafoResultante)
    return grafoResultante


def findSet(lista, nodo):
    for sublista in lista:
        for i in range (len(sublista)):
            if sublista[i] == nodo:
                return sublista


def algoritmoKruskal(grafo):
    grafoResultante = dict()
    listaOrdenada = []
    disjointSet = []
    aristasDO = []


    for vertice in grafo:
        adyacentes = grafo.get(vertice)


        for i in range (len(adyacentes)):
            origen = vertice
            destino = adyacentes[i][0]
            velocidad = adyacentes[i][1]
            arista = (velocidad, (origen, destino))


            if arista not in aristasDO:
                listaOrdenada.append(arista)
                aristasDO.append((velocidad, (destino, origen)))


        disjointSet.append([vertice])


    print(disjointSet)
    listaOrdenada.sort()


    while len(listaOrdenada) > 0:
        arista = listaOrdenada.pop()
        print("arista: ", arista)
        origen = arista[1][0]
        destino = arista[1][1]
        
        conjunto1 = findSet(disjointSet, origen)
        conjunto2 = findSet(disjointSet, destino)


        if conjunto1 != conjunto2:
            aristaAGrafo(arista, grafoResultante)
            
            nuevoConjunto = conjunto1 + conjunto2
            disjointSet.append(nuevoConjunto)
            disjointSet.remove(conjunto1)
            disjointSet.remove(conjunto2)
        print(disjointSet)
    return grafoResultante


def algoritmoDijkstra(grafo, nodoOrigen, nodoDestino):
    arregloDistancias = dict()
    arregloCamino = dict()
    pq = PriorityQueue()
    grafoResultante = dict()


    for nodo in grafo:
        if nodo == nodoOrigen:
            arregloDistancias[nodo] = 0
            arregloCamino[nodo] = nodo
        else:
            arregloDistancias[nodo] = math.inf
            arregloCamino[nodo] = ''


    pq.put((0, nodoOrigen))


    while not pq.empty():
        n = pq.get()
        nodoN = n[1]
        adyacentes = grafo.get(nodoN)


        for i in range (len(adyacentes)):
            nDestino = adyacentes[i][0]
            distanciaDestino = adyacentes[i][1]
            distanciaNodoN = arregloDistancias[nodoN]
            sumaDistancias = distanciaDestino + distanciaNodoN
            distDestinoArreglo = arregloDistancias[nDestino] 
            
            if sumaDistancias < distDestinoArreglo:
                arregloDistancias[nDestino] = sumaDistancias
                arregloCamino[nDestino] = nodoN
                pq.put((sumaDistancias, nDestino))


    for nodo in arregloCamino:
        if nodo == nodoDestino:
            while nodo != nodoOrigen:
                destino = arregloCamino[nodo]
                if nodo in grafoResultante:
                    grafoResultante[nodo].append(destino)
                else:
                    grafoResultante[nodo] = [destino]
                if destino in grafoResultante:
                    grafoResultante[destino].append(nodo)
                else:
                    grafoResultante[destino] = [nodo]
                nodo = arregloCamino[nodo]


    return arregloDistancias, arregloCamino, grafoResultante