# čas stráveny pri robení kódu: cca 5 hodin
from tkinter import *
from tkinter import Tk
import tkinter as tk
import requests

root = Tk()

countrycc = tk.StringVar()
mesto3 = tk.StringVar()
jazykc = tk.StringVar()
countryc = tk.Label(root, text="Zadaj krajinu (napr: 'sk'): ")
countryc.pack()
countryc1 = tk.Entry(root, textvariable=countrycc)
countryc1.pack()
mestoz = tk.Label(root, text="Zadaj mesto: ")
mestoz.pack()
mestoz1 = tk.Entry(root, textvariable=mesto3)
mestoz1.pack()
jazyk1 = tk.Label(root, text="Zadaj jazyk (napr: 'sk'): ")
jazyk1.pack()
jazyk2 = tk.Entry(root, textvariable=jazykc)
jazyk2.pack()
Label(root, text="Zavri toto okno aby si sa dostal ďalej").pack()
root.mainloop()

api = "d78bb880bdfc9f39db3e5ed24f322ee9"
country_code = countrycc.get()
mesto = mesto3.get()
jazyk = jazykc.get()
url = f"https://api.openweathermap.org/data/2.5/weather?q={mesto},{country_code}&appid={api}&lang={jazyk}&units=metric"
request = requests.get(url)
info = request.json()

if request.status_code == 200:
    
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

koren = Tk()
Label(koren, text="Vyber si čo chceš vedieť o počasí:").pack()
c = IntVar()
check1 = tk.Checkbutton(koren, text='teplota', variable=c)
check1.pack()
d = IntVar()
check2 = tk.Checkbutton(koren, text='pocitova teplota', variable=d)
check2.pack()
e = IntVar()
check3 = tk.Checkbutton(koren, text='minimalna teplota', variable=e)
check3.pack()
f = IntVar()
check4 = tk.Checkbutton(koren, text='maximalna teplota', variable=f)
check4.pack()
g = IntVar()
check5 = tk.Checkbutton(koren, text='počasie (prši/neprši/sneži/nesneži)', variable=g)
check5.pack()
h = IntVar()
check6 = tk.Checkbutton(koren, text='rychlost vetra', variable=h)
check6.pack()
i = IntVar()
check7 = tk.Checkbutton(koren, text='vlhkost', variable=i)
check7.pack()
ii = IntVar()
check8 = tk.Checkbutton(koren, text='oblačnost', variable=ii)
check8.pack()
j = IntVar()
check9 = tk.Checkbutton(koren, text='atmosfericky tlak', variable=j)
check9.pack()
jj = IntVar()
check10 = tk.Checkbutton(koren, text='viditelnost', variable=jj)
check10.pack()
Label(koren, text="Zavri toto okno aby si sa dostal ďalej").pack()
koren.mainloop()

root1 = Tk()
if c.get():
    tk.Label(root1, text=f"teplota: {teplota}").pack()
if d.get():
    tk.Label(root1, text=f"pocitová teplota: {pocitovo}").pack()
if e.get():
    tk.Label(root1, text=f"min teplota: {min_teplota} ").pack()
if f.get():
    tk.Label(root1, text=f"max teplota: {max_teplota} ").pack()
if g.get():
    tk.Label(root1, text=f"počasie: {pocasie} ").pack()
if h.get():
    tk.Label(root1, text=f"vietor: {vietor} ").pack()
if i.get():
    tk.Label(root1, text=f"vlhkosť: {vlhkost} ").pack()
if ii.get():
    tk.Label(root1, text=f"oblačnosť: {oblacnost} ").pack()
if j.get():
    tk.Label(root1, text=f"atmosferický tlak: {tlak} ").pack()
if jj.get():
    tk.Label(root1, text=f"viditelnost: {viditelnost} ").pack()
root1.mainloop()

