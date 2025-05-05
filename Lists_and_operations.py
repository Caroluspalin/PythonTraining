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

#9 Prints all words that are exactly 15 characters long from the MIT word list on a single line, separated by commas
from urllib.request import urlopen

sanalista = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read().splitlines()
pitkat_sanat = [sana.decode("utf-8") for sana in sanalista if len(sana.decode("utf-8")) == 15]
print(", ".join(pitkat_sanat))


#10
# Returns the second largest unique number from a list

def toiseksi_suurin(lista):
    lista = list(set(lista))
    lista.sort()
    return lista[-2]

def main():
    print(toiseksi_suurin([1, 5, 4, 5, 4, 3]))

main()

#11
# Print unique and sorted numbers, then the original list sorted

def yksilolliset_lista():
    luvut = []
    for i in range(5):
        luku = int(input("Anna kokonaisluku: "))
        luvut.append(luku)

    singles = sorted(list(dict.fromkeys(luvut)))
    kaikki = sorted(luvut)

    print(', '.join(map(str, singles)))
    print(', '.join(map(str, kaikki)))

yksilolliset_lista()



#12 Check if a given row in a Sudoku grid contains only unique non-zero values

def rivi_oikein(sudoku: list, rivi_nro: int) -> bool:
    rivi = sudoku[rivi_nro]
    luvut = [x for x in rivi if x != 0]
    return len(luvut) == len(set(luvut))

sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(rivi_oikein(sudoku, 0))
print(rivi_oikein(sudoku, 1))



#13 Multiply each element in a list by 3, modifying the list in place

def kerro_kolmella(lista):
    for i in range(len(lista)):
        lista[i] *= 3

lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [10, 20, 30]

print(lista_1)
kerro_kolmella(lista_1)
print(lista_1)

print(lista_2)
kerro_kolmella(lista_2)
print(lista_2)


#14 Create a new list with elements multiplied by 3, original list remains unchanged

def kerro_kolmella(lista):
    uusi_lista = []
    for arvo in lista:
        uusi_lista.append(arvo * 3)
    return uusi_lista

# Main program:
lista = [1, 2, 3, 4, 5, 6]
uusi_lista = kerro_kolmella(lista)
print(lista)
print(uusi_lista)
