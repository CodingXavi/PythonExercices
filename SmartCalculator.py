while main_loop:
    mensaje()
    user_selection = str(input(" Escoja la operación que desea realizar "))

    if user_selection == "1":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        operacion_suma = num1 + num2
        print("El resultado es: {} ".format(operacion_suma))

        keep_calculating = input("¿ Desea realizar otra operación ?")

        if keep_calculating == "si":
            continue
        else:
            print("Hasta la próxima !")
            break
    if user_selection == "2":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        operacion_resta = num1 - num2
        print("El resultado es: {}".format(operacion_resta))

        keep_calculating = input("¿ Desea realizar otra operación ?")

        if keep_calculating == "si":
            continue
        else:
            print("Hasta la próxima !")
            break
    if user_selection == "3":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        operacion_division = num1 / num2
        print("El resultado es: {}".format(operacion_division))

        keep_calculating = input("¿ Desea realizar otra operación ?")

        if keep_calculating == "si":
            continue
        else:
            print("Hasta la próxima !")
            break
    if user_selection == "4":
        num1 = int(input("Primer numero: "))
        num2 = int(input("Segundo numero: "))
        operacion_mult = num1 * num2
        print("El resultado es: {}".format(operacion_mult))

        keep_calculating = input("¿ Desea realizar otra operación ?")

        if keep_calculating == "si":
            continue
        else:
            print("Hasta la próxima !")
            break
    else:
        print("Hasta la próxima")
        break
