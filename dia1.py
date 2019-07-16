print(2+2)
print(2+4)
print(3*6)
print(32+8)
print(76/3)


#la union de palabra mas numeros
print("hola mundo!") #usar comillas para palabras 

print("hola"*55) #multiplica las palabras 

print("hola"+"feliz dia") #unen (+) las palabras

a = "hola"#si la variable equivale a un texto debe ir entre comillas
b=10
print(a*b)# a y b son variables por eso no hace falta poner comillas

c=12

d=10

print(c+d)# suma de variables

print(c,d)

print("hola",c,"feliz")# la coma separa los textos 

#ejercicios  crear una variable nombre,edad
#con sus nombre edad y despues imprimir 
#hola me llamo nestor y tengo 27 ahos

nombre="Nestor"

edad=27

print("hola me llamo",nombre,"y tengo",edad,"ahos")#las variables y los textos se van separando con la coma 

#crear una variable hobby con tu pasatiempo
#imprimir 
#hola, me llamo---- tengo ahos mi hobby es...y mi pasatiempo es

hobby="bailar "

pasatiempo=" hacer ejercicios"

print("hola me llamo",nombre,"tengo",edad,"anhos","mi hobby es",hobby,"y mi pasatiempo es",pasatiempo)


#listas en las listas podemos cargar varios elementos debe ir entre corchete y cada elemento separados por comas

#print(listax)

datos=["nestor",27]#los indices de las listas empiezan desde cero

#ej-crear una lista que en el primer lugar este tu nombre 

#y en el segundo lugar este tu edad 

#imprimir "hola me llamo ---y tengo ..... ahos "

print("hola me llamo",datos[0],"y tengo",datos[1],"anhos")

print("hola todos me llamo",datos[0])

#como modificar un elemento de una lista

datos[1]=33#sirve para modificar un elemento



print("hola mi nombre es",datos[0],"y tengo",datos[1],"ahos")

datos[0]="sebastian"

print("hola mi nombre es",datos[0],"y tengo",datos[1],"ahos")

#como puedo agregar un elemto o mas a mi lista..utilizamos append

#ejercicios .agr una profesion y un hobyy a la lista datos 

# imprimir la lista

datos.append("lic en ciencias de la edc.")#sirve para agregar elementos a la lista

print(datos)

datos.append("bailar")

print(datos)

datos[3]="bailar"

print(datos)

print("yo me llamo",datos[0],"tengo",datos[1],"anhos","mi profesion es",datos[2],"y mi hobby es",datos[3])

#como borrar un elemto de la lista....utilizamos pop.pop elimina el ultimo elemento de la lista

datos.pop()   #sirve para eliminar elemeto de la lista

datos.pop()

print(datos)

#como puedo saber cuantos elementos tiene mi lista.....len()

#funcion len() lenght


cuenta_e = [1,2,3,4,5,6,7,8,9,10]

print(len( cuenta_e)) #cuenta la cantidad de elementos de la lista

#ej obtener la dimencion de la lista de cuenta_e e imprimir;

#la lista de datos tiene ----elementos 

print("la lista de datos tiene",len(cuenta_e),"elementos")


#eje.imprimir el ultimon elemento que no sabemos

#cuantos elementos,tiene,pista usar len()

#no hacer lista larga[]
 lista_g=[2,4,6,7,8,9,12,1,33,55]

print(len(lista_g)-1)

print(lista_g[len(lista_g)-1])

#bucles/ciclos/iteraciones

list_tema=["vari<ble","listas","tipos de datos"]

list_tema[0]="variable"

print(list_tema)


    

#recorrer una lista con for e imprimir en cada ciclo 
#el valor del elemento con 3 signos de admiracion al final
#fuera del bucle "fin"!!!
#ej variab

     







for w in range(1,101):
    print(w)
    #ej 2 imprimir el resultado de la suma de los numeros 
#del 1 al 10usando range¨1+2+3+4+7+8+9+10:55
lista_i=[1,2,3,4,5,6,7,8,9,10]
suma=0
for s in lista_i:
    suma=suma+s
print(suma)