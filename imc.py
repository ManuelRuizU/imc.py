
# Actividad 1 - IMC Manuel Ruiz
# Se declaran las variables Peso, Altura
# Solicitar al usuario que ingrese el peso en Kg y la altura en centímetros

peso = float(input("Ingrese su peso en Kg: "))

# Validar que el peso no sea 0 o negativo
if peso <= 0:
    print("El peso no puede ser cero o negativo. Por favor, ingrese un valor válido.")
    peso = float(input("Ingrese su peso en Kg: "))

altura = float(input("Ingrese su altura en centímetros: "))

# Validar que la altura no sea 0 o negativa
if altura <= 0:
    print("La altura no puede ser cero o negativa. Por favor, ingrese un valor válido.")
    altura = float(input("Ingrese su altura en centímetros: "))

# Convertir la altura a metros
altura = altura / 100

# Formula del IMC
imc = peso / (altura ** 2)

# Mostrar el IMC calculado 
print(f"Su IMC es: {imc:.2f}")

# Nivel de sobre Peso
if imc < 18.5:
    print("Tiene bajo peso")
elif 18.5 <= imc < 25:
    print("Tiene un peso adecuado")
elif 25 <= imc < 30:
    print("Tiene sobrepeso")
elif 30 <= imc < 35:
    print("Tiene obesidad grado I")
elif 35 <= imc < 40:
    print("Tiene obesidad grado II")
else:
    print("Tiene obesidad grado III")



