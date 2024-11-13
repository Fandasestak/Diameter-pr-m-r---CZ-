input = input("čísla k průměru: ") #1

seznam = [float(cislo) for cislo in input.split(",")] #2
vysledek = sum(seznam) / len(seznam) #3
print(f" - průměr je: {vysledek}") #4

#1 - vytvoříme si input(textový řetězec)
#2 - vytvorime si název složky(seznam), [] = jedná se o list, input(spojime všechny čísla v inputu rozdělí pomocí .split ...)
#2 ... a zadáme proto nazev cislo, cislo pomocí "float"(převedeme na desetinné číslo) 
#3 - nyní vytvoříme složku(vysledek) a zadáme normálně průměr(sečtená čísla[sum] / počet čísel[len])
#4 - nakonec vyvoláme funkci "print", a složku výsledek. (to moje je pro lepší přehlednost)
#4 ... můžete to zadat i npř. "print(vysledek)"
