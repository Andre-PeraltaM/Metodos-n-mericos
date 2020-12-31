from tkinter import *
import brain
import biseccion
import BiseccionGrafica
import Newton_Raphson
import results
import matplotlib.pyplot as plt
from tkinter import messagebox


def Grafico1(x):
    ventana = Tk()
    ventana.config(background="#213141")
    ventana.title("Calculadora")
    texto = Entry(ventana, background="white", foreground="black",
                  font=("Open-Sans", 25))

    texto.grid(row=0, column=1, columnspan=8, padx=10,
               pady=50)
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
                       command=lambda: click_boton("√"))
    botonPunto = Button(ventana, text=".", width=5, height=2,
                        command=lambda: click_boton("."))
    botonX = Button(ventana, text="x", width=5, height=2,
                    command=lambda: click_boton("x"))
    botonY = Button(ventana, text="y", width=5, height=2,
                    command=lambda: click_boton("y"))
    botonZ = Button(ventana, text="z", width=5, height=2,
                    command=lambda: click_boton("z"))
    botonabc = Button(ventana, text="abc", width=5, height=2)
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
    botonRaiz.grid(row=1, column=3, padx=5, pady=5)

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

    def borrarElemento():
        x = texto.get()
        texto.delete(0, END)
        texto.insert(0, x[:-1])

    def click_boton(valor):
        i = len(texto.get())
        texto.insert(i, valor)

    def borrar():
        texto.delete(0, END)

    def confirmar():
        if x == 0:  # biseccion

            try:


                for i in range(1):
                    texto_1 = texto.get()

                    objeto = biseccion.Biseccion(texto_1)
                    y = objeto.solucion()
                    ventana.destroy()

                    obj = BiseccionGrafica.Biseccion()
                    obj.calculate(brain.ecuacion(texto_1))


                    cad = str(y[0]) + "\n---------------------\n" + str(y[1])
                    results.Results(cad)

                    # print(y[0])
                    # print(y[1])
                    break

            except Exception as e:
                messagebox.showerror(
                    message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")

        elif x == 2:  # N-R
            try:
                texto_1 = texto.get()
                objeto = Newton_Raphson.NewtonRapson(texto_1)
                y = objeto.calculate()

                cad = str(y[0]) + "\n---------------------\n" + \
                    str(y[1]) + "\n---------------------\n" + str(y[2])
                ventana.destroy()
                results.Results(cad)
                # print(y[0])
                # print(y[1])
                # print(y[2])

            except Exception as e:
                messagebox.showerror(
                    message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")

    ventana.mainloop()
