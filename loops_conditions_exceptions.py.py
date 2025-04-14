# 1  For loop demonstration
# This function prints numbers from 0 to 9 using a for loop

def for_silmukka():
    for i in range(10):
        print(i, end=' ')
        
for_silmukka()


# 2  For loop from 10 to 30
# This function prints numbers from 10 to 30 using a for loop

def tulosta_numerot():
    for i in range(10, 31):
        print(i, end=' ')

tulosta_numerot()


# 3  Countdown with sum
# Asks the user for a number and prints numbers from n to 1, then prints the sum

def tulosta_laskevasti():
    n = int(input("Anna kokonaisluku: "))

    if n <= 0:
        print("Ei tulostettavaa!")
    else:
        summa = 0
        for i in range(n, 0, -1):
            print(i, end=" ")
            summa += i
        print()  
        print("Lukujen summa on", summa)

tulosta_laskevasti()
