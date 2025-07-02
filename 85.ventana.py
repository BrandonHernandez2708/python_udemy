from tkinter import *
ventana = Tk()
ventana.title("mi primerva ventana con python")
ventana.resizable(True, True)
#ventana.iconbitmap("icono.ico")
#ventana.geometry("640x320")
ventana.config(bg="red")
frame = Frame()

frame.pack(side = "right", anchor="s")


frame.config(bg="yellow")
frame.config(width=640, height=320)

ventana.mainloop()
