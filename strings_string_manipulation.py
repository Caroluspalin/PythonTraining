
#1 program prints the given text first with lowercase, then uppercase and then tells how many letters it had
def merkkijonot_1():
    teksti = input("Anna teksti: ")
    print()  
    print(teksti.lower())
    print(teksti.upper())
    print(f'Merkkijonossa "{teksti}" on {len(teksti)} merkkiä')


merkkijonot_1()


#2 count how many times user inputs helmi break program when user writes quit
def helminauha():
    count = 0
    first_input = True

    while True:
        if first_input:
            text = input("Anna ensimmäinen teksti: ")
            first_input = False
        else:
            text = input("Anna seuraava teksti: ")

        if text == "quit":
            break
        if text.lower() == "helmi":
            count += 1

    if count > 0:
        print(f"{count} helmeä")
    print("Näkemiin!")

helminauha()

#3 asks for an input from user and counts all the numbers in it and sums them together
def teksti_summa():
    teksti = input("Anna teksti: ")
    summa = 0

    for merkki in teksti:
        if merkki.isdigit():
            summa += int(merkki)

    print(f"\nLukujen summa on {summa}")

teksti_summa()

#4  Asks for a number of surnames, capitalizes them properly, removes duplicates, sorts them alphabetically, and prints them on one line.

def sukunimet():
    count = int(input("Anna nimien lukumäärä: "))
    surnames = set()

    for _ in range(count):
        name = input("Anna sukunimi: ").capitalize()
        surnames.add(name)

    sorted_surnames = sorted(surnames)
    print("\n" + " ".join(sorted_surnames))

sukunimet()

#5 Checks if all characters of string 2 are in string 1
def osajoukko():
    str1 = input("Anna 1. teksti: ")
    str2 = input("Anna 2. teksti: ")

    if str2 == "":
        print("Ei tutkittavaa!")
    elif all(char in str1 for char in str2):
        print("Osajoukko")
    else:
        print("Ei ole osajoukko")

osajoukko()



# 6. Text box
# Ask the user for a string and print it inside a box of dashes and vertical lines

text = input("Anna teksti: ")
border = '-' * (len(text) + 4)
print(border)
print(f"| {text} |")
print(border)




#7 Print the last 3 characters and reverse the string

text = input("Anna teksti: ")
print(text[-3:])    
print(text[::-1]) 