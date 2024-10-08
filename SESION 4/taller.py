 class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depositado: {monto}. Saldo actual: {self.saldo}")
        else:
            print("Monto debe ser positivo")
    
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retirado: {monto}. Saldo actual: {self.saldo}")
        else:
            print("Monto inválido o saldo insuficiente")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, saldo_inicial, tasa_interes):
        super().__init__(saldo_inicial)
        self.tasa_interes = tasa_interes
    
    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes / 100
        self.depositar(interes)

class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo_inicial, sobregiro):
        super().__init__(saldo_inicial)
        self.sobregiro = sobregiro
    
    def retirar(self, monto):
        if 0 < monto <= (self.saldo + self.sobregiro):
            self.saldo -= monto
            print(f"Retirado: {monto}. Saldo actual: {self.saldo}")
        else:
            print("Monto inválido o límite de sobregiro alcanzado")

class CuentaPadre:
    def __init__(self, cuenta_principal):
        self.cuenta_principal = cuenta_principal
        self.subcuentas = []
    
    def agregar_subcuenta(self, subcuenta):
        self.subcuentas.append(subcuenta)
    
    def mostrar_saldo_total(self):
        saldo_total = self.cuenta_principal.saldo
        for subcuenta in self.subcuentas:
            saldo_total += subcuenta.saldo
        print(f"Saldo total (principal + subcuentas): {saldo_total}")


cuenta_principal = CuentaCorriente(300, 500) 
cuenta_ahorros = CuentaAhorros(560, 2.5)    
cuenta_corriente = CuentaCorriente(500, 800) 

cuenta_padre = CuentaPadre(cuenta_principal)
cuenta_padre.agregar_subcuenta(cuenta_ahorros)
cuenta_padre.agregar_subcuenta(cuenta_corriente)

cuenta_padre.mostrar_saldo_total() 

cuenta_ahorros.aplicar_interes() 
cuenta_padre.mostrar_saldo_total() 


