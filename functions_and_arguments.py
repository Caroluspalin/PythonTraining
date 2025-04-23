#1 Print powers of 2 from 2^0 to 2^19 using a function call

def print_powers():
    for i in range(20):
        print(f"{2**i}", end=" " if i < 19 else "\n")


def eka_funktio():
    print_powers()


eka_funktio()


def main():
    print_powers

#2 Print a rectangle of asterisks with user-defined height and width

def print_rectangle(korkeus, leveys):
    for _ in range(korkeus):
        print("*" * leveys)

def main():
    korkeus = int(input("Anna suorakulmion korkeus: "))
    leveys = int(input("Anna suorakulmion leveys: "))
    print_rectangle(korkeus, leveys)

if __name__ == "__main__":
    main()


    
#3 Calculate and print a discount amount based on user input

def compute_discount(hinta, alennusprosentti):
    alennus = hinta * (alennusprosentti / 100)
    return alennus

def main():
    hinta = float(input("Anna hinta: "))
    alennusprosentti = float(input("Anna alennusprosentti: "))
    alennus = compute_discount(hinta, alennusprosentti)
    print(f"Alennus on {alennus:.2f} euroa")

if __name__ == "__main__":
    main()


    
#4 Calculate earnings based on hourly wage and overtime

def compute_earning(Tuntipalkka, Työtunnit):
    try:
        if Työtunnit > 40:
            Ylityötunnit = Työtunnit - 40
            Tulot = (40 * Tuntipalkka) + (Ylityötunnit * Tuntipalkka * 1.5)
        else:
            Tulot = Tuntipalkka * Työtunnit
        return Tulot
    except:
        return 0  

def main():
    Tuntipalkka = float(input("Anna tuntipalkka: "))
    Työtunnit = int(input("Anna tehdyt tunnit: "))
    Tulot = compute_earning(Tuntipalkka, Työtunnit)
    print(f"Ansiosi ovat {Tulot:.2f} euroa")

if __name__ == "__main__":
    main()



#5 Add two float numbers and round the result using standard rounding (round half up)

from decimal import Decimal, ROUND_HALF_UP

def funktio_add(Luku1, Luku2):
    summa = Decimal(str(Luku1)) + Decimal(str(Luku2))
    kokonaisluku = summa.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(kokonaisluku) 

def main():
    Luku1 = float(input("Anna ensimmäinen luku: "))
    Luku2 = float(input("Anna toinen luku: "))
    kokonaisluku = funktio_add(Luku1, Luku2)
    print(kokonaisluku)

if __name__ == "__main__":
    main()


#6 This program prints a pyramid shape based on the user-input height.
def print_pyramid(korkeus):
    for i in range(korkeus):
        valit = " " * i
        tahtia = "*" * (2 * (korkeus - i) - 1)
        print(valit + tahtia)

def main():
    korkeus = int(input("Anna pyramidin korkeus: "))
    print_pyramid(korkeus)

if __name__ == "__main__":
    main()



# 7. Date calculator
# This program asks the user for a date in the format dd.mm.yyyy and a number of days to add.
# It then calculates and displays the new date after adding the given number of days

from datetime import datetime, timedelta

def laske_paivays(paivays_str, lisapaivat):
    try:
        paivamaara = datetime.strptime(paivays_str, "%d.%m.%Y")
    except ValueError:
        print("Virheellinen päivämäärämuoto. Käytä muotoa pp.kk.vvvv.")
        return None

    uusi_paivays = paivamaara + timedelta(days=lisapaivat)
    return uusi_paivays.strftime("%d.%m.%Y")

def main():
    paivays_input = input("Anna päiväys muodossa pp.kk.vvvv: ")
    try:
        lisapaivat = int(input("Anna lisättävien päivien määrä: "))
    except ValueError:
        print("Virhe: päivien määrän pitää olla numero.")
        return 1

    tulos = laske_paivays(paivays_input, lisapaivat)
    if tulos is None:
        return 1

    print(f"Uusi päiväys on {tulos}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
