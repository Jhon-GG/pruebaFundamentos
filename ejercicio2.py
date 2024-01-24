base = float(input("Ingrese el valor de la base del triángulo:  \n"))
altura = float(input("Ingrese el valor de la altura del triángulo: \n"))

calc = (base * altura) / 2

if calc > 1000:
    print("Datos no válidos!!!")
else:
    print(f"El area de tu triangulo es: \t {calc}")