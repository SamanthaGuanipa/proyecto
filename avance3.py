"""
Problemática: Gran acumulación de plástico
en las áreas verdes de “El Refugio”,
Querétaro, producida por sus residentes,
ya que tienen una gran cantidad de consumo
y compra de artículos de plásticos sin moderación.  

Objetivo general: Regular el suministro
a los consumidores de artículos
de plásticos en los comercios a los
alrededores y dentro de “El Refugio,
Querétaro”. 

Objetivos específicos y plan de acción: 
Restringir la cantidad de compras
de productos que estén contenidos
en: PET, PEAD (que se utiliza para
contener productos de limpieza), y
LDPE o PEBD (que se utiliza en la
fabricación de bolsas y botellas)a
los habitantes de "El Refugio, Querétaro".


Se investigará la cantidad de productos
básicos que están
contenidos en plásticos necesarios para
el consumo en general de los
habitantes de El Refugio. Es decir, se
establecerá una media de consumo
de plástico semanalmente por familia
para poder regular la cantidad máxima a vender.


Se establecerán listas en las que se
dividirán los artículos dependiendo
del tipo de plástico que lleven.


Por cada compra que realice el usuario,
se determinará que tipo de plástico
(de los mencionados anteriormente) es,
y se llevará un contador que, indicará
la cantidad de plástico (dependiendo del
tipo de plástico) le queda disponible
para comprar, y, al alcanzar el número
de consumo de plástico máximo, bloqueará
el producto. Al bloquearlo, se le indicará
al usuario la razón del bloqueo del producto,
y se le asignará una nueva fecha en la que
podrá volver a adquirirlo.
El producto se reactivará 7 días después.  
Se le indicará al usuario si su cantidad de
consumo de plástico aumentó o
disminuyó con respecto a la semana pasada.


Algoritmo para contar consumo de plástico por
usuario y decirle cuánta cantidad
puede comprar(solo en categorías
PET, PEAD, y PEBD):

"""


"""
el máximo de artículos plásticos que se
puede comprar (dependiendo del tipo de
plástico son seis
"""
MAX_PET=6

MAX_PEBD=5

MAX_PEAD=4

"""
Se creó una función que
se usará en el futuro con
condicionales
para restar la cantidad máxima,
y la comprada
"""

def resta_productos(art_comprados, maximo):
    return maximo-art_comprados

"""
el porcentaje de artículos
comprados con
respecto al total
de artículos
"""

def porcentaje(art_comprados, maximo):
    return art_comprados/maximo*100

"""
se calcula el porcentaje
de productos por comprar
"""

def porcent_restante(art_comprados, maximo):
    return resta_productos(art_comprados, maximo)/maximo

"""
se valida que el
usuario no compre más de
lo permitido
"""

def validacion (art_comprados, maximo):
    if art_comprados>maximo:
        return "Excedió el máximo de la semana, por favor introduzca otra cantidad"
    else:
        return "es accesible, por favor continue con su compra"
    

def aclara_porcentaje (art_comprados, maximo):
    if porcent_restante(art_comprados, maximo)<0:
        return "Excedió el máximo de la semana, no se le permitirá comprar más"
    else:
        return "Aún tiene artículos disponibles, por favor continue con su compra"
    
"""
evaluar con datos
ingresados por el usuario
"""
art_comp_pet= int(input("Ingrese el número de artículos de PET a comprar:"))


art_comp_pead= int(input("Ingrese el número de artículos de PEAD a comprar:"))


art_comp_pebd= int(input("Ingrese el número de artículos de PEBD a comprar:"))


print("ha comprado",porcentaje(art_comp_pet, MAX_PET ),"% de los artículos posibles de la semana")


print("Le quedan",porcent_restante(art_comp_pet, MAX_PET),"% de artículos por comprar")


print("Le quedan",resta_productos(art_comp_pet,MAX_PET),"artículos por comprar")


print("ha comprado",porcentaje(art_comp_pead, MAX_PEAD ),"% de los artículos posibles de la semana")


print("Le quedan",porcent_restante(art_comp_pead, MAX_PEAD),"% de artículos por comprar")


print("Le quedan",resta_productos(art_comp_pead,MAX_PEAD),"artículos por comprar")


print("ha comprado",porcentaje(art_comp_pead, MAX_PEAD ),"% de los artículos posibles de la semana")


print("Le quedan",porcent_restante(art_comp_pead, MAX_PEAD),"% de artículos por comprar")


print("Le quedan",resta_productos(art_comp_pead,MAX_PEAD),"artículos por comprar")


print("ha comprado",porcentaje(art_comp_pebd, MAX_PEBD ),"% de los artículos posibles de la semana")


print("Le quedan",porcent_restante(art_comp_pebd, MAX_PEBD),"% de artículos por comprar")


print("Le quedan",resta_productos(art_comp_pebd,MAX_PEBD),"artículos por comprar")


print("La cantidad de productos de PET", validacion(art_comp_pet, MAX_PET))


print("La cantidad de productos de PEAD", validacion(art_comp_pead, MAX_PEAD))


print("La cantidad de productos de PEBD", validacion(art_comp_pebd, MAX_PEBD))


print(aclara_porcentaje (art_comp_pet, MAX_PET))


print(validacion(art_comp_pead, MAX_PEAD))


print(validacion(art_comp_pebd, MAX_PEBD))



    