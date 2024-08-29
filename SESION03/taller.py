'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
class cuentaBancaria:
    def __init__(self,numeroCta,nombreClente,saldoCta, fechaApertura, ultimoRetiro=None,ultimaConsignacion=None):
       set(numeroCta, nombreClente,saldoCta, fechaApertura, ultimoRetiro=None,ultimaConsignacion=None)
       
       def set(self,numeroCta,nombreClente,saldoCta, fechaApertura, ultimoRetiro=None,ultimaConsignacion=None):
        self._numeroCta= numeroCta
        self._nombreClente=nombreClente
        self._saldoCta=saldoCta
        self._fechaApertura=fechaApertura
        self._ultimoRetiro=ultimoRetiro
        self._ultimaConsignacion=_ultimaConsignacion
        
    def retirar(self,cantidad,fecha):
            
           
