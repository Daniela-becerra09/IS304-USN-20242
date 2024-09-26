# Pedimos al usuario que introduzca un número
numero = int(input("Introduce un número: "))

# Verificamos si el número es múltiplo de 3, 5 o ambos
if numero % 3 == 0 and numero % 5 == 0:
    print("fizzbuzz")
elif numero % 3 == 0:
    print("fizz")
elif numero % 5 == 0:
    print("buzz")
else:
    print(numero)



    cuando el nuemro no es divisible por ningun numero,automaticamente nos dara el mismo numero que colocamos en este caso, 7 no es divisible de ninguno de los nuemros que se menseiona anterior mente, 
    asi que nos dara el mismo numero en este caso 7.
