import tkinter as tk
from tkinter import messagebox
from libreria import *

# Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.config(width=400, height=300, background='#008181')
ventana_principal.title("Ventana principal")

texto_capital = tk.Label(ventana_principal, text="")

pais=tk.StringVar()

def Buscar_ciudades():
    pais_buscado = pais.get()
    ciudades = Consulta_ciudades(pais_buscado)
    pais.set("")
    if ciudades != "":
        ### Label que presenta las ciudades de los paises
        global texto_capital
        texto_capital.place_forget()
        texto_capital = tk.Label(ventana_principal, text=ciudades, justify="center")
        texto_capital.place(x= 130,y=150)
    else:
        messagebox.showinfo("Observation", "country not found") 


Nombre_app = tk.Label(ventana_principal, text=" Buscar ciudades del pais seleccionado (ingles)", background='#008181',
                     foreground="white")
Nombre_app.place(x= 80,y=10)

texto_entrada = tk.Label(ventana_principal, text=" Enter the country name: ",background='#008181', foreground="white")
texto_entrada.place(x= 100,y=40)

pais_solicitud = tk.Entry(ventana_principal, textvariable=pais)
pais_solicitud.place(x= 110,y= 70)

# botón dentro de la ventana principal que activa la funcion de buscar
boton_buscar = tk.Button(ventana_principal,text="Search", command=Buscar_ciudades)
boton_buscar.place(x=150, y=100)

ventana_principal.mainloop()