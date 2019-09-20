list_de_list = [
    ['Sebastian' , 'Ramirez', 'sebastian@correo.com'],
    ['Sandra' , 'Sanchez', 'sandra@correo.com'],
    ['Hermione' , 'Pots', 'hermion@correo.com']
]
diccionario = {}
lista_de_dic=[]
for convers in list_de_list:
    # Salida de convers = 
    #['Sebastian', 'Ramirez', 'sebastian@correo.com']
    #['Sandra', 'Sanchez', 'sandra@correo.com']
    #['Hermione', 'Pots', 'hermion@correo.com']

    #Establecemos la estructura del diccionario que se guardara en la lista vacia
    diccionario = {
        'nombre': convers[0],
        'apellido': convers[1],
        'correo': convers[2]
    }
    
    #Agregamos el diccinario en la lista vacia
    lista_de_dic.append(diccionario)

    #Mostramos la lista de lista con un arreglo bidimencional
print('lista de lista')
print('El nombre del tercer alumno es: {}'.format(list_de_list[2][0]))
print('El correo del segundo alumno es: {}'.format(list_de_list[1][2]))
print('El apellido del primer alumno es: {}'.format(list_de_list[0][1]))

#Mostramos la les de diccionarios usamos un indice y la "categoria"
print('lista de diccionario')
print('El nombre del tercer alumno es: {}'.format(lista_de_dic[2]['nombre']))
print('El correo del segundo alumno es: {}'.format(lista_de_dic[1]['correo']))
print('El apellido del primer alumno es: {}'.format(lista_de_dic[0]['apellido']))