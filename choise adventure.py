### Choise adventure


#raid

pages = [
    "Page 0) elije tu propia aventura\choose your own adventure\nQue quieres hacer?\What do you want to do? \n1)Vas a comprar al chino\you go to the chinese to buy \n2)Te quedas en casa\Stay home\n3)Tomas yogurt vencido de la heladera\You eat expired yogurt from the refrigerator...",
    "Page 1) \nB\n1)\n2)\n3)...",
    "Page 2)\nC\n1)\n2)\n3)...",
    "Page 3)\nD\n1)\n2)\n3)...",
]

#a function was created called showpage and it takes the raid and the position of the raid as parameters.

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))


showPage(0)
