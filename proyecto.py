# biblioteca extra colorama
"""
Muestra el texto con diferentes /
fondos y colores
"""

from colorama import *

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
    
    resta = maximo-art_comprados
    
    if resta<0:
        return 0
    
    else:
        return resta

"""
el porcentaje de artículos
comprados con
respecto al total
de artículos
"""


def porcentaje(art_comprados, maximo):
    
    porcent= art_comprados/maximo*100
    
    if porcent>100:
        return 100
    
    else:
        return porcent


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


def validacion(art_comprados, maximo):
    
    if art_comprados>=maximo:
       
       return "Excedió el máximo de la semana. introduzca otra cantidad"
    
    else:
        
        return "es accesible, por favor continue con su compra"


def aclara_porcentaje(art_comprados, maximo):
    
    if porcent_restante(art_comprados, maximo)<0:
       
       return "Excedió el máximo de la semana, no se le permitirá comprar más"
    
    else:
        
        return "Aún tiene artículos disponibles, puede continuar con su compra"


"""
evaluar con datos
ingresados por el usuario
por medio de un menú
"""


while True:
    
    opcion=int(input("¿Desea realizar una compra? 0: Sí, 1:No"))
    
    if opcion==0:      
        
        """Se explican en qué categoría se dividen los plásticos"""  
        
        lista_pet=["Coca-cola","Sprite","Aceites", "Fanta"]   #lista
        
        print(Back.BLUE+ Fore.WHITE + "Algunos artículos de PET son: ", lista_pet)
        
        
        
        lista_pead=["Detergentes","Suavizantes","Shampoo", "Acondicionador"] #lista 
        print(Back.GREEN+ Fore.WHITE + "Algunos artículos de PEAD son: ", lista_pead)
        
        
        
        
        
        
        lista_pebd=["Bolsas para mascotas","Botellas","Bolsas para el aseo"] #lista
        print(Back.YELLOW+ Fore.WHITE + "Algunos artículos de PEBD son: ", lista_pebd)
        
        
        
        
        
        productos = [lista_pet,lista_pead,lista_pebd] #lista anidada 
        """Se crea un menú para que el usuario eliga qué desea hacer"""
        




        
        menu=int(input("Ingrese 1 si desea comprar artículos PET, 2 artículos PEAD, 3 Artículos PEBD: "))
        
        
        
        
        
        
        if menu==1:
            print ("Usted eligió comprar alguno de los siguientes artículos", productos [0])
            art_comp_pet= int(input("Ingrese el número de artículos de PET a comprar:"))
            
            
            print("ha comprado",porcentaje(art_comp_pet, MAX_PET ),"% de los artículos posibles de la semana")
            
            
            print("Le quedan",porcent_restante(art_comp_pet, MAX_PET),"% de artículos por comprar")
            
            
            print("Le quedan",resta_productos(art_comp_pet,MAX_PET),"artículos por comprar")
            
            
            print("La cantidad de productos de PET", validacion(art_comp_pet, MAX_PET))
            
            
            print(aclara_porcentaje (art_comp_pet, MAX_PET))
            
            
            
            
            
            
        elif menu==2:
            
            print ("Usted eligió comprar alguno de los siguientes artículos", productos [1])
            
            art_comp_pead= int(input("Ingrese el número de artículos de PEAD a comprar:"))
            
            print("ha comprado",porcentaje(art_comp_pead, MAX_PEAD ),"% de los artículos posibles de la semana")
                
            
            print("Le quedan",porcent_restante(art_comp_pead, MAX_PEAD),"% de artículos por comprar")
                
                
            print("Le quedan",resta_productos(art_comp_pead,MAX_PEAD),"artículos por comprar")
                
                
            print("La cantidad de productos de PEAD", validacion(art_comp_pead, MAX_PEAD))
                
                
            print(validacion(art_comp_pead, MAX_PEAD))
                
                
                
                
                
        elif menu==3:
                
                print ("Usted eligió comprar alguno de los siguientes artículos", productos [2])
                
                art_comp_pebd= int(input("Ingrese el número de artículos de PEBD a comprar:"))
                    
                    
                print("ha comprado",porcentaje(art_comp_pebd, MAX_PEBD ),"% de los artículos posibles de la semana")
                    
                    
                print("Le quedan",porcent_restante(art_comp_pebd, MAX_PEBD),"% de artículos por comprar")
                    
                    
                print("Le quedan",resta_productos(art_comp_pebd,MAX_PEBD),"artículos por comprar")
                    
                    
                print("La cantidad de productos de PEBD", validacion(art_comp_pebd, MAX_PEBD))
                    
                    
                print(validacion(art_comp_pebd, MAX_PEBD))
                
                
                
    
    elif opcion==1:
        
        print ("Gracias por venir")
        
        break
    
    else:
        
        print (Back.RED+ Fore.WHITE + "Ingrese una opción válida")