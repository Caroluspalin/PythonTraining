# 1  For loop demonstration
# This function prints numbers from 0 to 9 using a for loop

def for_silmukka():
    for i in range(10):
        print(i, end=' ')
        
for_silmukka()


# 2  For loop from 10 to 30
# This function prints numbers from 10 to 30 using a for loop

def tulosta_numerot():
    for i in range(10, 31):
        print(i, end=' ')

tulosta_numerot()


# 3  Countdown with sum
# Asks the user for a number and prints numbers from n to 1, then prints the sum

def tulosta_laskevasti():
    n = int(input("Anna kokonaisluku: "))

    if n <= 0:
        print("Ei tulostettavaa!")
    else:
        summa = 0
        for i in range(n, 0, -1):
            print(i, end=" ")
            summa += i
        print()  
        print("Lukujen summa on", summa)

tulosta_laskevasti()



#4
# This program calculates the average of user-input numbers.
# The user enters numbers one at a time and ends the input with 0.
# If at least one number is entered, it prints the average.

def laske_keskiarvo():
    summa = 0
    määrä = 0

    luku = float(input("Anna ensimmäinen numero: "))
    while luku != 0:
        summa += luku
        määrä += 1
        luku = float(input("Anna seuraava numero: "))

    if määrä == 0:
        print("Ei mitään laskettavaa")
    else:
        keskiarvo = summa / määrä
        print(f"Keskiarvo on {keskiarvo:.2f}")


def main():
    laske_keskiarvo()
    return 0


if __name__ == "__main__":
    main()



#5
# This program asks the user for a month number (1–12) and checks its validity.
# It keeps prompting until a valid month number is given and handles invalid input gracefully.

def tarkasta_kuukausi():
    while True:
        syote = input("Anna kuukauden numero: ")
        try:
            kuukausi = int(syote)
            if 1 <= kuukausi <= 12:
                print("OK")
                break
            else:
                print(f"{kuukausi} ei ole kelvollinen kuukausinumero")
        except ValueError:
            print(f"'{syote}' ei ole kelvollinen kuukausinumero")

def main():
    tarkasta_kuukausi()
    return 0

if __name__ == "__main__":
    main()



#6
# This program calculates the yearly growth of a deposit with compound interest and capital gains tax.
# The user provides the interest rate, tax rate, initial deposit, and the number of years.
# The program then prints the balance at the end of each year.

def talletus_korot():
    korkoprosentti = float(input("Anna korkoprosentti:"))
    veroprosentti = float(input("Anna pääomatuloveroprosentti:"))
    paoma = float(input("Anna talletuksen suuruus:"))
    vuodet = int(input("Anna vuosien lukumäärä:"))

    for vuosi in range(1, vuodet + 1):
        korko = korkoprosentti / 100 * paoma
        vero = veroprosentti / 100 * korko
        paoma = paoma + korko - vero
        print(f"vuosi {vuosi}: {paoma:.2f}")


talletus_korot()



#7
# This program uses a while loop to print numbers from 2 to 20 on the same line, separated by spaces.

def while_loop():
    luku = 2
    while luku <= 20:
        print(luku, end=" ")
        luku += 1

while_loop()
 