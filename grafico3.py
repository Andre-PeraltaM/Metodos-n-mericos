from tkinter import *
import lagranje
import lagrange2grafica
import minimosCuadrados
import matplotlib.pyplot as plt
from tkinter import messagebox
import simpson1_3
import simpson3_8
import simpson
import trapecio
import results


def Grafico3(x):

    interGrafico = Tk()
    interGrafico.geometry("1100x700")
    interGrafico.config(background="#213141")
    interGrafico.title("Calculadora")
    interGrafico.resizable(False, False)

    # Entradas de texto y labels ------------------------------------------------------
    texto = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    texto.grid(row=0, column=1, columnspan=8, padx=10,
               pady=50)
    textoDos = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    textoDos.grid(row=1, column=1, columnspan=8, padx=10,
                  pady=50)
    textoTres = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    textoTres.grid(row=0, column=10, columnspan=8, padx=10,
                   pady=50)

    textoCinco = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    textoCinco.grid(row=1, column=10, columnspan=8, padx=10,
                    pady=50)

    aa = Label(interGrafico, state="disabled", width=5, height=2,
               background="white", foreground="black", font=("Helvetica", 15), text="∫")
    aa.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
    aaDos = Label(interGrafico, state="disabled", width=12, height=2,
                  background="white", foreground="black", font=("Helvetica", 15), text="a")
    aaDos.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
    aaTres = Label(interGrafico, state="disabled", width=12, height=2,
                   background="white", foreground="black", font=("Helvetica", 15), text="b")
    aaTres.grid(row=0, column=9, columnspan=1, padx=5, pady=5)

    aaCuatro = Label(interGrafico, state="disabled", width=15, height=2,
                     background="white", foreground="black", font=("Helvetica", 15), text="Nº Iteraciones =")
    aaCuatro.grid(row=1, column=9, columnspan=1, padx=5, pady=5)

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
                        height=2, command=lambda: confirmar(texto.get(), int(textoDos.get()), int(textoTres.get()),  int(textoCinco.get())))
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
        x = texto.get()
        texto.delete(0, END)
        texto.insert(0, x[:-1])
        textoDos.delete(0, END)
        textoTres.delete(0, END)
        textoTres.insert(0, x[:-1])
       # #textoCuatro.delete(0, END)
       # #textoCuatro.insert(0, x[:-1])
        textoCinco.delete(0, END)
        textoCinco.insert(0, x[:-1])

    def click_boton(valor):
        i = len(texto.get())
        if texto.tk_focusNext():
            texto.insert(i, valor)
        elif textoDos.tk_focusPrev():
            textoDos.insert(i, valor)
        elif textoTres.tk_focusNext():
            textoTres.insert(i, valor)
        # elif #textoCuatro.tk_focusNext():
        #     #textoCuatro.insert(i, valor)
        elif textoCinco.tk_focusNext():
            textoCinco.insert(i, valor)

        '''
        textoDos.insert(i, valor)
        textoTres.insert(i, valor)
        #textoCuatro.insert(i, valor)
        textoCinco.insert(i, valor)
		'''

    def borrar():
        texto.delete(0, END)
        textoDos.delete(0, END)
        textoTres.delete(0, END)
        ##textoCuatro.delete(0, END)
        textoCinco.delete(0, END)

    def confirmar(fun, a, b, itr):
        if x == 6:  # trapecio
            objeto = trapecio.trapecio_1(fun, a, b, itr)
            y = objeto.operacion()

            cad = str(y[0]) + "\n-----------------------\n" + \
                str(y[1]) + "\n-----------------------\n" + str(y[2])
            interGrafico.destroy()
            results.Results(cad)

            # print(y[0])
            # print(y[1])
            # print(y[2])

        elif x == 7:  # simpson 1/3
            objeto = simpson1_3.simpson_tercio(fun, a, b, itr)
            y = objeto.operacion()

            cad = str(y[0]) + "\n-----------------------\n" + \
                str(y[1]) + "\n-----------------------\n" + str(y[2])
            interGrafico.destroy()
            results.Results(cad)

            # print(y[0])
            # print(y[1])
            # print(y[2])

        elif x == 8:  # simpson 3/8
            objeto = simpson3_8.simpson_tresoctavos(fun, a, b, itr)
            y = objeto.operacion()

            cad = str(y[0]) + "\n-----------------------\n" + \
                str(y[1]) + "\n-----------------------\n" + str(y[2])
            interGrafico.destroy()
            results.Results(cad)

            # print(y[0])
            # print(y[1])
            # print(y[2])

        elif x == 9:  # simpsonS
            for i in range(1):
                try:

                    objeto = simpson.Simp(fun, a, b, itr)
                    y = objeto.solucion()

                    cad = str(y[0]) + "\n-----------------------\n" + \
                        str(y[1]) + "\n-----------------------\n" + str(y[2])
                    interGrafico.destroy()
                    results.Results(cad)

                    # print(y[0])
                    # print(y[1])
                    # print(y[2])
                except Exception as e:
                    messagebox.showerror(
                        message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")

    interGrafico.mainloop()
