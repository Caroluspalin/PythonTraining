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

