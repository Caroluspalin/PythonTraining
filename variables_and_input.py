# 1. Print "Hello World!"
print("Hello World!") 



# 2. Calculate the number of bottles needed for a party
import math 

vieraat = int(input("Anna juhliin tulevien aikuisten määrä: "))  

lasia_per_pullo = 7  

tarvittavat_pullot = math.ceil(vieraat / lasia_per_pullo)  

print(f"Pulloja tarvitaan {tarvittavat_pullot} kappaletta")  




# 3. Greeting input and output
tervehdys = input("Anna tervehdys: ")  
etunimi = input("Anna etunimi: ") 
sukunimi = input("Anna sukunimi: ")  
print(f"{tervehdys} {etunimi} {sukunimi}!")  



# 4. Format a floating-point number
luku = float(input("Anna desimaaliluku: "))  

print(f"{luku:.2f}")  
print(f"{luku:.4f}")  




# 5. Calculate price with VAT
def price_plus_vat():
    ALV_PROSENTTI = 25.5  
    
    try:
        hinta = float(input("Anna hinta:"))  
        kokonaishinta = hinta * (1 + ALV_PROSENTTI / 100)  
        print(f"Arvonlisäverollinen hinta on {kokonaishinta:.2f}") 
    except ValueError:
        print("Virheellinen hinta!")  
        
price_plus_vat()




# 6. Special characters in strings
# This function demonstrates how to include special characters in Python strings.
def erikoismerkit():
    print('Python is named after the "Monty Python\'s Flying Circus",')
    print("a BBC comedy series from 1970s.")
    
erikoismerkit()  
