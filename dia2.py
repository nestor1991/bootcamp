lista_h =[1,2,3,4,5,6,7,8,9,10]
suma=0
for a in lista_h:
    suma=suma+a
print(suma)
#
lista_d=[2,4,6,8,10,12,14,16,18,20]
suma=0
for o in lista_d:
    suma=suma+o
print(suma)
lista_g=[150000,540000]
suma=0
for w in lista_g:
    suma=suma+w
print(suma)
#funcion

def suma(n1,n2):
    print(n1+n2)

suma(5,6)

def  suma(num1,num2):

    resultado=num1+num2

    return resultado

    #equivalente al de arriba 
def suma2(num1,num2):

        return num1+num2
f=suma2(10,5)
print(f)


#crear una funcion resta que reciba parametro o argumento los numeros 
#y retorne la resta de esos numeros
#luego llama a la funcion e imprimir el reultado 
##
def resta(num3,num4):

        return num3-num4
j=resta(150,100)

print(j)








# crear una funcion saludos que reciba como parametro nombre y edad 
#ej imprimir "hola soy------y tengo -----ahos"

def saludos(nombre,edad):
        print("hola soy",nombre,"y tengo",edad,"ahos)
saludos("nestor",27)
saludos("juana",33)
saludos("arturo",65)






#llamar varias veces a la funcion con  distintos valores
 




def datos (informe,archibos):
    print ("hola soy",informe,"y tengo",archibos,"ahos")
datos("ana",23)


def multiplicacion(nur2,nur3):
  
    return nur2*nur3

h=multiplicacion(5,10)
#crear una funcion suma_lista que reciba el como argumento una lista de numero
#y retorne la suma de sus elementos 
#pistas: usar un acumulador




def suma_lista(lista_l):

    suma=0

    for z in lista_l:

        suma=suma+z
    return suma


listita=[1,2,3,4,5]

resultado=(suma_lista(listita))

print(resultado)

listota=[100,5,5]

resultado2=(suma_lista(listota))

print(resultado2)
















#eliminar for
grupo5 =


# crear una funcion suma_cuadro que reciba una lista de numeros
#y retorne el valor de la suma de cada numero al cuadrado
#[1,2,3,4]...> 1+4+9+16--->30



lista=[1,2,3,4]

def suma_cuadrado(lista_o):
        
        suma=0
        for g in lista_o:
                suma=suma+(g*g)
        return suma

print(suma_cuadrado(lista))

        

    











