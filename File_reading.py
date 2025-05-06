#1 A program that reads and prints the contents of a text file. If the file is not found, it shows an error message.

def lue_tiedosto():
    tiedoston_nimi = input("Anna tiedoston nimi: ")

    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print(f"Tiedostoa {tiedoston_nimi} ei löytynyt")

lue_tiedosto()
