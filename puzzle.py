from collections import deque

class Nodo:
    def __init__(self, datos, padre=None):
        self.datos = datos  # Estado actual
        self.padre = padre  # Nodo padre
    
    def get_datos(self):
        return self.datos
    
    def get_padre(self):
        return self.padre
    
    def en_lista(self, lista_nodos):
        return any(self.datos == nodo.datos for nodo in lista_nodos)

def buscar_solucion(estado_inicial, solucion, metodo):
    if metodo == "DFS_REC":
        return dfs_recursivo(Nodo(estado_inicial), solucion, [])
    
    solucionado = False
    nodos_visitados = []
    nodos_frontera = deque() if metodo == "BFS" else []  # Cola para BFS, Pila para DFS
    
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.popleft() if metodo == "BFS" else nodos_frontera.pop()
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        
        # Expandir nodos hijo
        dato_nodo = nodo.get_datos()
        
        hijos = [
            [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]],  # Izquierdo
            [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]],  # Central
            [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]   # Derecho
        ]
        
        for hijo in hijos:
            nodo_hijo = Nodo(hijo, nodo)
            if not nodo_hijo.en_lista(nodos_visitados) and not nodo_hijo.en_lista(nodos_frontera):
                nodos_frontera.append(nodo_hijo)
    
    return None  # No hay solución

def dfs_recursivo(nodo, solucion, visitados):
    if nodo.get_datos() == solucion:
        return nodo
    visitados.append(nodo)
    
    dato_nodo = nodo.get_datos()
    hijos = [
        [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]],  # Izquierdo
        [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]],  # Central
        [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]   # Derecho
    ]
    
    for hijo in hijos:
        nodo_hijo = Nodo(hijo, nodo)
        if not nodo_hijo.en_lista(visitados):
            resultado = dfs_recursivo(nodo_hijo, solucion, visitados)
            if resultado:
                return resultado
    
    return None

def ejecutar_metodo(metodo, estado_inicial, solucion):
    nodo_solucion = buscar_solucion(estado_inicial, solucion, metodo)
    
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        return resultado  # 
    
    return ["No se encontró solución."]  # 
