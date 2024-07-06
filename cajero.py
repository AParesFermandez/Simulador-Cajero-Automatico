usuarios = [{"numeroDeCuenta": i + 1, "saldo": 10000} for i in range(10)]

def obtener_usuario(numeroDeCuenta):
    if 1 <= numeroDeCuenta <= len(usuarios):
        return usuarios[numeroDeCuenta - 1]
    else:
        return None

def menu():
    print("Seleccione una opción:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Transferir a otra cuenta")
    print("5. Salir")

while True:
    numeroDeCuenta = int(input("Por favor introduzca su numero de cuenta: "))
    usuario = obtener_usuario(numeroDeCuenta)

    if usuario is None:
        print("No existe usuario con ese numero de cuenta.")
        continue

    menu()
    opcion = input("Ingrese su opcion: ")

    if opcion == '1':
        print(f"Tu saldo es: {usuario['saldo']}")

    elif opcion == '2':
        retiro = int(input("Cuánto dinero deseas retirar: "))
        if retiro > usuario['saldo']:
            print("El monto excede el saldo de su cuenta")
        else:
            usuario['saldo'] -= retiro
            print(f"Su retiro de {retiro} ha sido exitoso")
            print(f"Su saldo actual es: {usuario['saldo']}")

    elif opcion == '3':
        deposito = int(input("Cuánto dinero deseas depositar: "))
        if deposito > 0:
            usuario['saldo'] += deposito
            print("Depósito exitoso")
            print(f"Su saldo actual es: {usuario['saldo']}")
        else:
            print("El depósito debe ser mayor a 0")

    elif opcion == '4':
        transferencia = int(input("Cuánto dinero desea transferir: "))
        if transferencia > 0:
            cuenta_destino = int(input("¿A qué cuenta desea transferir?: "))
            usuario_destino = obtener_usuario(cuenta_destino)

            if usuario_destino is None:
                print("No existe usuario con ese número de cuenta.")
            elif transferencia > usuario['saldo']:
                print("El monto excede el saldo de su cuenta")
            else:
                usuario['saldo'] -= transferencia
                usuario_destino['saldo'] += transferencia
                print(f"Transferencia de {transferencia} a la cuenta {cuenta_destino} exitosa")
                print(f"Su saldo actual es: {usuario['saldo']}")
        else:
            print("La transferencia debe ser mayor a 0")

    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
