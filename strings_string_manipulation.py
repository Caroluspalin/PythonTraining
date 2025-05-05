
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