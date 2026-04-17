import tkinter as tk

class VentanaPrincipal(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Ventana con Herencia")
		self.geometry("400x200")

		etiqueta = tk.Label(self, text="Hola, esta ventana hereda de tkinter.Tk")
		etiqueta.pack(pady=20)

		boton = tk.Button(self, text="Cerrar", command=self.destroy)
		boton.pack()

if __name__ == "__main__":
	app = VentanaPrincipal()
	app.mainloop()
