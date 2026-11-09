imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print(imie[0] + nazwisko[0])

tekst = input("Podaj tekst: ")
print(tekst * 5)

tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")
tekst3 = tekst1 + tekst2
print(tekst3)

tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")
tekst3 = tekst1[:len(tekst1)//2] + tekst2[:len(tekst2)//2]
print(tekst3)