#1 Gender Distribution
# This program asks the user for the number of female and male students,
# calculates the percentage of each gender, and prints the results.

def gender_distribution():
    females = int(input("Enter the number of female students:"))
    males = int(input("Enter the number of male students:"))
    
    total = males + females
    
    females_percentage = (females / total) * 100 if total > 0 else 0.0
    males_percentage = (males / total) * 100 if total > 0 else 0.0
    
    print(f"\nFemales: {females_percentage:.1f}%")
    print(f"Males: {males_percentage:.1f}%")
    
gender_distribution()


#2 - Sales Commission Calculation
# This exercise practices the use of arithmetic operations, conditional statements (if-else),
# and error handling (try-except). The program calculates a car salesperson's commission 

def myyntipalkkio():
    try:
        myyntihinta = float(input("Anna auton myyntihinta: "))

        if myyntihinta < 50000:
            bonus = myyntihinta * 0.01
        else:
            bonus = myyntihinta * 0.015

        bonus = max(bonus, 200)

        print(f"Myyntipalkkio on {bonus:.2f}€.")

    except ValueError:
        print("Virheellinen syöte: Anna myyntihinta numerona!")

myyntipalkkio()


#3
# This exercise practices integer division and modulus operations.
# The user is asked how many apples and children there are.
# The program calculates how many apples each child gets and how many are left over.

def omenat():
	try:
		omenat = int(input("Omenoiden lukumäärä? "))
		lapset = int(input("Lasten lukumäärä? "))
		
		if lapset <= 0:
			print("Lasten määrän on oltava suurempi kuin nolla.")
			return
		
		perlapsi = omenat // lapset
		yliomenat = omenat % lapset
		
		print(f"Omenoita per lapsi: {perlapsi}")
		print(f"Ylijääviä omenoita : {yliomenat}")
		
	except ValueError:
		print("Virheellinen syöte: Anna kokonaisluvut.")
		
omenat()


#4
# This task practices conditional logic and basic arithmetic operations.
# The user enters how many times they go to the gym per year, the price of a day ticket, and the annual pass.
# The program calculates which option is cheaper and by how much.

def kuntosali():
	try:
		paivat = int(input("Anna käyntikertojen vuosimäärä: "))
		paivalippu = float(input("Anna päivälipun hinta: "))
		vuosilippu = float(input("Anna vuosilipun hinta: "))
		
		hinta = paivat * paivalippu
		
		if hinta < vuosilippu:
			ero = vuosilippu - hinta
			print(f"Päivälippu tulee {ero:.2f} euroa halvemmaksi")
		elif vuosilippu < hinta:
			ero = hinta - vuosilippu
			print(f"Vuosilippu tulee {ero:.2f} euroa halvemmaksi")
		else:
			print("Vuosilippu ja päiväliput tulevat samanhintaisiksi")
		
	except ValueError:
		print("Virheellinen syöte! Syötä numerot uudelleen")
		
kuntosali()



#5
# This task practices input validation and error handling using try-except.
# The user is asked to input an integer. If the input is not a valid integer, 
# the program prints an error message and shows the invalid input in quotes.

def tarkasta_kokonaisluku():
	syote = input("Anna kokonaisluku: ")
	try:
		numero = int(syote)
		print("OK")
	except ValueError:
		print(f"'{syote}' ei ole kokonaisluku")

tarkasta_kokonaisluku()


#6
# This task practices numeric input validation and conditional logic.
# The user is asked for a weekday number (1–7). If the input is valid, the program prints "OK".
# Otherwise, it instructs the user to input a number within the correct range.

def viikonpaiva_nro():
	try:
		numero = int(input("Anna viikonpäivän numero: "))
		if 1 <= numero <= 7:
			print("OK")
		else:
			print("Syötä kokonaisluku väliltä 1 ja 7")
	except ValueError:
		print("Syötä kokonaisluku väliltä 1 ja 7")

viikonpaiva_nro()

