import random  # Librería para generar números y elecciones aleatorias

while True:  # Mantiene el menú repitiéndose
    print("\n--- MENU ---")
    print("1. Jugar Adivina el número 🎮🔮")
    print("2. Jugar Adivina el código 🔐")
    print("3. Jugar Ahorcado 🪢")
    print("4. Jugar Revoltijo de palabras🔀")
    print("5. Salir ↩️")

    opcion = input("Elige una opción: ")

    # ---------------- JUEGO 1 ----------------
    if opcion == "1":

        numero_secreto = random.randint(1, 100)
        intentos = 6

        print("Adivina el número entre 1 y 100")
        print("Tienes 6 intentos")

        for i in range(intentos):

            numero = int(input("Ingrese un número: "))

            if numero < numero_secreto:
                print("El número es mayor")

            elif numero > numero_secreto:
                print("El número es menor")

            else:
                print("¡Ganaste! Acertaste el número")
                break

        else:
            print("Perdiste. El número era:", numero_secreto)

        print("Volviendo al menú...")

    # ---------------- JUEGO 2 ----------------
    elif opcion == "2":

        codigo = []

        # Genera el código secreto de 4 números
        for i in range(4):
            codigo.append(str(random.randint(0, 9)))

        progreso = ["_", "_", "_", "_"]  # Lo que el usuario va descubriendo
        intentos = 7

        print("Adivina el código de 4 números")

        for i in range(intentos):

            print("Código:", " ".join(progreso))
            intento = input("Ingresa 4 números: ")

            # Revisa cada posición del código
            for j in range(4):
                if intento[j] == codigo[j]:
                    progreso[j] = intento[j]

            # Si ya descubrió todo el código
            if progreso == codigo:
                print("¡Ganaste! El código era:", "".join(codigo))
                break

        else:
            print("Perdiste. El código era:", "".join(codigo))

        print("Volviendo al menú...")

    # ---------------- JUEGO 3 ----------------
    elif opcion == "3":

        palabras = ["casa", "computadora", "avion", "teclado", "carro"]

        # Escoge una palabra aleatoria
        palabra_seleccionada = random.choice(palabras).upper()

        errores = 0
        vidas = 6
        usadas = []  # Letras usadas
        respuesta = []  # Progreso de la palabra

        # Crea los guiones bajos
        for i in palabra_seleccionada:
            respuesta.append("_")

        # Dibujos del ahorcado según errores
        Ahorcado = {
            0: " ___\n |     |\n |\n |\n |\n |\n",
            1: " ___\n |     |\n |     O\n |\n |\n |\n",
            2: " ___\n |     |\n |     O\n |     |\n |\n |\n",
            3: " ___\n |     |\n |     O\n |    /|\n |\n |\n",
            4: " ___\n |     |\n |     O\n |    /|\n |    /\n |\n",
            5: " ___\n |     |\n |     O\n |    /|\n |    / \\\n |\n",
            6: " ___\n |     |\n |     O\n |    /|\n |    / \\\n |\n"
        }

        print("Adivine la palabra")

        while errores < vidas and "_" in respuesta:

            print(Ahorcado[errores])
            print("Palabra:", " ".join(respuesta))

            letra = input("Ingrese una letra: ").upper()

            if letra in usadas:
                print("Ya usó esa letra")
                continue

            usadas.append(letra)

            if letra in palabra_seleccionada:

                # Recorre la palabra para descubrir letras
                for i in range(len(palabra_seleccionada)):
                    if palabra_seleccionada[i] == letra:
                        respuesta[i] = letra
            else:
                errores += 1

        if "_" not in respuesta:
            print("¡Ganaste! La palabra era:", palabra_seleccionada)
        else:
            print("Perdiste. La palabra era:", palabra_seleccionada)

        print("Volviendo al menú...")

    # ---------------- JUEGO 4 ----------------
    elif opcion == "4":

        palabras = ["casa", "computadora", "avion", "teclado", "carro"]

        # Escoge una palabra al azar
        palabra_seleccionada = random.choice(palabras).upper()

        # Convierte la palabra en lista de letras
        lista_letras = list(palabra_seleccionada)

        # Mezcla las letras aleatoriamente
        random.shuffle(lista_letras)

        # Une las letras mezcladas para mostrar la palabra revuelta
        palabra_nueva = "".join(lista_letras)

        print("Adivina la palabra:")
        print(palabra_nueva)

        intentos = 3

        # El usuario tiene 3 intentos
        while intentos > 0:

            respuesta = input("Escribe tu respuesta: ").upper()

            if respuesta == palabra_seleccionada:
                print("¡Haz ganado! Adivinaste la palabra")
                break
            else:
                intentos -= 1
                print("Incorrecto. Intentos restantes:", intentos)

        # Si se queda sin intentos
        if intentos == 0:
            print("Perdiste. La palabra era:", palabra_seleccionada)

    # ---------------- SALIR ----------------
    elif opcion == "5":
        print("Adiós Gamer 👨‍💻")
        break

    else:
        print("Opción inválida")