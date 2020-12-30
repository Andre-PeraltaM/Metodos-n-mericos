import puntoFijo
import results
from tkinter import *


def Grafico4(x):
    interGrafico = Tk()
    interGrafico.geometry("1100x700")
    interGrafico.config(background="#213141")
    interGrafico.title("Calculadora")
    interGrafico.resizable(False, False)

    # Entradas de texto y labels ------------------------------------------------------
    func = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    func.grid(row=0, column=1, columnspan=8, padx=10,
              pady=50)
    despUno = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    despUno.grid(row=1, column=1, columnspan=8, padx=10,
                 pady=50)
    despDos = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    despDos.grid(row=2, column=1, columnspan=8, padx=10,
                 pady=50)
    limiteA = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    limiteA.grid(row=0, column=10, columnspan=8, padx=10,
                 pady=50)

    limiteB = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    limiteB.grid(row=1, column=10, columnspan=8, padx=10,
                 pady=50)

    iterations = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    iterations.grid(row=2, column=10, columnspan=8, padx=10,
                    pady=50)

    aa = Label(interGrafico, state="disabled", width=5, height=2,
               background="white", foreground="black", font=("Helvetica", 15), text="f(x) =")
    aa.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
    aaDos = Label(interGrafico, state="disabled", width=12, height=2,
                  background="white", foreground="black", font=("Helvetica", 15), text="Despeje 1 =")
    aaDos.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
    aaTres = Label(interGrafico, state="disabled", width=12, height=2,
                   background="white", foreground="black", font=("Helvetica", 15), text="Despeje 2 =")
    aaTres.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
    aaCuatro = Label(interGrafico, state="disabled", width=15, height=2,
                     background="white", foreground="black", font=("Helvetica", 15), text="Límite a =")
    aaCuatro.grid(row=0, column=9, columnspan=1, padx=5, pady=5)

    aaB = Label(interGrafico, state="disabled", width=15, height=2,
                background="white", foreground="black", font=("Helvetica", 15), text="Límite b =")
    aaB.grid(row=1, column=9, columnspan=1, padx=5, pady=5)

    aaCuatro = Label(interGrafico, state="disabled", width=15, height=2,
                     background="white", foreground="black", font=("Helvetica", 15), text="Nº Iteraciones =")
    aaCuatro.grid(row=2, column=9, columnspan=1, padx=5, pady=5)

    # -------------------------------------------------------------------------------

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
                        height=2, command=lambda: confirmar(func.get(), despUno.get(), despDos.get(), int(limiteA.get()), int(limiteB.get()), int(iterations.get())))
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
                       height=2, command=lambda: click_boton("√"))
    botonPunto = Button(interGrafico, text=".", width=5,
                        height=2, command=lambda: click_boton("."))
    botonX = Button(interGrafico, text="x", width=5, height=2,
                    command=lambda: click_boton("x"))
    botonY = Button(interGrafico, text="y", width=5, height=2,
                    command=lambda: click_boton("y"))
    botonZ = Button(interGrafico, text="z", width=5, height=2,
                    command=lambda: click_boton("z"))
    botonabc = Button(interGrafico, text="abc", width=5, height=2)
    botonFx = Button(interGrafico, text="f(x)", width=5, height=2)
    boton123 = Button(interGrafico, text="123", width=5, height=2)
    botonBorrarTodo.grid(row=3, column=8, padx=5, pady=5)
    botonParentesisAbre.grid(row=3, column=1, padx=5, pady=5)
    botonParentesisCierre.grid(row=3, column=2, padx=5, pady=5)
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

    # Grid de botones -------------------------------------------------------------
    botonSin.grid(row=3, column=5, padx=5, pady=5)
    botonCos.grid(row=4, column=5, padx=5, pady=5)
    botonTan.grid(row=5, column=5, padx=5, pady=5)
    botonLog.grid(row=6, column=5, padx=5, pady=5)
    botonXelavado.grid(row=7, column=5, padx=5, pady=5)
    botonRaiz_x.grid(row=3, column=6, padx=5, pady=5)
    botonRaiz_3.grid(row=4, column=6, padx=5, pady=5)
    botonFactorial.grid(row=5, column=6, padx=5, pady=5)
    botonpi.grid(row=6, column=6, padx=5, pady=5)
    botone.grid(row=7, column=6, padx=5, pady=5)
    botonX.grid(row=4, column=0, padx=5, pady=5)
    botonY.grid(row=5, column=0, padx=5, pady=5)
    botonZ.grid(row=6, column=0, padx=5, pady=5)
    botonabc.grid(row=6, column=7, padx=5, pady=5)
    boton1.grid(row=6, column=1, padx=5, pady=5)
    boton2.grid(row=6, column=2, padx=5, pady=5)
    boton3.grid(row=6, column=3, padx=5, pady=5)
    boton4.grid(row=5, column=1, padx=5, pady=5)
    boton5.grid(row=5, column=2, padx=5, pady=5)
    boton6.grid(row=5, column=3, padx=5, pady=5)
    boton7.grid(row=4, column=1, padx=5, pady=5)
    boton8.grid(row=4, column=2, padx=5, pady=5)
    boton9.grid(row=4, column=3, padx=5, pady=5)
    boton0.grid(row=7, column=2, padx=5, pady=5)
    botonPunto.grid(row=7, column=3, padx=5, pady=5)
    botonProducto.grid(row=3, column=4, padx=5, pady=5)
    botonDivision.grid(row=4, column=4, padx=5, pady=5)
    botonResta.grid(row=5, column=4, padx=5, pady=5)
    botonSuma.grid(row=6, column=4, padx=5, pady=5)
    botonElevar.grid(row=7, column=4, padx=5, pady=5)
    botonRaiz.grid(row=3, column=3, padx=5, pady=5)
    botonFx.grid(row=5, column=7, padx=5, pady=5)
    botonBorrar.grid(row=3, column=7, padx=5, pady=5)
    boton123.grid(row=7, column=7, padx=5, pady=5)
    botonEnter.grid(row=4, column=7, padx=5, pady=5)
    botonComa = Button(interGrafico, text=",", width=5,
                       height=2, command=lambda: click_boton(","))
    botonComa.grid(row=7, column=1, padx=5, pady=5)

    def borrarElemento():
        x = func.get()
        func.delete(0, END)
        func.insert(0, x[:-1])
        despUno.delete(0, END)
        despDos.delete(0, END)
        despDos.insert(0, x[:-1])
        limiteA.delete(0, END)
        limiteA.insert(0, x[:-1])
        iterations.delete(0, END)
        iterations.insert(0, x[:-1])

        limiteB.delete(0, END)
        limiteB.insert(0, x[:-1])

    def click_boton(valor):
        if func.tk_focusNext():
            i = len(func.get())
            func.insert(i, valor)
        elif despUno.tk_focusNext():
            i = len(despUno.get())
            despUno.insert(i, valor)
        elif despDos.tk_focusNext():
            i = len(despDos.get())
            despDos.insert(i, valor)
        elif limiteA.tk_focusNext():
            i = len(limiteA.get())
            limiteA.insert(i, valor)
        elif limiteB.tk_focusNext():
            i = len(limiteB.get())
            limiteB.insert(i, valor)
        elif iterations.tk_focusNext():
            i = len(iterations.get())
            iterations.insert(i, valor)

        '''
        textoDos.insert(i, valor)
        textoTres.insert(i, valor)
        textoCuatro.insert(i, valor)
        textoCinco.insert(i, valor)
		'''

    def borrar():
        func.delete(0, END)
        despUno.delete(0, END)
        despDos.delete(0, END)
        limiteA.delete(0, END)
        limiteB.delete(0, END)
        iterations.delete(0, END)

    def confirmar(ecu, despUno, despDos, valA, valB, iterations):
        if x == 1:
            for i in range(1):
                try:

                    obj = puntoFijo.PuntoFijo(
                        ecu, despUno, despDos, valA, valB, iterations)
                    finalResultsOne, finalResultsTwo = obj.calculate()
                    cad = str(finalResultsOne) + \
                        "\n---------------------------------\n" + str(finalResultsTwo)
                    interGrafico.destroy()
                    results.Results(cad)
                except Exception as e:
                    messagebox.showerror(message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")
 


    interGrafico.mainloop()
