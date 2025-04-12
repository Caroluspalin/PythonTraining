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