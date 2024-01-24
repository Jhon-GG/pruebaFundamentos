vol1 = float(input("Ingrese el valor del primer voltaje:  \n"))
vol2 = float(input("Ingrese el valor del segundo voltaje:  \n"))
vol3 = float(input("Ingrese el valor del tercer voltaje:  \n"))

prom = (vol1 + vol2 + vol3) / 3

if prom < 115:
    print(f"/ Voltaje Correcto /  \nSu voltaje es de: {prom} ")
elif prom > 115 and prom < 220:
    print(f"Alto voltaje!!! \nSu voltaje es de: {prom}")
elif prom > 220:
    print(f"Peligro!!! \nSu voltaje es de: {prom}")