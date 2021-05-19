import pandas
import folium
from geopy import Nominatim
import tkinter as tk
from tkinter import *
import webbrowser
from folium.features import DivIcon

df = pandas.read_csv('Autorizatii1.csv')
loc = Nominatim(user_agent="myGeocoder")

m = folium.Map(location=[45.7583255, 21.2346139],type='OpenStreetMap', zoom_start=13)

name = " Autorizații de construire în Municipiul Timișoara "
title = '<h2 align="center" style="background-color:Violet" style="font-size:20px"><b>{}</h2>'.format(name)
m.get_root().html.add_child(folium.Element(title))

folium.map.Marker([45.742135, 21.113419], icon=DivIcon(icon_size=(500, 500), icon_anchor=(0, 0),
                                          html='<div style="font-size: 13pt"><b>Contact:</b><br>Adresa: b-dul C.D. Loga, nr. 1<br>Telefon: (0256) 408.300<br>'
                                          'Fax: (0256) 490.635<br>Email: primariatm@primariatm.ro</div>')).add_to(m)

for i in range(1, len(df["Adresa"])):
 location = loc.geocode(df["Adresa"][i] + " " + "Timisoara")

 try:
  location = loc.geocode(df["Adresa"][i] + " " + "Timisoara")
  html = '<b>Beneficiar: ' + "</b> " + df["Beneficiar"][i] + "<br>" + '<b>Descriere: ' + "</b>" + df["Descriere"][i]
  iframe = folium.IFrame(html)
  popup = folium.Popup(iframe, min_width=300, max_width=300)
  marker = folium.Marker(location=[location.latitude, location.longitude], popup= popup, icon=folium.Icon(color='purple')).add_to(m)
 except AttributeError:
  print(df["Adresa"][i])

m.save('index.html')

url = 'index.html'
window = tk.Tk()
window.title("Interfata grafica")
window.geometry("250x100")
window.configure(bg='pink')
frame = Frame(window)
frame.pack()

def OpenUrl(url):
   webbrowser.open_new(url)
button = tk.Button(window, text="Deschide harta cu autorizatii", command=lambda aurl=url:OpenUrl(aurl), bg="pink")
button2 = tk.Button(window, text="Inchide fereastra", bg="pink", command=window.destroy)
button.pack(pady=10)
button2.pack(pady=10)
window.mainloop()