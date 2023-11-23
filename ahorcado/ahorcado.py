### Ahorcado ###
import random

import string

from palabras import palabras


def palabras_validas(palabras):
    palabra = random.choice(palabras)
    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper

def ahorcado():

    palabra = palabras_validas(palabras)

    letras_por_adiviar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase, "ñ")
    lives = 7
    while len(letras_por_adiviar) > 0 and lives > 0:
        print(f"Te quedan!{lives} vidas y usaste estas letras: {" ".join(letras_adivinadas)}")