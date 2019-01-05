import numpy as np
import math
import random

ops = ["+", "-", "*", "/", "max", "min"]
tam = 128
arbol = [None for i in range(tam)]

#Estos son los valores que le damos al arbol con el que se realizan los test
arbol[0] = "+"
arbol[1] = "+"
arbol[2] = "*"
arbol[3] = "+"
arbol[4] = 3
arbol[5] = "+"
arbol[6] = "/"
arbol[7] = "x"
arbol[8] = "y"
arbol[9] = None
arbol[10] = None
arbol[11] = "y"
arbol[12] = 1
arbol[13] = "x"
arbol[14] = 2

def printArbol(arbol, index=0, cant=1):
  cpy = cant
  while cpy > 0:
    if index == tam - 1:
      print("")
      return
    print(str(arbol[index]), end = ' ')
    index += 1
    cpy -= 1
  print("")
  cant = 2*cant
  printArbol(arbol, index, cant)

printArbol(arbol)

#Asumiendo que el arbol esta indexado desde 0
def hijoIzq(index):
  return 2*index + 1

def hijoDer(index):
  return 2*index + 2

def cantNodos(arbol):
  cont = 0
  for nodo in arbol:
    if nodo != None:
      cont+=1
  return cont

#arbol[0] son los nodos del arbol y arbol[1] es la cantidad de nodos que tiene
def isLeaf(arbol, index):
  return arbol[hijoIzq(index)] == None and arbol[hijoDer(index)] == None

#Borra el subarbol desde que inicia en index
def borrarSubarbol(arbol, index):
  if arbol[index] == None:
    return
  else:
    arbol[index] = None
    if isLeaf(arbol, index):
      return
    borrarSubarbol(arbol, hijoIzq(index))
    borrarSubarbol(arbol, hijoDer(index))

def copiarSubarbol(source_arbol, target_arbol, source, target):
  if source_arbol[source] == None:
    return
  else:
    target_arbol[target] = source_arbol[source]
    copiarSubarbol(source_arbol, target_arbol, hijoIzq(source), hijoIzq(target))
    copiarSubarbol(source_arbol, target_arbol, hijoDer(source), hijoDer(target))

#Parent1 es el target, mientras que parent2 es el source
def subTreeCrossOver(parent1, parent2):
  source = random.randint(1,cantNodos(parent1))
  target = random.randint(1,cantNodos(parent2))
  #Copia de arbol, en la que trabajaremos
  source_tree = list.copy(parent1)
  #Salvamos el subarbol de source
  target_tree = list.copy(parent2)
  #borramos el subardol que comienza en target
  borrarSubarbol(source_tree, target)
  #copiamos todos los nodos desde el subarbol que comienza en source al subarbol que comienza en target
  copiarSubarbol(source_tree, target_tree, source, target)
  return source_tree 

arcopia = subTreeCrossOver(arbol, arbol)
printArbol(arcopia)
printArbol(arbol)
