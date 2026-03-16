from PIL import Image

img = Image.open('resultadoEsperado.png')
pixeles = img.load()

tamanio = img.size[0]*img.size[1]
print("el tamanio de la imagen es de: ", tamanio)


cont = 0
for i in range(0, img.size[0]):
    for j in range(0, img.size[1]):
        color = pixeles[i, j]
        cont+= color[0]
        cont+= color[1]
        cont+= color[2]

print("Calculo total de euristica:", cont)