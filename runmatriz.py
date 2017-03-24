import matriz

def main():
    def matriz_determinante():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_det(a)

    def matriz_inver():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_inversa(a)

    def transpuesta():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.transpuesta()

    def matriz_numero():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_numero()

    def matriz_elevada():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        matrizA.matriz_elevada()

    def matrizSimetrica():
        matrizA = matriz.Matriz()
        matrizA.matrizSimetrica()

    def matrizidentica():
        matrizA = matriz.Matriz()
        matrizA.matrizidentica()

    def multiplicacionmatriz():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

        matrizB = matriz.Matriz()
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprime_matrizC()

        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()
        matrizA.multiplicacionmatriz(filasA, columnasB, filasB, columnasA, a, b)

    def sumamatriz():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

        matrizB = matriz.Matriz()
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprime_matrizC()

        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()
        matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

    def restamatriz():
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

        matrizB = matriz.Matriz()
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprime_matrizC()

        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()
        matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

    M = False
    while M!=True:

            mi_menu = matriz.Menu()
            a=mi_menu.loop()

            if a == 1:
                hilo1 = threading.Thread(target=matriz_determinante, args=())
                hilo1.start()
                hilo1.join()

            if a == 2:
                hilo2 = threading.Thread(target=matriz_inver, args=())
                hilo2.start()
                hilo2.join()

            if a == 3:
                hilo3 = threading.Thread(target=transpuesta, args=())
                hilo3.start()
                hilo3.join()

            if a == 4:
                hilo4 = threading.Thread(target=matriz_numero, args=())
                hilo4.start()
                hilo4.join()

            if a == 5:
                hilo5 = threading.Thread(target=matriz_elevada, args=())
                hilo5.start()
                hilo5.join()

            if a == 6:
                hilo6 = threading.Thread(target=matrizSimetrica(), args=())
                hilo6.start()
                hilo6.join()

            if a == 7:
                hilo7 = threading.Thread(target=matrizidentica(), args=())
                hilo7.start()
                hilo7.join()

            if a == 8:
                hilo8 = threading.Thread(target=multiplicacionmatriz(), args=())
                hilo8.start()
                hilo8.join()

            if a == 9:
                hilo9 = threading.Thread(target=sumamatriz(), args=())
                hilo9.start()
                hilo9.join()

            if a == 10:
                hilo10 = threading.Thread(target=restamatriz(), args=())
                hilo10.start()
                hilo10.join()

            if a == 11:
                print "Hasta Luego "
                M = True
            else:
                b = raw_input("Presione enter para volver al menu")
                M = False














if __name__ == '__main__':
    main()
