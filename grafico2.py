from tkinter import *
import lagranje
import lagrange2grafica
import minimosCuadrados
import results
import matplotlib.pyplot as plt
from tkinter import messagebox


def Grafico2(x):

    interGrafico = Tk()
    interGrafico.config(background="#213141")
    interGrafico.title("Calculadora")
    texto = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    texto.grid(row=0, column=1, columnspan=8, padx=10,
               pady=50)
    interGrafico.resizable(False, False)
    aa = Label(interGrafico, state="disabled", width=5, height=2,
               background="white", foreground="black", font=("Helvetica", 15), text="X =")
    aa.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
    texto2 = Entry(interGrafico, background="white", foreground="black", font=(
        "Open-Sans", 25))
    texto2.grid(row=1, column=1, columnspan=8, padx=10,
                pady=50)
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
                        height=2, command=lambda: confirmar(texto.get(), texto2.get()))
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
    botonRaiz.grid(row=2, column=3, padx=5, pady=5)
    botonFx.grid(row=4, column=7, padx=5, pady=5)
    botonBorrar.grid(row=2, column=7, padx=5, pady=5)
    boton123.grid(row=6, column=7, padx=5, pady=5)
    botonEnter.grid(row=3, column=7, padx=5, pady=5)
    botonComa = Button(interGrafico, text=",", width=5,
                       height=2, command=lambda: click_boton(","))
    botonComa.grid(row=6, column=1, padx=5, pady=5)

    def borrarElemento():
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
            for i in range(1):
                try:

                    obj = lagranje.lagran(lx, ly)
                    ecuG, ecuM = obj.procedimiento()

                    cad = str(ecuG) + \
                        "\n---------------------------\n" + str(ecuM)
                    interGrafico.destroy()
                    results.Results(cad)
                except Exception as e:
                    messagebox.showerror(
                        message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")

            # print(ecuG)
            # print(ecuM)

        elif x == 5:  # Minimos
            for i in range(1):
                try:

                    obj = minimosCuadrados.miniCuadrados()
                    r1, r2, r3 = obj.procedimiento(lx, ly)
                    cad = str(r1) + "\n---------------------------\n" + \
                        str(r2) + "\n---------------------------\n" + str(r3)
                    interGrafico.destroy()
                    results.Results(cad)

                except Exception as e:
                    messagebox.showerror(
                        message="La función usada es erronea, por favor introduzca una fucnión correcta", title="función erronea")

            # print(r1)
            # print(r2)
            # print(r3)

    interGrafico.mainloop()
