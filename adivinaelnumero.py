
### ADIVINA EL NUMERO ###


import random


def adivina(x):
    print("""
    Bienvenido a este lindo juego de adivina el numero
    Tu meta es adivinar el numero que genera la computadora
    """)
    random_number = random.randint(1, x) # Numero aleatorio entre 1 y x
    prediction = 0
    
    
    while prediction != random_number:
        
        try:
            prediction = int(input(f"Adivina un numero entre 1 y {x}: "))
        except :
            print("Error: Ingresa un valor numérico válido.")
            continue
        
        if prediction < random_number:
            print("Casi! Este numero es chico ")
        elif prediction > random_number:
            print("Casi! Este numero es grande! ")
        
        
    print(f"ADIVINASTE EL NUMERO!!{random_number}!!! ")


adivina(10)