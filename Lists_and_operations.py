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


#3
# This program asks the user for a certain number of integers,
# stores them in a list, and then prints the list in reversed order.

def kaannetty_lista():
    luvut = []
    maara = int(input("Kuinka monta kokonaislukua syötät? "))
    for i in range(maara):
        luku = int(input("Anna kokonaisluku: "))
        luvut.append(luku)
    luvut.reverse()
    print()
    print(' '.join(map(str, luvut)))

kaannetty_lista()


#4
# This program asks the user for five integers,
# stores them in a list, sorts the list in descending order,
# and then prints the numbers on one line.

def laskeva_lista():
    luvut = []
    for i in range(5):
        luku = int(input("Anna kokonaisluku: "))
        luvut.append(luku)
    luvut.sort(reverse=True)
    print()
    print(' '.join(map(str, luvut)))

laskeva_lista()



#5
# This program asks the user for five integers,
# stores them in a list, and prints the count, minimum, maximum, and sum of the list.

def tulosta_tiedot(luvut):
    print()
    print(f"count: {len(luvut)}")
    print(f"min:   {min(luvut)}")
    print(f"max:   {max(luvut)}")
    print(f"sum:   {sum(luvut)}")

def main():
    luvut = []
    for i in range(5):
        luku = int(input("Anna kokonaisluku: "))
        luvut.append(luku)
    tulosta_tiedot(luvut)

main()



#6
# This program asks the user for a letter,
# and then tells how many times that letter appears in a predefined list.

def kirjainlista():
    lista = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
    kirjain = input("Anna kirjain: ").upper()
    maara = lista.count(kirjain)
    print(f"Kirjain {kirjain} löytyi listasta {lista} {maara} kertaa.")

kirjainlista()


#7
# This program asks the user for surnames until they type "ok",
# then prints all unique surnames in alphabetical order.

def listaa_sukunimet():
    sukunimet = []
    while True:
        nimi = input("Anna sukunimi (ok lopettaa): ")
        if nimi.lower() == "ok":
            break
        if nimi not in sukunimet:
            sukunimet.append(nimi)
    sukunimet.sort()
    print()
    print(', '.join(sukunimet))

listaa_sukunimet()


#8
# This program asks the user for five integers,
# then calculates and prints the sum of the positive numbers.

def positive_sum(lista):
    return sum(luku for luku in lista if luku > 0)

def main():
    luvut = []
    for i in range(5):
        luku = int(input("Anna kokonaisluku: "))
        luvut.append(luku)
    tulos = positive_sum(luvut)
    print()
    print(tulos)

main()
