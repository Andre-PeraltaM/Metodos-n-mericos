import biseccion
import minimosCuadrados
import brain
import lagranje
import lagrange2grafica
import matplotlib.pyplot as plt


from tkinter import *


def funcion(x):
    # Esto es para diferenciar entre las tres tipos de ventanas que vamos a tener
    if x == 0:  # BISECCIÓN
        # Enviamos el número de la clase
        Grafico1(x)

    elif x == 1:  # punto fijo
        Grafico1(x)

    elif x == 2:  # N-R
        Grafico1(x)  # Este es punto fijo, debe llevar uno especifico para él

    elif x == 3:  # McLaurin
        Grafico1(x)

    elif x == 4:  # Lagrange
        Grafico2(x)

    elif x == 5:  # Mínimos cuadrados
        Grafico2(x)

    elif x == 6:  # trapecio
        Grafico2(x)

    elif x == 7:  # Simpson
        Grafico2(x)


def Grafico2(x):

    mywindow.withdraw()
    interGrafico = Tk()  # Creamos interGrafico
    interGrafico.config(background="#213141")  # Color de la interGrafico
    interGrafico.title("Calculadora")  # Titulo
    texto = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))  # Tipo de letra en la entrada
    texto.grid(row=0, column=1, columnspan=8, padx=10,
               pady=50)  # Posición de la entrada de texto
    # Esto es para que la interGrafico no pueda ser cambiada de tamaño
    interGrafico.resizable(False, False)
    aa = Label(interGrafico, state="disabled", width=5, height=2,
               background="white", foreground="black", font=("Helvetica", 15), text="X =")
    aa.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
    texto2 = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))  # Tipo de letra en la entrada
    texto2.grid(row=1, column=1, columnspan=8, padx=10,
                pady=50)  # Posición de la entrada de texto
    aa2 = Label(interGrafico, state="disabled", width=5, height=2,
                background="white", foreground="black", font=("Helvetica", 15), text="Y =")
    aa2.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
    boton1 = Button(interGrafico, text="1", width=5,
                    height=2, command=lambda: click_boton(1))
    boton2 = Button(interGrafico, text="2", width=5,
                    height=2, command=lambda: click_boton(2))
    boton3 = Button(interGrafico, text="3", width=5,
                    height=2, command=lambda: click_boton(3))
    boton4 = Button(interGrafico, text="4", width=5,
                    height=2, command=lambda: click_boton(4))
    boton5 = Button(interGrafico, text="5", width=5,
                    height=2, command=lambda: click_boton(5))
    boton6 = Button(interGrafico, text="6", width=5,
                    height=2, command=lambda: click_boton(6))
    boton7 = Button(interGrafico, text="7", width=5,
                    height=2, command=lambda: click_boton(7))
    boton8 = Button(interGrafico, text="8", width=5,
                    height=2, command=lambda: click_boton(8))
    boton9 = Button(interGrafico, text="9", width=5,
                    height=2, command=lambda: click_boton(9))
    boton0 = Button(interGrafico, text="0", width=5,
                    height=2, command=lambda: click_boton(0))
    botonBorrarTodo = Button(interGrafico, text="AC",
                             width=5, height=2, command=lambda: borrar())
    botonBorrar = Button(interGrafico, text="⌫", width=5,
                         height=2, command=lambda: borrarElemento())
    botonEnter = Button(interGrafico, text="Enter", width=5,
                        height=2, command=lambda: confirmar( texto.get(), texto2.get() ))
    botonResta = Button(interGrafico, text="-", width=5,
                        height=2, command=lambda: click_boton("-"))
    botonSuma = Button(interGrafico, text="+", width=5,
                       height=2, command=lambda: click_boton("+"))
    botonDivision = Button(interGrafico, text="÷", width=5,
                           height=2, command=lambda: click_boton("/"))
    botonProducto = Button(interGrafico, text="*", width=5,
                           height=2, command=lambda: click_boton("*"))
    botonElevar = Button(interGrafico, text="^", width=5,
                         height=2, command=lambda: click_boton("^"))
    botonParentesisAbre = Button(
        interGrafico, text="(", width=5, height=2, command=lambda: click_boton("("))
    botonParentesisCierre = Button(
        interGrafico, text=")", width=5, height=2, command=lambda: click_boton(")"))
    botonRaiz = Button(interGrafico, text="√", width=5,
                       height=2, command=lambda: click_boton("√"))  # \sqrt()
    botonPunto = Button(interGrafico, text=".", width=5,
                        height=2, command=lambda: click_boton("."))
    botonX = Button(interGrafico, text="x", width=5, height=2,
                    command=lambda: click_boton("x"))
    botonY = Button(interGrafico, text="y", width=5, height=2,
                    command=lambda: click_boton("y"))
    botonZ = Button(interGrafico, text="z", width=5, height=2,
                    command=lambda: click_boton("z"))
    botonabc = Button(interGrafico, text="abc", width=5, height=2)  # EN ESPERA
    botonFx = Button(interGrafico, text="f(x)", width=5, height=2)
    boton123 = Button(interGrafico, text="123", width=5, height=2)
    botonBorrarTodo.grid(row=2, column=8, padx=5, pady=5)
    botonParentesisAbre.grid(row=2, column=1, padx=5, pady=5)
    botonParentesisCierre.grid(row=2, column=2, padx=5, pady=5)
    botonSin = Button(interGrafico, text="Sen(x)", width=5,
                      height=2, command=lambda: click_boton("sen()"))
    botonCos = Button(interGrafico, text="Cos(x)", width=5,
                      height=2, command=lambda: click_boton("cos()"))
    botonTan = Button(interGrafico, text="Tan(x)", width=5,
                      height=2, command=lambda: click_boton("tan()"))
    botonLog = Button(interGrafico, text="Log(x)", width=5,
                      height=2, command=lambda: click_boton("log()"))
    botonXelavado = Button(interGrafico, text="X^y", width=5,
                           height=2, command=lambda: click_boton("X^"))
    botonRaiz_x = Button(interGrafico, text="x√", width=5,
                         height=2, command=lambda: click_boton("x√"))
    botonRaiz_3 = Button(interGrafico, text="3√", width=5,
                         height=2, command=lambda: click_boton("3√"))
    botonFactorial = Button(interGrafico, text="!", width=5,
                            height=2, command=lambda: click_boton("!"))
    botonpi = Button(interGrafico, text="π", width=5,
                     height=2, command=lambda: click_boton("π"))
    botone = Button(interGrafico, text="e", width=5, height=2,
                    command=lambda: click_boton("e"))
    botonSin.grid(row=2, column=5, padx=5, pady=5)
    botonCos.grid(row=3, column=5, padx=5, pady=5)
    botonTan.grid(row=4, column=5, padx=5, pady=5)
    botonLog.grid(row=5, column=5, padx=5, pady=5)
    botonXelavado.grid(row=6, column=5, padx=5, pady=5)
    botonRaiz_x.grid(row=2, column=6, padx=5, pady=5)
    botonRaiz_3.grid(row=3, column=6, padx=5, pady=5)
    botonFactorial.grid(row=4, column=6, padx=5, pady=5)
    botonpi.grid(row=5, column=6, padx=5, pady=5)
    botone.grid(row=6, column=6, padx=5, pady=5)
    botonX.grid(row=3, column=0, padx=5, pady=5)
    botonY.grid(row=4, column=0, padx=5, pady=5)
    botonZ.grid(row=5, column=0, padx=5, pady=5)
    botonabc.grid(row=5, column=7, padx=5, pady=5)
    boton1.grid(row=5, column=1, padx=5, pady=5)
    boton2.grid(row=5, column=2, padx=5, pady=5)
    boton3.grid(row=5, column=3, padx=5, pady=5)
    boton4.grid(row=4, column=1, padx=5, pady=5)
    boton5.grid(row=4, column=2, padx=5, pady=5)
    boton6.grid(row=4, column=3, padx=5, pady=5)
    boton7.grid(row=3, column=1, padx=5, pady=5)
    boton8.grid(row=3, column=2, padx=5, pady=5)
    boton9.grid(row=3, column=3, padx=5, pady=5)
    boton0.grid(row=6, column=2, padx=5, pady=5)
    botonPunto.grid(row=6, column=3, padx=5, pady=5)
    botonProducto.grid(row=2, column=4, padx=5, pady=5)
    botonDivision.grid(row=3, column=4, padx=5, pady=5)
    botonResta.grid(row=4, column=4, padx=5, pady=5)
    botonSuma.grid(row=5, column=4, padx=5, pady=5)
    botonElevar.grid(row=6, column=4, padx=5, pady=5)
    botonRaiz.grid(row=2, column=3, padx=5, pady=5)  # \sqrt()
    botonFx.grid(row=4, column=7, padx=5, pady=5)
    botonBorrar.grid(row=2, column=7, padx=5, pady=5)
    boton123.grid(row=6, column=7, padx=5, pady=5)
    botonEnter.grid(row=3, column=7, padx=5, pady=5)
    botonComa = Button(interGrafico, text=",", width=5,
                       height=2, command=lambda: click_boton(","))
    botonComa.grid(row=6, column=1, padx=5, pady=5)

    def borrarElemento():  # PENDIENTE
        x = texto.get()
        texto.delete(0, END)
        texto.insert(0, x[:-1])

    def click_boton(valor):
        i = len(texto.get())
        texto.insert(i, valor)

    def borrar():
        texto.delete(0, END)

    def confirmar(lx, ly):
        
        if x == 4:
            obj = lagranje.lagran(lx, ly)
            ecuG, ecuM = obj.procedimiento()
            print(ecuG)
            print(ecuM)
            
            plot = lagrange2grafica.Lagrange(lx, ly)
            selfx, selfy, xplt, yplt = plot.calculate()
            
            # #ploting
            plt.plot(selfx, selfy, 'ro', xplt, yplt, 'b-')
            plt.xlabel('X')
            plt.ylabel('Y')
            winTitle = plt.gcf()
            winTitle.canvas.set_window_title("LAGRANGE")
            plt.grid()
            plt.show()

            

    interGrafico.mainloop()


