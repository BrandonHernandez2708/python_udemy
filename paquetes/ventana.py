import tkinter as tk 
import time 
class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("640x420")
        self.ventana.resizable(0, 0)
        self.ventana.title("Reloj")
        self.ventana.config(bg="blue")
        self.etiqueta = tk.Label(text="etiqueta",font=("Arial",40),fg="Blue",bg="white",padx=15,pady=15)
        self.etiqueta.place(x=200, y=150)
        self.actualizar()
        self.ventana.mainloop()
    def actualizar(self):
       hora = time.strftime("%H:%M:%S")
       self.etiqueta.configure(text=hora)
       self.etiqueta.after(1000, self.actualizar)
        


if __name__ == "__main__":
 main = Ventana()