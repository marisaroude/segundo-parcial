"""El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
resolver los siguientes requerimientos:
1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
distintos, los códigos no pueden ser repetidos (tenga cuidado);
2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
código;
3. realizar un barrido en orden del árbol ordenado por nombre;
4. mostrar toda la información del dinosaurio 00792;
5. mostrar toda la información de todos los T-Rex que hay en la isla;
6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
cargado, su nombre correcto es Stygimoloch;
7. mostrar la ubicación de todos los Raptores que hay en la isla;
8. contar cuantos Diplodocus hay en el parque;
9. debe cargar al menos 15 elementos."""

from arbol_binario import Arbol 

arbol_nombre = Arbol()
arbol_codigo = Arbol()

dinosaurios = {"nombre": "Sgimoloch", "codigo": "15981","zona_ubicacion":"5A"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "T-Rex", "codigo": "14561","zona_ubicacion":"7B"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "T-Rex", "codigo": "00792","zona_ubicacion":"6B"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "T-Rex", "codigo": "75321","zona_ubicacion":"3A"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Diplodocus", "codigo": "94619","zona_ubicacion":"5E"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Diplodocus", "codigo": "00001","zona_ubicacion":"4H"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Diplodocus", "codigo": "32105","zona_ubicacion":"3F"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Diplodocus", "codigo": "55544","zona_ubicacion":"9R"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Raptor", "codigo": "33366","zona_ubicacion":"4W"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Raptor", "codigo": "99987","zona_ubicacion":"0G"}
arboarbol_nombrel = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Raptor", "codigo": "65897","zona_ubicacion":"8G"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Raptor", "codigo": "10203","zona_ubicacion":"7Q"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Dino", "codigo": "60785","zona_ubicacion":"3L"}
arbarbol_nombreol = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Dino", "codigo": "00169","zona_ubicacion":"8H"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)
dinosaurios = {"nombre": "Dino", "codigo": "46800","zona_ubicacion":"2E"}
arbol_nombre = arbol_nombre.insertar_nodo(dinosaurios["nombre"],dinosaurios)
arbol_codigo = arbol_codigo.insertar_nodo(dinosaurios["codigo"],dinosaurios)

#3. realizar un barrido en orden del árbol ordenado por nombre;
print("Barrido inorden del arbol ordenado por nombre")
arbol_nombre.inorden()
print()

#4. mostrar toda la información del dinosaurio 00792;
buscado = "00792"
pos = arbol_codigo.busqueda(buscado)
if pos:
    print ("Info del dinosaurio con el codigo:",buscado," ",pos.datos)
print()


#5. mostrar toda la información de todos los T-Rex que hay en la isla;
print("Todos los T-rex que hay en la lista son: ")
arbol_nombre.inorden_trex()
print()

#6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal cargado, su nombre correcto es Stygimoloch;
buscado = "Sgimoloch"
pos = arbol_nombre.busqueda(buscado)

if pos:
    nuevo_nombre = input("Ingrese el nuevo nombre de Sgimoloch: ")
    nombre, criaturas = arbol_nombre.eliminar_nodo(buscado)
    dinosaurios["nombre"] = nuevo_nombre
    arbol = arbol_nombre.insertar_nodo(nuevo_nombre,dinosaurios)
print()
print("Barrido con el nombre de Sgimoloch cambiado:")
arbol_nombre.inorden()
print()

#7. mostrar la ubicación de todos los Raptores que hay en la isla;
print("Ubicacion de los raptores: ")
arbol_nombre.inorden_raptores()
print()

#8. contar cuantos Diplodocus hay en el parque;
print("La cantidad de Diplodocus que hay en el parque son: ",arbol_nombre.contar_ocurrencias("Diplodocus"))