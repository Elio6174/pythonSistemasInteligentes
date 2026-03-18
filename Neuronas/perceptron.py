import random
#algoritmo de red neuronal OR
def perceptron(patrones, w, umbral):
    while(True):
        bandera = True
        for patron in patrones:
            #Calcular FX
            fx=patron[0]*w[0]+patron[1]*w[1]+umbral

            #Calcular la funcion de activacion (y)
            if fx>0:
                y = 1
            else:
                y -=1
            #Evaluar si y!=d(x) y realizar ajustes
            if y!=patron[2]:
                #ajustamos pesos y umbral
                w[0]=w[0]+patron[2]*patron[0]
                w[1]=w[1]+patron[2]*patron[1]
                umbral=umbral + patron[2]
        if bandera == True:
            break
    return w,umbral


#Fase de entrenamiendo
#1.-Patrones de entrada compuerta OR
patrones=[[-1,-1,-1],[1,-1,1],[-1,1,1],[1,1,1]]
umbral=random.uniform(-1,1)
w=[]
w.append(random.uniform(-1,1))
w.append(random.uniform(-1,1))
w,umbral=perceptron(patrones,w,umbral)  

#Fase de evaluacion/prediccion
x1=int(input("Ingresa el valor para x1="))
x2=int(input("Ingresa el valor para x2="))
prediccion=x1*w[0]+x2*w[1]+umbral

if prediccion>0:
    print("Verdadero")
else:
    print("False")