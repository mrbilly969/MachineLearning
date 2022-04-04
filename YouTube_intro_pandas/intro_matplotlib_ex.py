import matplotlib.pyplot as plt
import matplotlib.colors

##Grafico de linea
a = [1,2,3,4]
b = [11,22,33,44]

plt.plot(a,b, color='green', linewidth=1, label='línea de prueba')
plt.legend()
plt.show()

##Gráfico de lineas
#Definir los datos
x1= [3,4,5,6]
y1= [5,6,3,4]
x2= [2,5,8]
y2=[3,4,3]

#Configurar las características del gráfico
plt.plot(x1,y1, label= 'Esta es la línea 1', linewidth = 3, color = 'red')
plt.plot(x2,y2, label= 'Esta es la línea 2', linewidth = 3, color = 'yellow')

#Definir título y nombre de los ejes
plt.title('Diagrama de lineas :D')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Mostrar leyenda, cuadrícula y figura
plt.legend()
plt.grid()
plt.show()

##Gráfico de barras
#Definir los datos
x_a = [0.25,1.25, 2.25, 3.25, 4.25]
y_a= [10, 55,80,32, 40]
x_b= [0.75,1.75,2.75,3.75,4.75]
y_b= [42, 26, 10, 29, 66]

#Configurar las características del gráfico
plt.bar(x_a, y_a, label = 'Datos 1', width = 0.5, color ='darkblue')
plt.bar(x_b, y_b, label = 'Datos 2', width = 0.5, color ='orange')

#Definir título y nombres de ejes
plt.title('Gráfico de barras :D')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Definir leyenda y figura
plt.legend()
plt.grid()
plt.show()

#Gráfico de dispersión,
#Definir los datos, estos se tomaron de la definición anterior de grafico de barras
#x_a = [0.25,1.25, 2.25, 3.25, 4.25]
#y_a= [10, 55,80,32, 40]
#x_b= [0.75,1.75,2.75,3.75,4.75]
#y_b= [42, 26, 10, 29, 66]

#Configurar las características del gráfico
plt.scatter(x_a, y_a, label = 'Datos 1', color ='red')
plt.scatter(x_b, y_b, label = 'Datos 2', color ='purple')

#Definir título y nombres de ejes
plt.title('Gráfico de dispersión :D')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

#Definir leyenda y figura
plt.legend()
plt.grid()
plt.show()

##Gráfico circular
#Definir los datos
dormir = [7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar = [7,8,7,2,2]
recreacion = [8,5,7,8,13]
divisiones = [7,2,2,13]
actividades = ['Dormir','Comer','Trabajar','Recreación']
colores = ['tomato','blueviolet', 'brown', 'royalblue']

#Configurar las características del gráfico
plt.pie(divisiones, labels=actividades, colors=colores, startangle=90,
    shadow= True, explode= (0.2,0.3,0.4,0), autopct='%1.1f%%')

#Definir título
plt.title('Gráfico circular')
#Definir figura
plt.show()
