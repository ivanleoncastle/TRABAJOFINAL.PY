import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def obtener_informacion_tratamiento(tipo_piel):
    tratamientos = {
        "grasa": "Para la piel grasa, se recomienda usar limpiadores suaves, tónicos astringentes, y evitar cremas muy oleosas. También puedes usar productos que controlen el exceso de sebo.",
        "seca": "La piel seca necesita hidratación. Usa limpiadores suaves sin alcohol, cremas ricas en ceramidas, ácido hialurónico y aceites naturales.",
        "acneica": "Para piel acneica, se recomiendan productos con ácido salicílico, peróxido de benzoilo o retinoides. Evita productos comedogénicos.",
    }
    return tratamientos.get(tipo_piel.lower(), "Lo siento, no tengo información sobre este tipo de piel.")


def procesar_formulario():
    try:
        edad = int(entry_edad.get())
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return


    tipo_piel = tipo_piel_var.get().lower()
    enfermedades_previas = entry_enfermedades.get().lower()
    color_piel = color_piel_var.get().lower()
    tiene_acne = acne_var.get().lower()

    if not color_piel or not enfermedades_previas or not tiene_acne:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    tratamiento = obtener_informacion_tratamiento(tipo_piel)
    resultado = f"Recomendación de tratamiento:\n{tratamiento}"

    if enfermedades_previas == "sí":
        resultado += "\nEs importante consultar con un dermatólogo para un tratamiento más personalizado."

    if tiene_acne == "sí":
        resultado += "\nTe sugerimos revisar opciones de tratamientos para acné, como cremas con ácido salicílico o peróxido de benzoilo."
    if edad >= 85:
        resultado += "\nEdad avanzada se recomienda tratamiento con productos hidratantes y agua micelar"
    if edad < 15:
        resultado += "\n No se recomienda usar productos en niños a menos que sea protectores solares e hidrtantes naturales"
      
    messagebox.showinfo("Resultado del Tratamiento", resultado)


ventana = tk.Tk()
ventana.title("Consulta de Tratamientos Cutáneos")
ventana.geometry("400x400")

# imagen = PhotoImage(file="C:\Users\Gael Castillo\Desktop\trabajo practico 2\tpgi-gihub.py\TRABAJOFINAL.PY\piel.ico")  # Cambia "ruta_de_la_imagen.png" por el nombre de tu archivo
# label_imagen = tk.Label(ventana, image=imagen)
# label_imagen.pack(pady=10)
 

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_tipo_piel = tk.Label(ventana, text="Tipo de piel:")
label_tipo_piel.pack()

tipo_piel_var = tk.StringVar(value="PIEL") 
menu_tipo_piel = tk.OptionMenu(ventana, tipo_piel_var, "grasa", "seca", "acneica")
menu_tipo_piel.pack()


label_enfermedades = tk.Label(ventana, text="¿Enfermedades cutáneas previas? (Sí/No):")
label_enfermedades.pack()
entry_enfermedades = tk.Entry(ventana)
entry_enfermedades.pack()


label_color_piel = tk.Label(ventana, text="Color de piel (claro, medio, oscuro):")
label_color_piel.pack()


color_piel_var = tk.StringVar(value="COLOR")  
menu_color_piel = tk.OptionMenu(ventana, color_piel_var, "blanca", "media", "oscura")
menu_color_piel.pack()

acne_var = tk.StringVar(value = "¿tiene acné?")
menu_acne = tk.OptionMenu(ventana, acne_var, "si", "no")
menu_acne.pack()


boton_procesar = tk.Button(ventana, text="Obtener Tratamiento", command=procesar_formulario)
boton_procesar.pack(pady=20)

ventana.mainloop()