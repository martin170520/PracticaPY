#Creando una lista (se peude modificar)
lista = ["Steven Perez","Soy Marven",True,1.68]
#Creando una tupla (no pueden modificar)
tupla = ("Steven Perez","Soy Marven",True,1.68)

#esto es valido
lista[3]="Maquinola"

#esto no
#tupla[3]="Maquinola"


#print(lista[3])
#print(tupla[3])

#Creando un conjunto(set) tambien no imprime duplicado
conjunto = {"Steven Perez","Soy Marven",True,1.68,"Soy Marven"}
#print(conjunto)
#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario(dict)(la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Steven Perez",
    'canal'  : "seventenn",
    'esta_emocionado' : True,
    'altura' : 1.68,
    'dato_duplicado' : "Marven"
}

print(diccionario['altura'])