def Grafico1(x):
    mywindow.withdraw()
    ventana = Tk()  # Creamos ventana

    ventana.config(background="#213141")  # Color de la ventana
    ventana.title("Calculadora")  # Titulo
    texto = Entry(ventana, background="white", foreground="black",
                  font=("Open-Sans", 25))  # Tipo de letra en la entrada

    texto.grid(row=0, column=1, columnspan=8, padx=10,
               pady=50)  # Posición de la entrada de texto
    # El 10 es el espacio a los lados, el 5 el espacio de arriba a abajo entre la ventana y la entrada de texto
    # Esto es para que la ventana no pueda ser cambiada de tamaño
    ventana.resizable(False, False)
    aa = Label(ventana, state="disabled", width=5, height=2, background="white",
               foreground="black", font=("Helvetica", 15), text="f(x)=")
    aa.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

    boton1 = Button(ventana, text="1", width=5, height=2,
                    command=lambda: click_boton(1))
    boton2 = Button(ventana, text="2", width=5, height=2,
                    command=lambda: click_boton(2))
    boton3 = Button(ventana, text="3", width=5, height=2,
                    command=lambda: click_boton(3))
    boton4 = Button(ventana, text="4", width=5, height=2,
                    command=lambda: click_boton(4))
    boton5 = Button(ventana, text="5", width=5, height=2,
                    command=lambda: click_boton(5))
    boton6 = Button(ventana, text="6", width=5, height=2,
                    command=lambda: click_boton(6))
    boton7 = Button(ventana, text="7", width=5, height=2,
                    command=lambda: click_boton(7))
    boton8 = Button(ventana, text="8", width=5, height=2,
                    command=lambda: click_boton(8))
    boton9 = Button(ventana, text="9", width=5, height=2,
                    command=lambda: click_boton(9))
    boton0 = Button(ventana, text="0", width=5, height=2,
                    command=lambda: click_boton(0))
    botonBorrarTodo = Button(ventana, text="AC", width=5,
                             height=2, command=lambda: borrar())
    botonBorrar = Button(ventana, text="⌫", width=5,
                         height=2, command=lambda: borrarElemento())
    botonEnter = Button(ventana, text="Enter", width=5,
                        height=2, command=lambda: confirmar())
    botonResta = Button(ventana, text="-", width=5, height=2,
                        command=lambda: click_boton("-"))
    botonSuma = Button(ventana, text="+", width=5, height=2,
                       command=lambda: click_boton("+"))
    botonDivision = Button(ventana, text="÷", width=5,
                           height=2, command=lambda: click_boton("/"))
    botonProducto = Button(ventana, text="*", width=5,
                           height=2, command=lambda: click_boton("*"))
    botonElevar = Button(ventana, text="^", width=5,
                         height=2, command=lambda: click_boton("^"))
    botonParentesisAbre = Button(
        ventana, text="(", width=5, height=2, command=lambda: click_boton("("))
    botonParentesisCierre = Button(
        ventana, text=")", width=5, height=2, command=lambda: click_boton(")"))
    botonRaiz = Button(ventana, text="√", width=5, height=2,
                       command=lambda: click_boton("√"))  # \sqrt()
    botonPunto = Button(ventana, text=".", width=5, height=2,
                        command=lambda: click_boton("."))
    botonX = Button(ventana, text="x", width=5, height=2,
                    command=lambda: click_boton("x"))
    botonY = Button(ventana, text="y", width=5, height=2,
                    command=lambda: click_boton("y"))
    botonZ = Button(ventana, text="z", width=5, height=2,
                    command=lambda: click_boton("z"))
    botonabc = Button(ventana, text="abc", width=5, height=2)  # EN ESPERA
    botonFx = Button(ventana, text="f(x)", width=5, height=2)
    boton123 = Button(ventana, text="123", width=5, height=2)

    botonParentesisAbre.grid(row=1, column=1, padx=5, pady=5)
    botonParentesisCierre.grid(row=1, column=2, padx=5, pady=5)

    botonSin = Button(ventana, text="Sen(x)", width=5,
                      height=2, command=lambda: click_boton("sen()"))
    botonCos = Button(ventana, text="Cos(x)", width=5,
                      height=2, command=lambda: click_boton("cos()"))
    botonTan = Button(ventana, text="Tan(x)", width=5,
                      height=2, command=lambda: click_boton("tan()"))
    botonLog = Button(ventana, text="Log(x)", width=5,
                      height=2, command=lambda: click_boton("log()"))
    botonXelavado = Button(ventana, text="X^y", width=5,
                           height=2, command=lambda: click_boton("X^"))
    botonRaiz_x = Button(ventana, text="x√", width=5,
                         height=2, command=lambda: click_boton("x√"))
    botonRaiz_3 = Button(ventana, text="3√", width=5,
                         height=2, command=lambda: click_boton("3√"))
    botonFactorial = Button(ventana, text="!", width=5,
                            height=2, command=lambda: click_boton("!"))
    botonpi = Button(ventana, text="π", width=5, height=2,
                     command=lambda: click_boton("π"))
    botone = Button(ventana, text="e", width=5, height=2,
                    command=lambda: click_boton("e"))
    botonSin.grid(row=1, column=5, padx=5, pady=5)
    botonCos.grid(row=2, column=5, padx=5, pady=5)
    botonTan.grid(row=3, column=5, padx=5, pady=5)
    botonLog.grid(row=4, column=5, padx=5, pady=5)
    botonXelavado.grid(row=5, column=5, padx=5, pady=5)
    botonRaiz_x.grid(row=1, column=10, padx=5, pady=5)
    botonRaiz_3.grid(row=2, column=10, padx=5, pady=5)
    botonFactorial.grid(row=3, column=10, padx=5, pady=5)
    botonpi.grid(row=4, column=10, padx=5, pady=5)
    botone.grid(row=5, column=10, padx=5, pady=5)

    botonX.grid(row=2, column=0, padx=5, pady=5)
    botonY.grid(row=3, column=0, padx=5, pady=5)
    botonZ.grid(row=4, column=0, padx=5, pady=5)

    boton1.grid(row=4, column=1, padx=5, pady=5)
    boton2.grid(row=4, column=2, padx=5, pady=5)
    boton3.grid(row=4, column=3, padx=5, pady=5)
    boton4.grid(row=3, column=1, padx=5, pady=5)
    boton5.grid(row=3, column=2, padx=5, pady=5)
    boton6.grid(row=3, column=3, padx=5, pady=5)
    boton7.grid(row=2, column=1, padx=5, pady=5)
    boton8.grid(row=2, column=2, padx=5, pady=5)
    boton9.grid(row=2, column=3, padx=5, pady=5)
    boton0.grid(row=5, column=2, padx=5, pady=5)
    botonPunto.grid(row=5, column=3, padx=5, pady=5)
    botonProducto.grid(row=1, column=4, padx=5, pady=5)
    botonDivision.grid(row=2, column=4, padx=5, pady=5)
    botonResta.grid(row=3, column=4, padx=5, pady=5)
    botonSuma.grid(row=4, column=4, padx=5, pady=5)
    botonElevar.grid(row=5, column=4, padx=5, pady=5)
    botonRaiz.grid(row=1, column=3, padx=5, pady=5)  # \sqrt()

    botonFx.grid(row=3, column=11, padx=5, pady=5)
    botonBorrar.grid(row=1, column=11, padx=5, pady=5)
    boton123.grid(row=5, column=11, padx=5, pady=5)
    botonEnter.grid(row=2, column=11, padx=5, pady=5)
    botonabc.grid(row=4, column=11, padx=5, pady=5)
    botonBorrarTodo.grid(row=1, column=12, padx=5, pady=5)

    sec = Button(ventana, text="Sec", width=5, height=2,
                 command=lambda: click_boton("sec()"))
    csc = Button(ventana, text="Csc", width=5, height=2,
                 command=lambda: click_boton("csc()"))
    cot = Button(ventana, text="Cot", width=5, height=2,
                 command=lambda: click_boton("cot()"))
    senh = Button(ventana, text="Senh", width=5, height=2,
                  command=lambda: click_boton("senh()"))
    cosh = Button(ventana, text="Cosh", width=5, height=2,
                  command=lambda: click_boton("cosh()"))
    tanh = Button(ventana, text="Tanh", width=5, height=2,
                  command=lambda: click_boton("tanh()"))
    sin1 = Button(ventana, text="Sin^-1", width=5, height=2,
                  command=lambda: click_boton("sin^-1()"))
    cos1 = Button(ventana, text="cos^-1", width=5, height=2,
                  command=lambda: click_boton("cos^-1()"))
    tan1 = Button(ventana, text="tan^-1", width=5, height=2,
                  command=lambda: click_boton("tan^-1()"))
    Ln = Button(ventana, text="Ln", width=5, height=2,
                command=lambda: click_boton("Ln()"))
    acos = Button(ventana, text="acos", width=5, height=2,
                  command=lambda: click_boton("acos()"))
    asin = Button(ventana, text="asin", width=5, height=2,
                  command=lambda: click_boton("asin()"))
    atan = Button(ventana, text="atan", width=5, height=2,
                  command=lambda: click_boton("atan()"))
    sec.grid(row=1, column=6, padx=5, pady=5)
    csc.grid(row=2, column=6, padx=5, pady=5)
    cot.grid(row=3, column=6, padx=5, pady=5)
    senh.grid(row=1, column=7, padx=5, pady=5)
    cosh.grid(row=2, column=7, padx=5, pady=5)
    tanh.grid(row=3, column=7, padx=5, pady=5)
    sin1.grid(row=1, column=8, padx=5, pady=5)
    cos1.grid(row=2, column=8, padx=5, pady=5)
    tan1.grid(row=3, column=8, padx=5, pady=5)
    Ln.grid(row=4, column=6, padx=5, pady=5)
    acos.grid(row=1, column=9, padx=5, pady=5)
    asin.grid(row=2, column=9, padx=5, pady=5)
    atan.grid(row=3, column=9, padx=5, pady=5)
    botonComa = Button(ventana, text=",", width=5, height=2,
                       command=lambda: click_boton(","))
    botonComa.grid(row=5, column=1, padx=5, pady=5)

    def borrarElemento():  # PENDIENTE
        x = texto.get()
        texto.delete(0, END)
        texto.insert(0, x[:-1])

    def click_boton(valor):
        i = len(texto.get())
        texto.insert(i, valor)

    def borrar():
        texto.delete(0, END)

