from tkinter import *
from tkinter import ttk, messagebox

pacientes = []

def registrar():
    nombre = txt_nombre.get()
    edad = txt_edad.get()
    enfermedad = txt_enfermedad.get()
    sintoma = txt_sintoma.get()

    if sintoma.lower() in ["fractura", "convulsiones", "hemorragia"]:
        triaje = "GRAVE"
    else:
        triaje = "LEVE"

    datos = [nombre, edad, enfermedad, triaje]

    pacientes.append(datos)
    tabla.insert("", END, values=datos)

    messagebox.showinfo("Registro", "Paciente registrado")

    txt_nombre.delete(0, END)
    txt_edad.delete(0, END)
    txt_enfermedad.delete(0, END)
    txt_sintoma.delete(0, END)

ventana = Tk()
ventana.title("Sistema Hospitalario")
ventana.geometry("600x400")

Label(ventana, text="Sistema Hospitalario", font=("Arial", 16)).pack(pady=10)

frame = Frame(ventana)
frame.pack()

Label(frame, text="Nombre").grid(row=0, column=0)
txt_nombre = Entry(frame)
txt_nombre.grid(row=0, column=1)

Label(frame, text="Edad").grid(row=1, column=0)
txt_edad = Entry(frame)
txt_edad.grid(row=1, column=1)

Label(frame, text="Enfermedad").grid(row=2, column=0)
txt_enfermedad = Entry(frame)
txt_enfermedad.grid(row=2, column=1)

Label(frame, text="Síntoma").grid(row=3, column=0)
txt_sintoma = Entry(frame)
txt_sintoma.grid(row=3, column=1)

Button(frame, text="Registrar", command=registrar).grid(row=4, column=0, columnspan=2, pady=10)

tabla = ttk.Treeview(
    ventana,
    columns=("Nombre", "Edad", "Enfermedad", "Triaje"),
    show="headings"
)

for col in ("Nombre", "Edad", "Enfermedad", "Triaje"):
    tabla.heading(col, text=col)

tabla.pack(pady=20)

ventana.mainloop()
