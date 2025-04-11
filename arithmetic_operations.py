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
