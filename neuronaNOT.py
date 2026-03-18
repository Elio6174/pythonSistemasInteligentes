def neuronaNOT(x):
    w=-1
    umbral=-1
    #suma ponderada
    fx=x*w
    #aplicamos la funcion de activacion
    if fx>umbral:
        return 1
    else:
        return 0

def neuronaAND(x1, x2):
    w1,w2=1,1
    umbral=1
    #suma ponderada
    fx=x1*w1+x2*w2
    #aplicamos la funcion de activacion
    if fx>umbral:
        return 1
    else:
        return 0

def neuronaOR(x1, x2):
    w1,w2=1,1
    umbral=0
    #suma ponderada
    fx=x1*w1+x2*w2
    #aplicamos la funcion de activacion
    if fx>umbral:
        return 1
    else:
        return 0


salida = neuronaNOT(int(input("Ingresa la entrada para x=")))
print("Salida=", salida)

print("Neurona AND")
x1=int(input("Ingresa el valor para x1="))
x2=int(input("Ingresa el valor para x2="))
salida=neuronaAND(x1, x2)
print("Salida:", salida)


print("Neurona OR")
x1=int(input("Ingresa el valor para x1="))
x2=int(input("Ingresa el valor para x2="))
salida=neuronaOR(x1, x2)
print("Salida:", salida)
