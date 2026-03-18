import random

def perceptron(patrones, w, umbral):
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

#Fase de entrenamiendo
#1.-Patrones de entrada compuerta OR
patrones=[[-1,-1,-1],[1,-1,1],[-1,1,1],[1,1,1]]
umbral=random.uniform(-1,1)
w=[]
w.append(random.uniform(-1,1))
w.append(random.uniform(-1,1))
w,umbral=perceptron(patrones,w,umbral)