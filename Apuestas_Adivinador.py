import random 


print ("=================================")
print ("________JUEGO DE APUESTAS________")
print ("________ADIVINA EL NUMERO________")
print ("=================================")

     
     


dinero= 0

def depositar_dinero (nu):
    global dinero
    
    dinero += nu
    
    print ("============================")
    print ("Dinero Depositado Exitosamente")
    print ("============================ \n")
    
    
def rango (numero, apuesta, multiplicador):
    global dinero
    
    n= random.randint (1,3)
    if dinero >= 1:
        pass
        if n == numero: 
            print ("==============")
            print ("¡¡HAS GANADO")
            print ("============== \n")
            dinero += apuesta * multiplicador
        
        else:
            print ("==============")
            print ("Has perdido")
            print ("Tu numero: ",numero, "El numero", n)
            print ("============== \n")
            dinero -= apuesta * multiplicador
            
    else:
        print ("====================")
        print ("Dinero Insuficiente")
        print ("==================== \n")
        
def mostrar_dinero ():
    global dinero
    
    print ("============================")  
    print ("Su Dinero Actual Es: ", dinero)
    print ("============================")
     
def retirar_dinero (canti):
    global dinero
    
    if dinero >=1:
        
        dinero -= canti
        print ("============================")
        print ("Dinero Retirado Exitosamente")
        print ("============================ \n")
        
    else:
        print ("No tiene Dinero \n")
        
        
while True:
    print ("""           [1]Depositar dinero
    	   [2]Jugar
    	   [3]Mostrar Dinero
    	   [4]Retirar Dinero
    	   [5]Salir""")
    	           
    opcion= int (input ("Opcion: "))
    
    if opcion == 1:
        nu= int (input ("Ingrese el monto a depositar: ")) 
        depositar_dinero (nu)
        
    elif opcion == 2:
        apuesta= int (input ("Ingrese el monto de su Apuesta: "))
        print ("""Multiplicadores Disponibles:
            	[X1]= 1
            	[X3]= 3
            	[X7]= 7""")
        multiplicador= int (input ("Multiplicador: "))
        print ("*Nota: Escoja un Numero entre 1 y 3")

        numero= int (input ("Numero: "))
        rango(numero, apuesta, multiplicador)
        
    elif opcion == 3:
        mostrar_dinero ()
        
    elif opcion == 4:
        print ("Su dinero Actual es: ", dinero)
        canti= int (input ("Ingrese la cantidad a Retirar: "))
        retirar_dinero (canti)
        
    else:
        break
    	          
    
    
    
        
    


