"""
Program sprawdza, czy podane słowo jest palindromem.
"""
slowo = input("Wpisz słowo, aby sprawdzić czy jest palindromem:")      
def palindrom(slowo):
    if slowo == slowo[::-1]:
        print(f"{slowo} jest palindromem")
    else:
        print(f"{slowo} nie jest palindromem")
palindrom(slowo)