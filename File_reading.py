#1 A program that reads and prints the contents of a text file. If the file is not found, it shows an error message.

def lue_tiedosto():
    tiedoston_nimi = input("Anna tiedoston nimi: ")

    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())
    except FileNotFoundError:
        print(f"Tiedostoa {tiedoston_nimi} ei löytynyt")

lue_tiedosto()


#2 A program that reads city bike data from a CSV file, calculates statistics, and displays the results.

def lue_tiedot(tnimi: str) -> list:
    try:
        with open(tnimi, encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()[1:]  
            return [rivi.strip() for rivi in rivit if rivi.strip()]
    except FileNotFoundError:
        print(f"Tiedostoa ei löytynyt!")
        return []

def nayta_tiedot(lista: list) -> None:
    tapahtumia = len(lista)
    yhteis_m = 0
    yhteis_sec = 0

    for rivi in lista:
        osat = rivi.split(",")
        try:
            matka = int(osat[6]) 
            kesto = int(osat[7])  
            yhteis_m += matka
            yhteis_sec += kesto
        except (IndexError, ValueError):
            continue  

    yhteis_km = yhteis_m / 1000
    keski_km = yhteis_km / tapahtumia if tapahtumia > 0 else 0
    keski_min = yhteis_sec / 60 / tapahtumia if tapahtumia > 0 else 0

    print(f"Lainaustapahtumia oli {tapahtumia} kappaletta.")
    print(f"Pyörillä ajettiin yhteensä {int(yhteis_km)} km")
    print(f"Pyörillä ajettiin keskimäärin {keski_km:.1f} km")
    print(f"Ajoaika oli keskimäärin {int(keski_min)} minuuttia")

def main():
    tnimi = input("Anna tiedoston nimi: ")
    tiedot = lue_tiedot(tnimi)
    if len(tiedot) > 0:
        nayta_tiedot(tiedot)

main()



#3 A program that reads city bike data and finds the departure stations with the fewest rides.

def lue_tiedot(tnimi: str) -> list:
    try:
        with open(tnimi, encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()[1:]  
            return [rivi.strip() for rivi in rivit if rivi.strip()]
    except FileNotFoundError:
        print(f"Tiedostoa ei löytynyt!")
        return []

def nayta_hiljaisin_lahtoasema(lista: list) -> None:
    asemat = {}

    for rivi in lista:
        osat = rivi.split(",")
        if len(osat) >= 4:
            asema = osat[3]
            asemat[asema] = asemat.get(asema, 0) + 1

    if not asemat:
        print("Ei lähtöasematietoja saatavilla.")
        return

    min_maara = min(asemat.values())

    hiljaisimmat = [asema for asema, lkm in asemat.items() if lkm == min_maara]

    print("Vähiten lähtöjä oli asemilta:")
    for asema in sorted(hiljaisimmat):
        print(f"{asema} ({min_maara} kappaletta)")

def main():
    tnimi = input("Anna tiedoston nimi: ")
    tiedot = lue_tiedot(tnimi)
    if len(tiedot) > 0:
        nayta_hiljaisin_lahtoasema(tiedot)

main()
