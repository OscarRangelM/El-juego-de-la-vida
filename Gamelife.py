# Este programa fue elaborado por Rangel Morales Oscar Mauricio y Rangel Romero Eric Alejandro 
# Materia: Algoritmos Computacionales 3NV40
# Profesor: Fernando Luque Marquez

#from collections import defaultdict
import os #importamos este modulo para poder limpiar la pantalla}
import time #este modulo nos va a permitir pausar la pantalla para poder observar mejor los cambios en el juego 
import random #modulo random para poder tener la generación inicial del juego de la vida
from collections import defaultdict # Nos permite crear nuestras porpias "Bibliotecas" la vamos a usar para guardar las condiciones de la celda y hacer las comparaciones

#función del juego
def juego(): # Función que genera el juego cuando se manda a llamar

    gen=int(input("¿Cuantas generaciones quiere ver?")) # Capturamos las generaciones a generar
    muerta = str('  ') # Como se va a ver una celula muerta
    viva = str('O ')  # Como se va a ver una celula viva  
    tabla = 15,15 #el tamaño de la tabla
    celda = defaultdict(int, { #funcion para definir las condiciones de la vida de las celulas
    (1, 2): 1, # si tiene dos vecinas vivas, esta vive
    (1, 3): 1, # si tiene tres vecinas vivas, esta vive
    (0, 3): 1, # si tiene tres vecinas vivas, revive
    } ) # Condiciones para que viva
    
    # Estados de comparació
    vartab = tabglobal = defaultdict(int) # Creamos un diccionario donde se indican los valores prederminados de las celdas vecinas
    gen
    vartab[(1,0)], vartab[(1,1)], vartab[(1,2)] = 1,1,1 #Estos valores predeterminados nos van a proporcionar los patrones principales como lo son el de la estrella (barra horizontal-vertical)
    vartab[(5,5)], vartab[(5,6)], vartab[(5,7)] = 1,1,1
    vartab[(6,6)], vartab[(6,7)], vartab[(6,8)] = 1,1,1
    vartab[(5,5)], vartab[(5,6)], vartab[(5,7)] = 1,1,1
    vartab[(6,5)] = 1
    vartab[(7,6)] = 1
    
    tabglobal = defaultdict(int, # arreglo para la generación aleatoria de la generación 0
                        ( ((fila, columna), random.choice((0,1))) 
                            for columna in range(tabla[0])
                            for fila in range(tabla[1])
                        ) )  # returns 0 for out of bounds
    
    for i in range(gen):
        time_duration = 0.5 # guardamos el tiempo que va haber entre generación y generación en una variable
        time.sleep(time_duration) # Usamos la funcion tiem.sleep de la biblioteca time para darle un tiempo entre generaciones
        print("\nGeneración %3i:" % ( i+1, )) # Imprimimos el número de generación para guiarnos de mejor manera
        for fila in range(tabla[1]): # En python el for se usa para hacer recorridos, en este caso vamos a recorrer los elementos de tabla 
            print("  ", ''.join(str(tabglobal[(fila,columna)]) 
                                for columna in range(tabla[0])).replace( # Remplazamos el valor de las celulas que mueren o que viven haciendo un recorrio con for
                                    '0', muerta).replace('1', viva))
        siguiente_gen = defaultdict(int) #
        for fila in range(tabla[1]): #recorrido de las filas
            for columna in range(tabla[0]): # recorrido de columna por columna
                siguiente_gen[(fila,columna)] = celda[ # En el arreglo siguiente_gen ingresamos los datos de filas por columnas uno por uno y es donde se realizan las comparaciones de los valores predeterminados en el diccionario tabglobal
                    ( tabglobal[(fila,columna)],
                    -tabglobal[(fila,columna)] + sum(tabglobal[(f,c)]
                                                for f in range(fila-1,fila+2)
                                                for c in range(columna-1, columna+2) )
                    ) ]
        tabglobal = siguiente_gen #ahora remplazamos los valores de la primer tabla por los nuevos valores ya remplazados con los diccionarios de la anterior 

    # Mini menú para continuar, terminar el juego o volver al inicio
    opc2 = int(input("\n\n¿Quiere volver a jugar? (1)\n¿Quiere terminar el juego? (2)\n¿Menú? (Cualquier otro número)\n"))
    if opc2 ==1: # Si la opción es 1 el juego se inicia
        print("Aquí va el juego o.O")
        juego()
    elif opc2 ==2: # Si la opción es 2 el juego se finaliza
        print("\n\n\n----------------->°°°°°\t Adios\t°°°°°<-----------------\n\n\n")
        SystemExit
    else:
        menu_principal()



#funcion de borrar pantalla para el menú
def borramos_pantalla():
    if os.name == "posix": # En caso de que el sistema en que se ejecuta este programa sea UNIX 
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos": # Si el sistema es DOS o windows   
        os.system ("cls")

#Función del menú principal
def menu_principal():
    borramos_pantalla()
    print("\n\n        Este es el juego de la vida de Conway       \n\n   Las reglas del juego son las siguientes:\n")
    print(" 1.- Si una celda esta viva y tiene dos o tres vecinas vivas, sobrevive\n")
    print(" 2.- Si una celda esta viva y tiene dos o tres vecinas vivas, puede renacer.\n")
    print(" 3.- Si una celda viva tiene mas de 3 vecinas vivas muere.\n\n")
    print("     ¿Quiere jugar? (1)\n     ¿Quiere salir? (2)\n")
    opc=int(input("\t\tOpción:")) # Declaramos la función opc para escoger una opción del menú
    if opc ==1: # Si la opción es 1 el juego se inicia
        print("Aquí va el juego o.O")
        juego() # Llamamos al juego
    elif opc ==2: # Si la opción es 2 el juego se finaliza
        print("\n\n\n----------------->°°°°°\t Adios\t°°°°°<-----------------\n\n\n")
        SystemExit # Terminamos el programa 
    else:
        time_duration = 0.5
        time.sleep(time_duration)      
        menu_principal()

menu_principal()
