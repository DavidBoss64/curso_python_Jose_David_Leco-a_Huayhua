#JOSE DAVID LECOÑA HUAYHUA 
#CI: 13828757

#METODOS DE LISTAS
numeros = [1,2,3,4,5]

#ADICIONAR ELEMENTOS A UNA LISTA
numeros.append(6)
print(numeros)

#ADICIONAR UN ELEMENTO EN UNA POSICION       
numeros.insert(0,-1)
print(numeros)

#Insertar numeros en la posicion 1
numeros.insert(1,0)
print(numeros)


#ELIMINAR UN ELEMENTO EN SU PRIMERA APARICION
numeros.remove(3) #Indicamos el valor del elemento eliminar
print(numeros)

numeros.remove(0)
print(numeros)

#VERIFICAR SU UN ELEMENTO SE ENCUENTRA EN LA LISTA
print(8 in numeros)  #Devuelve un valor booleano

#OBTENER EL TAMAÑO DE LA LISTA
print(f"La longitud de la lista es, {len(numeros)}")

#ELIMINAR EL CONTENIDO DE LA LISTA
numeros.clear()
print(numeros)

