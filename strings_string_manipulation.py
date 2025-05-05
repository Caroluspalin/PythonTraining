
#1 program prints the given text first with lowercase, then uppercase and then tells how many letters it had
def merkkijonot_1():
    teksti = input("Anna teksti: ")
    print()  
    print(teksti.lower())
    print(teksti.upper())
    print(f'Merkkijonossa "{teksti}" on {len(teksti)} merkkiä')


merkkijonot_1()