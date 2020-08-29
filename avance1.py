"""Problemática: Gran acumulación de plástico en las áreas verdes de “El Refugio”, Querétaro, producida por sus residentes, ya que tienen una gran cantidad de consumo y compra de artículos de plásticos sin moderación.  

Objetivo general: Regular el suministro a los consumidores de artículos de plásticos en los comercios a los alrededores y dentro de “El Refugio, Querétaro”. 

Objetivos específicos y plan de acción: 
Restringir la cantidad de compras de productos que estén contenidos en: PET, PEAD (que se utiliza para contener productos de limpieza), y LDPE o PEBD (que se utiliza en la fabricación de bolsas y botellas)a los habitantes de "El Refugio, Querétaro".

Se investigará la cantidad de productos básicos que están contenidos en plásticos necesarios para el consumo en general de los habitantes de El Refugio. Es decir, se establecerá una media de consumo de plástico semanalmente por familia para poder regular la cantidad máxima a vender.  

Se establecerán listas en las que se dividirán los artículos dependiendo del tipo de plástico que lleven.

Por cada compra que realice el usuario, se determinará que tipo de plástico (de los mencionados anteriormente) es, y se llevará un contador que, indicará la cantidad de plástico (dependiendo del tipo de plástico) le queda disponible para comprar, y, al alcanzar el número de consumo de plástico máximo, bloqueará el producto. Al bloquearlo, se le indicará al usuario la razón del bloqueo del producto, y se le asignará una nueva fecha en la que podrá volver a adquirirlo. El producto se reactivará 7 días después.  
Se le indicará al usuario si su cantidad de consumo de plástico aumentó o disminuyó con respecto a la semana pasada.

Algoritmo para contar consumo de plástico por usuario y decirle cuánta cantidad puede comprar(solo en categorías PET, PEAD, y PEBD): 

división(conspet=0, conspebd=0, conspead=0)
compra=str(input("¿Qué está comprando?)) 
if compra==PET: 
ciclo(conspet<=7)
conspet=conspet+1
max=7-conspet
return("Te quedan", " ", max, " ", "artículos de PET por comprar.")
else:
if compra==PEAD:
ciclo(conspead<=7)
conspead=conspead+1
max=7-conspead
return("Te quedan", " ", max, " ", "artículos de PEAD por comprar.")
else:
if:
compra==PEBD:
ciclo(conspebd<=7)
conspebd=conspebd+1
max=7-conspebd
return("Te quedan", " ", max, " ", "artículos de PEBD por comprar.")"""
#el usuario ingresará el número de artículos de plástico PET que llevará
import Numpy
artpet=int(input("Ingrese cuántos artículos de PET llevará")) #En un futuro se harán listas para que el usuario eliga el artículo que desea sin espeficar qué plástico es
maxpet = 6
if (artpet<=maxpet):
    restpet=maxpet-artpet #se restarán los artículos comprados para saber cuántos quedan
    porc= (artpet/maxpet)*100 #se utilizará un contador y un if para determinar cuando el usuario alcance el máximo,  si puede comprar más artículos de PET esa semana o no.
    print("Te quedan", restpet, "artículos de PET disponibles esta semana. Has consumido un", porc,"% de los artículos de PET totales de la semana")
else: print("Excediste el máximo de artículos PET permitidos, disminuye la cantidad.")
#el usuario ingresará el número de artículos de plástico PEBD que llevará
artpebd=int(input("Ingrese cuántos artículos de PEBD llevará")) #En un futuro se harán listas para que el usuario eliga el artículo que desea sin espeficar qué plástico es
maxpebd = 5
if(artpebd<=maxpebd):
    restpebd=maxpebd-artpebd #se restarán los artículos comprados para saber cuántos quedan
    porc2= (artpebd/maxpebd)*100 #se utilizará un contador y un if para determinar cuando el usuario alcance el máximo,  si lo alcanza se le dará un mensaje 
    print("Te quedan", restpebd, "artículos de PEBD disponibles esta semana. Has consumido un", porc2,"% de los artículos de PEBD totales de la semana")
else: print("Excediste el máximo de artículos PEBD permitidos, disminuye la cantidad.") #actualmente sumaría el dato igual si excede el máximo, pero en un futuro se volverá a preguntar un valor y se agregará por un ciclo hasta que ingrese el número correcto
#el usuario ingresará el número de artículos de plástico PEAD que llevará
artpead=int(input("Ingrese cuántos artículos de PEAD llevará")) #En un futuro se harán listas para que el usuario eliga el artículo que desea sin espeficar qué plástico es
maxpead = 5
if(artpead<=maxpead):
    restpead=maxpead-artpead #se restarán los artículos comprados para saber cuántos quedan
    porc3= (artpebd/maxpebd)*100 #se utilizará un contador y un if para determinar cuando el usuario alcance el máximo,  si puede comprar más artículos de PEAD esa semana o no.
    print("Te quedan", restpead, "artículos de PEAD disponibles esta semana. Has consumido un", porc3,"% de los artículos de PEAD totales de la semana")
else: print("Excediste el máximo de artículos PEBD permitidos, disminuye la cantidad.")
constotal= artpet + artpead + artpebd
consmaxtot=maxpet + maxpead + maxpebd
porcentotal=(constotal/consmaxtot)*100
print("Tu consumo de plástico total del día es de:", porcentotal, "% de artículos totales de la semana")
