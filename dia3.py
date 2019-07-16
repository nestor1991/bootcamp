#utilidad for dentro de  una funcion 

ing_pan =["harina","levadura""sal2","azucar","agua"]

def imprimir_lista(ingrediente):


    for productos in ingrediente:

        print(productos)

imprimir_lista(ing_pan)





#######################condicionales###########################
# ==igual o compararf
# >mayor que 
# <menor que 
# >= mayor igual que numeral
# <=menor o igual que 
# != distinto o igual

a=4
# pregunta uno 
if a > 3:
    print("si,a es mayor a 3")
    
else :
    print("no,no es mayor a 3")

#pregunts 2 
if a==3 :
     print("a es igual a 3")
nota = 60 
#pregunta 3

if nota >=60:
    print(" pasaste")
else:
     print("hule ya")

# ejr crear una funcion que reciba como parametro una 
# nota del 1 al 100 e imprimir si pasaste o no (se prueva con 61)



def examen (numeros):
    if numeros >=60:
        print("pasaste")
    else:
        print("no pasaste")
examen(65)
examen(55)

# 3el  uso de and para unir dos condiciones
a=11
if a>5 and a<10:
    print("a es mayor a 5 y menor que 10")

else:
    print("a no esta en el rango,alguna de las dos condiciones no se cumplieron")

#el uso de or para validar una de las condiciones que se cumpla

#if a>5 or <10:





    #elife
edad = 7 
if edad > 18:
    print("deveria estar en la universidad")
elif edad  > 13:
    print("deveria estar en la secundaria")
elif edad>6:
    print("devaria estar en la primaria")
else:
    print("deveria estar en la casa")


#ejercicios 
#crear una funcion puntaje que reciba como parametro una nota 
# del 1 al 100 e imprimir que nota sacaste
# nota < 60 ---->1 
#nota entre 60 y 70---->2
#nota entre 71 y75----> 3
# nota entre 76 y 85---->4
#nota mayor a 85 en adelante---->5


def puntos(nota_t):
    if nota_t< 60:
        print(1)
    elif nota_t >= 60 and nota_t<= 70:
        print(2)
    elif nota_t >=71 and nota_t <=75:
        print(3)
    elif nota_t >=76 and nota_t <=85:
        print(4)
    elif nota_t >85:
        print(5)
p
untos(86)


# ejercicios 
#pedir al usuario que ingrese tres numeros y multiplicarlos 
# entre si, imprimir el resultado

nombre =input("ingrese el primer numero:")
nombre2=input("ingrese el segundo numero: ")
nombre3=input("ingrese el tercer numero: ")

print(int(nombre)*int(nombre2)*int(nombre3))

# ejerc 2 pedir al usuario un numero del 1 al 100 y llamar ala 
# funcion que retornaba la nota que creamos hace un rato 
#utilizando el valor ingresado por el usuario

gs=int(input("ingrese un numero del 1 al 100:"))

puntos(gs)
# 

#bucles while==mientras ###
x=O 
while x !=5: #
    print("esto es un bucle while,se va a ejecutar mientras x sea distinto de 5")
    x = int(input("ingresar un numero:" )) #
    print("el valor de ahora es",x) 
print("termino!!")








 # usando while pedir al nusuario 5 ingredientes para hacer una pizza 
 #y agregar a una lista,al finalimprimir la lista 
  contador=0
  ing__lista = []
  while conta <5:
      print("hola")
      ingre= input("ingrese un ingrediente")
      ing_lista.appen(ingre)
      conta = conta + 1
print("los ingredientes de la pizza son",ing_lista) 
  


  #ejercios crear un numero como el de arriba y    
   #darle







