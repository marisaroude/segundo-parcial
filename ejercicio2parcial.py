"""Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
necesarios para resolver las tareas, listadas a continuación:
1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
Hat, Debian, Arch;
3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
Debian y Red Hat, hasta el servidor “MongoDB”;
4. encontrar el árbol de expansión mínima;
5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
realice un barrido en profundidad para corroborar que efectivamente fue borrada;
6. debe utilizar un grafo no dirigido."""

from grafo import Grafo 
from cola import Cola

red = Grafo(dirigido = False ) #Grafo no dirigido.

red.insertar_vertice("Ubuntu", data ="PC")
red.insertar_vertice("Impresora", data ="Impresora")
red.insertar_vertice("Mint", data ="PC")
red.insertar_vertice("Switch1", data ="Switch")
red.insertar_vertice("Debian", data ="Notebook")
red.insertar_vertice("Router1", data ="Router")
red.insertar_vertice("Router2", data ="Router")
red.insertar_vertice("Router3", data ="Router")
red.insertar_vertice("Red Hat", data ="Notebook")
red.insertar_vertice("Guarani", data ="Servidor")
red.insertar_vertice("Manjaro", data ="PC")
red.insertar_vertice("Switch2", data ="Switch")
red.insertar_vertice("Fedora", data ="PC")
red.insertar_vertice("Parrot", data ="PC")
red.insertar_vertice("MongoDB", data ="Servidor")
red.insertar_vertice("Arch", data ="Notebook")


red.insertar_arista(17,"Switch1","Debian")
red.insertar_arista(18,"Switch1","Ubuntu")
red.insertar_arista(22,"Switch1","Impresora")
red.insertar_arista(80,"Switch1","Mint")
red.insertar_arista(29,"Switch1","Router1")
red.insertar_arista(37,"Router1","Router2")
red.insertar_arista(43,"Router1","Router3")
red.insertar_arista(25,"Router2","Red Hat")
red.insertar_arista(9,"Router2","Guarani")
red.insertar_arista(50,"Router2","Router3")
red.insertar_arista(61,"Router3","Switch2")
red.insertar_arista(3,"Switch2","Fedora")
red.insertar_arista(56,"Switch2","Arch")
red.insertar_arista(5,"Switch2","MongoDB")
red.insertar_arista(12,"Switch2","Parrot")
red.insertar_arista(40,"Switch2","Manjaro")

#2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red Hat, Debian, Arch;
buscado = "Red Hat"
origen = red.buscar_vertice(buscado)
print("Barrido en profundidad desde Red Hat: ")
red.barrido_profundidad(origen)
red.marcar_no_visitado()
print()
print("Barrido en amplitud desde Red Hat:")
red.barrido_amplitud(origen)
red.marcar_no_visitado()
print()

buscado2 = "Debian"
origen2 = red.buscar_vertice(buscado2)
print("Barrido en profundidad desde Debian: ")
red.barrido_profundidad(origen2)
red.marcar_no_visitado()
print()
print("Barrido en amplitud desde Debian:")
red.barrido_amplitud(origen2)
red.marcar_no_visitado()
print()


buscado3 = "Arch"
origen3 = red.buscar_vertice(buscado3)
print("Barrido en profundidad desde Arch: ")
red.barrido_profundidad(origen3)
red.marcar_no_visitado()
print()
print("Barrido en amplitud desde Arch:")
red.barrido_amplitud(origen3)
red.marcar_no_visitado()
print()


#3. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Debian y Red Hat, hasta el servidor “MongoDB”;
buscado1 = "Debian"
origen = red.buscar_vertice(buscado1)
buscado2 = "MongoDB"
destino = red.buscar_vertice(buscado2)
camino = red.dijkstra(origen,destino)
print("Camino mas corto para enviar a imprimir un documento desde la pc Debian hasta el MongoDB ")
destino = buscado2
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino desde Debian a Mongo DB es:', costo)
print()

buscado1 = "Red Hat"
origen = red.buscar_vertice(buscado1)
buscado2 = "MongoDB"
destino = red.buscar_vertice(buscado2)
camino = red.dijkstra(origen,destino)

destino = buscado2
costo = None
print("Camino mas corto para enviar a imprimir un documento desde la pc Red Hat hasta el MongoDB ")
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino desde Red Hat a Mongo DB es:', costo)
print()

#4. encontrar el árbol de expansión mínima;
bosque = red.prim()
print('Arbol de expansion mínimo')
peso = 0
for elemento in bosque:
    print(elemento[1][0], '-', elemento[1][1])
    peso += elemento[0]
print('Costo total', peso)
print()

#5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y realice un barrido en profundidad para corroborar que efectivamente fue borrada;
red.eliminar_vertice("Impresora")
buscado = "Switch1"
origen = red.buscar_vertice(buscado)
print("Barrido sin la impresora ")
red.barrido_profundidad(origen)



