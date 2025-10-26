# čas stráveny pri robení kódu: cca 3-4 hodiny 

import requests

api = "d78bb880bdfc9f39db3e5ed24f322ee9"
country_code = str(input("vyberte si krajinu(skratku, napr.: 'sk'): "))
mesto = str(input("vyberte si mesto(cely názov): "))
jazyk = str(input("vyberte si jazyk(skratku, napr.: 'sk'): "))
url = f"https://api.openweathermap.org/data/2.5/weather?q={mesto},{country_code}&appid={api}&lang={jazyk}&units=metric"
request = requests.get(url)
info = request.json()

if request.status_code == 200:
    print("predpoved počasia:")
    
    teplota = info['main']['temp'], "°C"
    pocitovo = info['main']['feels_like'], "°C"
    min_teplota = info['main']['temp_min'], "°C"
    max_teplota = info['main']['temp_max'], "°C"
    vlhkost = info['main']['humidity'], "%"
    tlak = info['main']['pressure'], "hPa"
    pocasie = info['weather'][0]['description']
    vietor = info['wind']['speed'], "m/s"
    oblacnost = info['clouds']['all'], "%"
    viditelnost = info['visibility'], "m"
print(f"--------------------------------------------\n"
      "Vyber si čo chceš vedieť o počasí: ")

c = input("teplota (Y/N): ")
d = input("pocitova teplota (Y/N):")
e = input("minimalna teplota (Y/N):")
f = input("maximalna teplota (Y/N):")
g = input("počasie (oblačnosť) (Y/N):")
h = input("rychlost vetra (Y/N):")
i = input("vlhkost (Y/N):")
ii = input("oblačnosť (Y/N):")
j = input("atmosfericky tlak (Y/N):")
jj = input("viditelnost (Y/N):")

print(f"____________________________________________\n"
      f"AKTUALNE POCASIE V MESTE {mesto}:")

if c == "y" or c == "Y":    
    print(f"------------------------------------\n"
          f"teplota: {teplota}")
if d == "y" or d == "Y":
    print(f"------------------------------------\n"
          f"pocitová teplota: {pocitovo}")
if e == "y" or e == "Y":
    print(f"------------------------------------\n"
          f"min teplota: {min_teplota}")
if f == "y" or f == "Y":
    print(f"------------------------------------\n"
          f"max teplota: {max_teplota}")
if g == "y" or g == "Y":
    print(f"------------------------------------\n"
          f"počasie: {pocasie}")
if h == "y" or h == "Y":
    print(f"------------------------------------\n"
          f"vietor: {vietor}")
if i == "y" or i == "Y":
    print(f"------------------------------------\n"
          f"vlhkosť: {vlhkost}")
if ii == "y" or ii == "Y":
    print(f"------------------------------------\n"
          f"oblačnosť: {oblacnost}")
if j == "y" or j == "Y":
    print(f"------------------------------------\n"
          f"atmosferický tlak: {tlak}")
if jj == "y" or jj == "Y":
    print(f"------------------------------------\n"
          f"viditelnost: {viditelnost}\n"
          f"___________________________________________\n")