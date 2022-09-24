import tkinter as tk



def abrirWindowMA():
    windowMA = tk.Tk()
    windowMA.title("Menu Archivos")
    windowMA.columnconfigure([0,4], minsize=250)
    windowMA.rowconfigure([0,8], minsize=200)
    windowMA.configure(background="#0abde3")

    label1 = tk.Label(windowMA, text="Ruta del Archivo Con Nombre:" , bg="#9AECDB")
    label1.grid(row=0,column=1, padx=10)

    textBox1 = tk.Entry(windowMA, text="")
    textBox1.grid(row=0,column=2)

    button1= tk.Button(windowMA, text ="Abrir Archivo", bg="#48dbfb") #Abre el Archivo para poder editarlo
    button1.grid(row=1,column=1, padx=10,pady=10)

    button2= tk.Button(windowMA, text ="Guardar Archivo", bg="#48dbfb") #Guarda el archivo
    button2.grid(row=2,column=1, padx=10,pady=10)

    textBox2 = tk.Entry(windowMA)  
    textBox2.grid(row=3,column=2)

    button3= tk.Button(windowMA, text ="Guardar Archivo Como: ", bg="#48dbfb") #Guarda el Archivo con el nombre especificado
    button3.grid(row=3,column=1, padx=10,pady=10)

    button4= tk.Button(windowMA, text ="Analizar Información de Archivo", bg="#48dbfb") #Imprime la informacion presente en el archivo
    button4.grid(row=4,column=1, padx=10,pady=10)

    button5= tk.Button(windowMA, text ="Revisión de Errores",command=windowMA.destroy, bg="#48dbfb")   #Revisa los Errores del Archivo
    button5.grid(row=5,column=1)

    button5= tk.Button(windowMA, text ="Regresar",command=windowMA.destroy, bg="#ff6b6b")   #Botón de regresar
    button5.grid(row=8,column=2)

    windowMA.mainloop()

abrirWindowMA()