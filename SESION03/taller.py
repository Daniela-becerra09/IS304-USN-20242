'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''


from datetime import datetime
# Definición de la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, saldoCta=0):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = datetime.now().strftime('%Y-%m-%d')
        self.__ultimoRetiro = None
        self.__ultimaConsignacion = None

    # Métodos getter para acceder a los atributos
    def get_numeroCta(self):
        return self.__numeroCta
    
    def get_nombreCliente(self):
        return self.__nombreCliente
    
    def get_saldoCta(self):
        return self.__saldoCta
    
    def get_fechaApertura(self):
        return self.__fechaApertura
    
    def get_ultimoRetiro(self):
        return self.__ultimoRetiro
    
    def get_ultimaConsignacion(self):
        return self.__ultimaConsignacion

    # Método para consignar dinero
    def consignar(self, monto):
        if monto > 0:
            self.__saldoCta += monto
            self.__ultimaConsignacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Consignación de {monto} € realizada. Nuevo saldo: {self.__saldoCta} €")
        else:
            print("El monto a consignar debe ser positivo.")
    
    # Método para retirar dinero
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldoCta:
            self.__saldoCta -= monto
            self.__ultimoRetiro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Retiro de {monto} € realizado. Nuevo saldo: {self.__saldoCta} €")
        else:
            print("Fondos insuficientes o monto no válido.")
    
    # Método para transferir dinero a otra cuenta
    def transferir(self, monto, otra_cuenta):
        if monto > 0 and monto <= self.__saldoCta:
            self.retirar(monto)
            otra_cuenta.consignar(monto)
            print(f"Transferencia de {monto} € realizada con éxito a la cuenta {otra_cuenta.get_numeroCta()}.")
        else:
            print("Fondos insuficientes o monto no válido.")

    # Método para mostrar la información de la cuenta
    def mostrar_informacion(self):
        print(f"\nInformación de la cuenta {self.__numeroCta}")
        print(f"Cliente: {self.__nombreCliente}")
        print(f"Saldo: {self.__saldoCta} €")
        print(f"Fecha de apertura: {self.__fechaApertura}")
        print(f"Último retiro: {self.__ultimoRetiro}")
        print(f"Última consignación: {self.__ultimaConsignacion}\n")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Abrir cuenta")
    print("2. Consignar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Consultar información de la cuenta")
    print("6. Salir")
    return input("Seleccione una opción: ")

# Función principal del programa
def main():
    cuentas = {}  # Diccionario para almacenar las cuentas
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            numeroCta = input("Ingrese el número de cuenta: ")
            nombreCliente = input("Ingrese el nombre del cliente: ")
            saldoInicial = float(input("Ingrese el saldo inicial: "))
            cuentas[numeroCta] = CuentaBancaria(numeroCta, nombreCliente, saldoInicial)
            print(f"Cuenta {numeroCta} creada con éxito.")
        
        elif opcion == '2':
            numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Ingrese el monto a consignar: "))
                cuentas[numeroCta].consignar(monto)
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '3':
            numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                monto = float(input("Ingrese el monto a retirar: "))
                cuentas[numeroCta].retirar(monto)
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '4':
            numeroCta_origen = input("Ingrese el número de cuenta origen: ")
            numeroCta_destino = input("Ingrese el número de cuenta destino: ")
            if numeroCta_origen in cuentas and numeroCta_destino in cuentas:
                monto = float(input("Ingrese el monto a transferir: "))
                cuentas[numeroCta_origen].transferir(monto, cuentas[numeroCta_destino])
            else:
                print("Una o ambas cuentas no fueron encontradas.")
        
        elif opcion == '5':
            numeroCta = input("Ingrese el número de cuenta: ")
            if numeroCta in cuentas:
                cuentas[numeroCta].mostrar_informacion()
            else:
                print("Cuenta no encontrada.")
        
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
