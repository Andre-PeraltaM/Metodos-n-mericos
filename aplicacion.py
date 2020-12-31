import grafico1
import grafico2
import grafico3
import grafico4
import graficoMc
from tkinter import *

def funcion(x):
    # Esto es para diferenciar entre las tres tipos de ventanas que vamos a tener
    if x == 0:  # BISECCIÓN
        # Enviamos el número de la clase
        mywindow.destroy()
        grafico1.Grafico1(x)


    elif x == 1:  # punto fijo
        mywindow.destroy()

        grafico4.Grafico4(x)# Este es punto fijo, debe llevar uno especifico para él

    elif x == 2:  # N-R
        mywindow.destroy()

        grafico1.Grafico1(x)  

    elif x == 3:  # McLaurin
        mywindow.destroy()

        graficoMc.GraficoMc(x)

    elif x == 4:  # Lagrange
        mywindow.destroy()

        grafico2.Grafico2(x)

    elif x == 5:  # Mínimos cuadrados
        mywindow.destroy()

        grafico2.Grafico2(x)

    elif x == 6:  # trapecio
        mywindow.destroy()

        grafico3.Grafico3(x)

    elif x == 7:  # Simpson 1/3
        mywindow.destroy()

        grafico3.Grafico3(x)

    elif x == 8:  # Simpson 3/8
        mywindow.destroy()

        grafico3.Grafico3(x)
    elif x == 9: # Simpson 1/3 + Simpson 3/8
        mywindow.destroy()

        grafico3.Grafico3(x)

mywindow = Tk()
mywindow.geometry("600x700")  # -x+3/(x+2)
mywindow.title("Metodos Númericos")
mywindow.resizable(False, False)
mywindow.config(background="#213141")  # AQUI NOS QUEDAMOS

btnBiseccion = Button(mywindow, text="Metodo de bisección", width="30", height="6",
                      bg="#00CD63", command=lambda: funcion(0))  # biseccion.Biseccion(texto.get())
btnBiseccion.place(x=50, y=30)

btnPFijo = Button(mywindow, text="Metodo de Punto fijo", width="30", height="6",
                  bg="#00CD63", command=lambda: funcion(1))  
btnPFijo.place(x=50, y=130)

btnNewton = Button(mywindow, text="Metodo de Newton - Raphson", width="30", height="6",
                   bg="#00CD63", command=lambda:  funcion(2))  
btnNewton.place(x=270, y=30)

btnMcLaurin = Button(mywindow, text="Serie de McLaurin", width="30", height="6",
                     bg="#00CD63", command=lambda: funcion(3)) 
btnMcLaurin.place(x=270, y=130)

btnLagrange = Button(mywindow, text="Polinomio de Lagrange", width="30", height="6",
                     bg="#00CD63", command=lambda: funcion(4))  
btnLagrange.place(x=50, y=250)

btnMinCua = Button(mywindow, text="Minimos cuadrados", width="30", height="6",
                   bg="#00CD63", command=lambda: funcion(5)) 
btnMinCua.place(x=50, y=350)

btnTrapecio = Button(mywindow, text="Método de Trapecio", width="30", height="6", bg="#00CD63",
                   command=lambda: funcion(6))  
btnTrapecio.place(x=50, y=470)

btnSimp1_3 = Button(mywindow, text="Método de Simpson 1/3", width="30", height="6", bg="#00CD63",
                   command=lambda: funcion(7)) 
btnSimp1_3.place(x=50, y=570)

btnSimp3_8 = Button(mywindow, text="Método de Simpson 3/8", width="30", height="6", bg="#00CD63",
                   command=lambda: funcion(8))  
btnSimp3_8.place(x=270, y=570)

btnSimp = Button(mywindow, text="Método de Simpson 1/3 + 3/8", width="30", height="6", bg="#00CD63",
                   command=lambda: funcion(9))  
btnSimp.place(x=270, y=470)

mywindow.mainloop()



