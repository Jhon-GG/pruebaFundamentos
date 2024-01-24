vol1 = float(input("Ingrese el valor del primer voltaje:  \n"))
vol2 = float(input("Ingrese el valor del segundo voltaje:  \n"))
vol3 = float(input("Ingrese el valor del tercer voltaje:  \n"))
vol4 = float(input("Ingrese el valor del cuarto voltaje:  \n"))
vol5 = float(input("Ingrese el valor del cuarto voltaje:  \n"))


prom = (vol1 + vol2 + vol3 + vol4 + vol5) / 5

if prom > 220:
    print("Alto Voltaje!!")
else:
    print("/ Voltaje Correcto /")