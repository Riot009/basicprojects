import random

def jugar():
    

    user = input(" Selecciona piedra, papel, o tijera:\n ").lower()
    
    computer = random.choice(["piedra", "papel", "tijera"])

    if user == computer:
        return "Empate "f"seleccionaron lo mismo!"
    if win_user(user, computer):
        return "Ganaste!"f" La computadora eligio {computer}"
    
    return "Perdiste! "f"La computadora eligio {computer}"


def win_user(player, opponent):
    
    
    if ((player == "piedra" and opponent == "tijera")
        or(player == "tijera" and opponent == "papel")
        or (player == "papel" and opponent == "piedra")):
        return True
    else:
        return False
    


print(jugar())