# Este programa fue elaborado por Rangel Morales Oscar Mauricio y Rangel Romero Eric Alejandro 
# Materia: Algoritmos Computacionales 3NV40
# Profesor: Fernando Luque Marquez

#from collections import defaultdict
import os #importamos este modulo para poder limpiar la pantalla}
import time #este modulo nos va a permitir pausar la pantalla para poder observar mejor los cambios en el juego 
import random #modulo random para poder tener la generación inicial del juego de la vida
from collections import defaultdict # Nos permite crear nuestras porpias "Bibliotecas" la vamos a usar para guardar las condiciones de la celda y hacer las comparaciones

#función del juego
def juego():

    gen=int(input("¿Cuantas generaciones quiere ver?"))
    muerta = str('.')
    viva = str('x')    
    tabla = 25,25
    celda = defaultdict(int, {
    (1, 2): 1, # si tiene dos vecinas vivas, esta vive
    (1, 3): 1, # si tiene tres vecinas vivas, esta vive
    (0, 3): 1, # si tiene tres vecinas vivas, revive
    } ) # Condiciones para que viva
    
    ##
    ## Start States
    ##
    # blinker
    u = universe = defaultdict(int)
    u[(1,0)], u[(1,1)], u[(1,2)] = 1,1,1
    
    ## toad
    u = universe = defaultdict(int)
    u[(5,5)], u[(5,6)], u[(5,7)] = 1,1,1
    u[(6,6)], u[(6,7)], u[(6,8)] = 1,1,1
    
    ## glider
    u = universe = defaultdict(int)
    gen
    u[(5,5)], u[(5,6)], u[(5,7)] = 1,1,1
    u[(6,5)] = 1
    u[(7,6)] = 1
    
    ## random start
    universe = defaultdict(int, 
                        # array of random start values
                        ( ((row, col), random.choice((0,1)))
                            for col in range(tabla[0])
                            for row in range(tabla[1])
                        ) )  # returns 0 for out of bounds
    
    for i in range(gen):
        time_duration = 1.5
        time.sleep(time_duration)
        print("\nGeneración %3i:" % ( i+1, ))
        for row in range(tabla[1]):
            print("  ", ''.join(str(universe[(row,col)])
                                for col in range(tabla[0])).replace(
                                    '0', muerta).replace('1', viva))
        nextgeneration = defaultdict(int)
        for row in range(tabla[1]):
            for col in range(tabla[0]):
                nextgeneration[(row,col)] = celda[
                    ( universe[(row,col)],
                    -universe[(row,col)] + sum(universe[(r,c)]
                                                for r in range(row-1,row+2)
                                                for c in range(col-1, col+2) )
                    ) ]
        universe = nextgeneration

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
        juego()
    elif opc ==2: # Si la opción es 2 el juego se finaliza
        print("\n\n\n----------------->°°°°°\t Adios\t°°°°°<-----------------\n\n\n")
        SystemExit
    else:
        time_duration = 1.5        
        menu_principal()

menu_principal()