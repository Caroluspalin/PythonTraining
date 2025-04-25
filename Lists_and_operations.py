#1 Print a list without using a loop - Demonstrates unpacking a list with *
def tulosta_lista():
    lista = [1, 5, 4, 6, 2, 7]
    print(*lista)

tulosta_lista()

#2 Collect words until 'x' is entered, then print each word on a new line starting with 'x'
def sanat_jarjestykseen():
    lista = []
    while True:
        sana = input("Anna sana (x lopettaa): ")
        if sana == "x":
            break
        lista.append(sana)
    lista.sort()
    for sana in lista:
        print("x" + sana)

sanat_jarjestykseen()