# ----------PIDEN FUNCIÓN

    def confirmar():
        if x == 0:  # biseccion
            objeto = biseccion.Biseccion(str(texto.get()))
            y = objeto.solucion()
            print(y[0])
            print(y[1])

        elif x == 1:  # N-R
            objeto = '3'

        elif x == 2:  # McLaurin
            objeto = '3'


# De aquí para abajo es la primer ventana


mywindow = Tk()
mywindow.geometry("600x550")  # -x+3/(x+2)
mywindow.title("Registration Form - Python + Tkinter")
mywindow.resizable(False, False)
mywindow.config(background="#213141")  # AQUI NOS QUEDAMOS

btnBiseccion = Button(mywindow, text="Metodo de bisección", width="30", height="6",
                      bg="#00CD63", command=lambda: funcion(0))  # biseccion.Biseccion(texto.get())
btnBiseccion.place(x=50, y=30)

btnPFijo = Button(mywindow, text="Metodo de Punto fijo", width="30", height="6",
                  bg="#00CD63", command=lambda: funcion(1))  # fijo.PuntoFijo(texto.get())
btnPFijo.place(x=50, y=130)

btnNewton = Button(mywindow, text="Metodo de Newton - Raphson", width="30", height="6",
                   bg="#00CD63", command=lambda:  funcion(2))  # newtonRaphson.NewtonRaphson(texto.get())
btnNewton.place(x=50, y=230)

btnMcLaurin = Button(mywindow, text="Serie de McLaurin", width="30", height="6",
                     bg="#00CD63", command=lambda: funcion(3))  # mcLaurin.McLaurin(texto.get())
btnMcLaurin.place(x=50, y=330)

btnLagrange = Button(mywindow, text="Polinomio de Lagrange", width="30", height="6",
                     bg="#00CD63", command=lambda: funcion(4))  # interpolacionLineal.lineal(texto.get())
btnLagrange.place(x=270, y=30)

btnInterP = Button(mywindow, text="Interpolacion", width="30", height="6", bg="#00CD63",
                   command=lambda: funcion(5))  # interpolacionLineal.lineal(texto.get())
btnInterP.place(x=50, y=430)

btnMinCua = Button(mywindow, text="Minimos cuadrados", width="30", height="6",
                   bg="#00CD63", command=lambda: funcion(6))  # interpolacionLineal.lineal(texto.get())
btnMinCua.place(x=270, y=130)


mywindow.mainloop()
