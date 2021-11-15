from lista import Lista
from cola import Cola
from heap import HeapMin
from pila import Pila
from math import inf
from copy import deepcopy


class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.inicio = Lista()

    def insertar_vertice(self, dato, criterio='info', data=None):  # ! agregar otro
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista(), 'data': data}, criterio)


    def insertar_arista(self, peso, origen, destino, criterio='destino', data=None):  # ! agregar otro
        ver_origen = self.inicio.busqueda(origen, 'info')
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino, 'data': data}, criterio)
            if(not self.dirigido and origen != destino):
                data_aux = deepcopy(data)
                if(data):
                    data_aux['relacion'].reverse()
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen, 'data': data_aux}, criterio)
        else:
            print('los vertices origen o destino no estan en el grafo....', origen, destino)

    def grafo_vacio(self):
        return self.inicio.lista_vacia()

    def tamanio(self):
        return self.inicio.tamanio()
    
    def buscar_vertice(self, clave, criterio='info'):
        return self.inicio.busqueda(clave, criterio=criterio)

    def buscar_arista(self, origen, destino, criterio='destino'):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            return self.inicio.obtener_elemento(ver_origen)['aristas'].busqueda(destino, criterio)
        else:
            return ver_origen

    def barrido_vertices(self):
        self.inicio.barrido()

    def es_adyacente(self, origen, destino):
        """Relacion directa"""
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            destino = self.buscar_arista(origen, destino)
            if(destino != -1):
                return True
            else:
                return False
        else:
            return False

    def adyacentes(self, origen):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()
    
    def adyacentes_antecesores(self, origen):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()

    def eliminar_vertice(self, clave):
        aux = self.inicio.eliminar(clave, criterio='info')
        for posicion in range(self.tamanio()):
            origen = self.inicio.obtener_elemento(posicion)['info']
            self.eliminar_arista(origen, clave)
        return aux


    def eliminar_arista(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].eliminar(destino, 'destino')
            if(not self.dirigido):
                ver_destino = self.inicio.busqueda(destino, 'info')
                if(ver_destino != -1):
                    self.inicio.obtener_elemento(ver_destino)['aristas'].eliminar(origen, 'destino')

                    
    def barrido_profundidad(self, ver_origen):
        """Barrido en profundidad del grafo."""
        while(ver_origen < self.inicio.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                print(vertice['info'])
                aristas = 0
                while(aristas < vertice['aristas'].tamanio()):
                    arista = vertice['aristas'].obtener_elemento(aristas)
                    pos_vertice = self.buscar_vertice(arista['destino'])
                    nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                    if(not nuevo_vertice['visitado']):
                        self.barrido_profundidad(pos_vertice)
                    aristas += 1
            ver_origen += 1

    def barrido_amplitud(self, ver_origen):
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(ver_origen < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                cola.arribo(vertice)
                while(not cola.cola_vacia()):
                    nodo = cola.atencion()
                    print(nodo['info'], nodo['data'])
                    aristas = 0
                    while(aristas < nodo['aristas'].tamanio()):
                        adyacente = nodo['aristas'].obtener_elemento(aristas)
                        pos_vertice = self.buscar_vertice(adyacente['destino'])
                        nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                        if(not nuevo_vertice['visitado']):
                            nuevo_vertice['visitado'] = True
                            cola.arribo(nuevo_vertice)
                        aristas += 1
            ver_origen += 1


    def marcar_no_visitado(self):
        """Marca todos losvertices del grafo como no visitados."""
        for i in range(self.tamanio()):
            self.inicio.obtener_elemento(i)['visitado'] = False

    def existe_paso(self, ver_origen, ver_destino):
        """Barrido en profundidad del grafo."""
        resultado = False
        vertice = self.inicio.obtener_elemento(ver_origen)
        if(not vertice['visitado']):
            vertice['visitado'] = True
            aristas = 0
            while(aristas < vertice['aristas'].tamanio() and not resultado):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = self.buscar_vertice(arista['destino'])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                destino = self.inicio.obtener_elemento(ver_destino)
                if(nuevo_vertice['info'] == destino['info']):
                    return True
                else:
                    resultado = self.existe_paso(pos_vertice, ver_destino)
                aristas += 1
        return resultado

    def dijkstra(self, ver_origen, ver_destino):
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        no_visitados = HeapMin()
        camino = Pila()
        aux = 0
        while(aux < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            vertice_aux = self.inicio.obtener_elemento(aux)
            vertice_aux['anterior'] = None
            if(vertice_aux['info'] == vertice['info']):
                no_visitados.arribo([vertice_aux['info'], None], 0)
            else:
                no_visitados.arribo([vertice_aux['info'], None], inf)
            aux += 1
        while(not no_visitados.vacio()):
            dato = no_visitados.atencion()
            camino.apilar(dato)
            pos_aux = self.buscar_vertice(dato[1][0])
            vertice_aux = self.inicio.obtener_elemento(pos_aux)
            aristas = 0
            while(aristas < vertice_aux['aristas'].tamanio()):
                arista = vertice_aux['aristas'].obtener_elemento(aristas)
                pos_heap = no_visitados.busqueda(arista['destino'])
                if(pos_heap is not None and no_visitados.elementos[pos_heap][0] > dato[0] + arista['peso']):
                    no_visitados.elementos[pos_heap][1][1] = dato[1][0]
                    nuevo_peso = dato[0] + arista['peso']
                    no_visitados.cambiar_prioridad(pos_heap, nuevo_peso)
                aristas += 1
        # print(no_visitados.elementos)
        return camino

    def busqueda_prim(self, bosque, buscado):
        for elemento in bosque:
            if(buscado in elemento[1]):
                return elemento


    def prim(self):
        """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = HeapMin()
        origen = self.inicio.obtener_elemento(0)
        adyac = 0
        while(adyac < origen['aristas'].tamanio()):
            arista = origen['aristas'].obtener_elemento(adyac)
            aristas.arribo([origen['info'], arista['destino']], arista['peso'])
            adyac += 1
        # print(bosque)
        # print(aristas.elementos)
        # print()
        while(len(bosque) // 2 < self.tamanio() and not aristas.vacio()):
            dato = aristas.atencion()
            if(len(bosque) == 0) or ((self.busqueda_prim(bosque, dato[1][0]) is not None) ^ (self.busqueda_prim(bosque, dato[1][1]) is not None)):
                bosque.append(dato)
                pos_vertice = self.buscar_vertice(dato[1][1])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                adyac = 0
                while(adyac < nuevo_vertice['aristas'].tamanio()):
                    arista = nuevo_vertice['aristas'].obtener_elemento(adyac)
                    # print(arista)
                    aristas.arribo([nuevo_vertice['info'], arista['destino']], arista['peso'])
                    adyac += 1
            # print(bosque)
            # print(aristas.elementos)
            # a = input()
        return bosque

    def relaciones(self, clave,data = None):
        """devuelve relacion especifica"""
        origen = self.buscar_vertice(clave)
        if (origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(i)
                if(data in arista['data']['relacion'][-1]): 
                    print(arista["destino"])            
        else:
            print('dios no encontrado')
            
    
    def relaciones2(self, clave,data = None, lista = None):
        """devuelve relacion especifica"""
        origen = self.buscar_vertice(clave)
        if (origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(i)
                if(data in arista['data']['relacion'][-1]): 
                    if (not arista["destino"] in lista):
                        print(arista["destino"])
                        lista.append(arista["destino"])          
        else:
            print('dios no encontrado')

    def relaciones_nietos(self, clave,data = None, lista =None):
        """devuelve relacion especifica"""
        origen = self.buscar_vertice(clave)
        if (origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                arista = dios['aristas'].obtener_elemento(i)
                if(data in arista['data']['relacion'][-1]):
                    self.relaciones2(arista["destino"],"hijo",lista) 
        else:
            print('dios no encontrado')


    def ancestro(self,vertice_nombre):
        """Muestra los ancestros de un determinado dios"""
        origen = self.buscar_vertice(vertice_nombre)
        if(origen != -1):
            dios = self.inicio.obtener_elemento(origen)
            for i in range(dios['aristas'].tamanio()):
                nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
                dios_aux = dios['aristas'].obtener_elemento(i)['data']
                if(len(dios_aux['relacion']) > 1):
                    if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                        print(nombre_dios, dios_aux['relacion'])
                        self.ancestro(nombre_dios)
    
    def barrido_dios_madre(self):
        """Barrido que muestra la madre de cada dios"""
        for i in range(self.tamanio()):
            dios = self.inicio.obtener_elemento(i)
            aux = dios['info']        
            for j in range(dios['aristas'].tamanio()):
                nombre_madre = dios['aristas'].obtener_elemento(j)['destino']
                madre_aux = dios['aristas'].obtener_elemento(j)['data']
                if(len(madre_aux['relacion']) > 1):
                    if(madre_aux['relacion'][1] == 'madre' ):
                        print("dios: ",aux," su madre es: ",nombre_madre)    