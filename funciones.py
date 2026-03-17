#JOSE DAVID LECOÑA HUAYHUA 
#CI: 13828757

#FUNCIONES - Son bloques de codig que realiza una tarea especifica y que son reutilizables


#Funcion sin parametros ni devolucion de valor
def saludar():
    print("Hola Bienvenidos al curso de Python")


#Funciones con parametros
def saludo(nombre):
    print(f"Hola {nombre} bienvenido a clases")


#FUNCION QUE DEVUELVE VALORES
def suma(a,b):
    return a+b

#ESTABLECER VALORES POR DEFECTO PARA LOS PARAMETROS DE UNA FUNCION
def bienvenida(nombre = "Estudiante"):
    print("Bienvendido ", nombre)

#FUNCION CON ARGUMENTOS VARIABLES
def sumador(*args):
    return sum(args)


#Llamada a la funcion
saludo("David Huayhua")
saludo("Andres Valencia")

resultado = suma(10,20)
print("La suma es: ", resultado)

bienvenida()
bienvenida("David")

print(sumador(1,2,3,4,5,6))
print(sumador(6,2,1))