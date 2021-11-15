from cola import Cola


class Arbol(object):

    def __init__(self, info=None,frecuencia=None, datos=None):
        self.info = info
        self.datos = datos
        self.frecuencia = frecuencia
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos = datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos =datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden()

    def añadir_descripcion(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.añadir_descripcion()
            print("La criatura a añadir descripcion es ",self.info)
            breve_descripcion = input ("Ingrese una descripcion ")
            self.datos["descripcion"] = breve_descripcion
            if(self.der is not None):
                self.der.añadir_descripcion()
    
    def añadir_captura(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.añadir_captura()
            print("La criatura a añadir por quien fue capturada es ",self.info)
            capturador = input ("Ingrese por quien fue capturada ")
            self.datos["capturada_por"] = capturador
            if(self.der is not None):
                self.der.añadir_captura()


    def inorden_derrotados_heracles(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_derrotados_heracles()  
            if (self.datos["derrotado_por"] == "Heracles"):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_derrotados_heracles()

    def inorden_no_derrotados(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_no_derrotados()  
            if (self.datos["derrotado_por"] == ""):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_no_derrotados()         

    def inorden_capturados_heracles(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_capturados_heracles()  
            if (self.datos["capturada_por"] == "Heracles"):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_capturados_heracles()                 

    def inorden_villanos(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_villanos()  
            if (self.datos["heroe"] == False):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_villanos()
    
    def inorden_trex(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_trex()  
            if (self.datos["nombre"] == "T-Rex"):  
                print(self.datos)
            if(self.der is not None):
                self.der.inorden_trex()
    
    def inorden_raptores(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_raptores()  
            if (self.datos["nombre"] == "Raptor"):  
                print(self.datos["zona_ubicacion"])
            if(self.der is not None):
                self.der.inorden_raptores()

    def inorden_descendente(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.inorden_descendente() 
            print(self.info, self.datos)    
            if(self.izq is not None):
                self.izq.inorden_descendente()    

    def inorden_descendente_heroe(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.inorden_descendente_heroe() 
            if (self.datos["heroe"] == True):
                print(self.info, self.datos)    
            if(self.izq is not None):
                self.izq.inorden_descendente_heroe()                        

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)
                    
    def busqueda_proximidad_heroes(self, clave):
        if(self.info is not None):
            if(self.datos["heroe"] == True):
                if(self.info[0:len(clave)] == clave):
                    print(self.info)
            if(self.izq is not None ):
                self.izq.busqueda_proximidad_heroes(clave)   
            if(self.der is not None):
                self.der.busqueda_proximidad_heroes(clave) 
                
    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None
        if(self.der is None):
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.datos = self.izq.datos
                self.der = self.izq.der
                self.izq = self.izq.izq
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contador(self):
        cont = 0
        if(self.info is not None):
            if(self.datos["heroe"]== True):
                cont += 1
            if(self.izq is not None):
                cont += self.izq.contador()
            if(self.der is not None):
               cont += self.der.contador()
        return cont

    def contador_nodos(self):
        cont = 0
        if(self.info is not None):  
            cont +=1 
            if(self.izq is not None):
                cont += self.izq.contador_nodos()
            if(self.der is not None):
                cont += self.der.contador_nodos()
        return cont

    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    

    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def contar_heroes(self,dic):
        if(self.info is not None):
            if (self.datos["derrotado_por"] and self.datos["derrotado_por"] in dic):
                dic[self.datos["derrotado_por"]] += 1
            elif (self.datos["derrotado_por"] and self.datos["derrotado_por"] not in dic):
                dic[self.datos["derrotado_por"]] = 1
            if(self.izq is not None):
                self.izq.contar_heroes(dic)
            if(self.der is not None):
                self.der.contar_heroes(dic)

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            if(nodo.info):
                print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)


    def dos_arboles(self,arbol_superheroes, arbol_villanos):
            if(self.info is not None):
                    if(self.datos['heroe'] == True):
                        arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                    else:
                        arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                    if(self.izq is not None):
                        self.izq.dos_arboles(arbol_superheroes, arbol_villanos)
                    if(self.der is not None):
                        self.der.dos_arboles(arbol_superheroes, arbol_villanos)





                    