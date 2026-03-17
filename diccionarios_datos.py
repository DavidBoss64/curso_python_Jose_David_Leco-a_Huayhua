#JOSE DAVID LECOÑA HUAYHUA 
#CI: 13828757
#DICCIONARIOS  -> ALMACEN A PARES DE CLAVE VALOR

mi_diccionario = {'nombre':'Bruno Diaz','edad':25, 'ciudad':'La Paz'}
print(mi_diccionario)


#ACCEDER A UN VALOR
print(mi_diccionario['nombre']) #  -->  Accediendo al campo 'nombre' de mi diccionario
print(mi_diccionario['ciudad'])

#AGREGAR UN ELEMENTO A UN DICCIONARIO
mi_diccionario['profesion']='Ingeniero'
print(mi_diccionario)

#ELIMINAR UN ELEMENTO
del mi_diccionario['ciudad']
print(mi_diccionario)

#OBTENER TODAS LA CLAVES DEL DICCIONARIO
print(mi_diccionario.keys())

##OBTENER VALORES DEL DICCIONARIO
print(mi_diccionario.values())


#VERIFICAR SI UNA CLAVE EXISTE

if 'edad' in mi_diccionario:
    print("Clave encontrada")
else:
    print('Clave no encontrada')

#RECORRIDO DE UN DICCIONARIO
for clave, valor in mi_diccionario.items():
    print("Clave: ",clave," Valor:",valor)