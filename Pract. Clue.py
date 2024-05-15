import tkinter as tk
from tkinter import messagebox
import random

class ClueGame:
    def __init__(self, master):
        self.master = master
        master.title("Juego Clue")
        
        self.personajes = {
            "Juan": {"lugar": "Casa", "armas": ["Candelabro", "Revólver", "Llave Inglesa"]},
            "Pedro": {"lugar": "Hotel", "armas": ["Cuchillo", "Cuerda", "Pistola"]},
            "Fernanda": {"lugar": "Cocina", "armas": ["Llave Inglesa", "Candelabro", "Cuchillo"]},
            "Alex": {"lugar": "Salón", "armas": ["Candelabro", "Revólver", "Pistola"]},
            "Monica": {"lugar": "Jardín", "armas": ["Cuerda", "Revólver", "Cuchillo"]}
        }
        
        self.lugares = ["Casa", "Hotel", "Cocina", "Salón", "Jardín"]
        
        # Seleccionar aleatoriamente el culpable, el lugar y el arma
        self.culpable = random.choice(list(self.personajes.keys()))
        self.lugar_crimen = random.choice(self.lugares)
        self.arma_crimen = random.choice(self.personajes[self.culpable]["armas"])
        
        # Widgets
        self.label = tk.Label(master, text="¡Bienvenido al juego Clue!", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.personaje_entry = tk.Entry(master, width=30)
        self.personaje_entry.pack(pady=5)
        self.personaje_entry.insert(0, "Ingresa un personaje...")
        
        self.locacion_entry = tk.Entry(master, width=30)
        self.locacion_entry.pack(pady=5)
        self.locacion_entry.insert(0, "Ingresa una locación...")
        
        self.arma_entry = tk.Entry(master, width=30)
        self.arma_entry.pack(pady=5)
        self.arma_entry.insert(0, "Ingresa un arma...")
        
        self.verificar_button = tk.Button(master, text="Verificar", font=("Arial", 14), command=self.verificar)
        self.verificar_button.pack(pady=10)
        
        self.pista_button = tk.Button(master, text="Dar una pista", font=("Arial", 14), command=self.dar_pista)
        self.pista_button.pack(pady=5)
        
        self.pistas = []  # Inicializar la lista de pistas
        
    def verificar(self):
        # Obtener las sospechas del usuario
        sospecha_personaje = self.personaje_entry.get().strip().title()
        sospecha_locacion = self.locacion_entry.get().strip().title()
        sospecha_arma = self.arma_entry.get().strip().title()
        
        resultado = ""
        
        # Verificar si la sospecha es correcta
        if sospecha_personaje in self.personajes:
            if (sospecha_locacion == self.lugar_crimen) and (sospecha_arma == self.arma_crimen):
                resultado += "¡Felicidades! Has descubierto al culpable.\n"
                resultado += "El crimen fue cometido por {} en {} con {}.".format(self.culpable, sospecha_locacion, sospecha_arma)
                print(resultado)  # Imprimir en la consola
                messagebox.showinfo("¡Felicidades!", resultado)
                self.master.quit()
                return
            else:
                resultado += "Tu sospecha no es correcta. {}\n".format(self.personajes[sospecha_personaje]["lugar"])
                messagebox.showerror("¡Sospecha incorrecta!", resultado)
        else:
            messagebox.showerror("Error", "El personaje ingresado no es válido.")
        
        # Limpiar las entradas
        self.personaje_entry.delete(0, tk.END)
        self.locacion_entry.delete(0, tk.END)
        self.arma_entry.delete(0, tk.END)
        # Focus en la primera entrada
        self.personaje_entry.focus_set()
    
    def dar_pista(self):
        if len(self.pistas) < 3 :
            pistas_disponibles = self.lugares.copy()
            pistas_disponibles.append(self.arma_crimen)
            pista = random.choice(pistas_disponibles)
            pistas_disponibles.remove(pista)
            self.pistas.append(pista)
            messagebox.showinfo("Pista", pista)
        else:
            messagebox.showinfo("Pista", "Ya has recibido 3 pistas.")
            

# Crear una ventana Tkinter
root = tk.Tk()
game = ClueGame(root)

# Imprimir en la consola el culpable, el lugar y el arma
print("El crimen fue cometido por {} en {} con {}.".format(game.culpable, game.lugar_crimen, game.arma_crimen))

root.mainloop()
