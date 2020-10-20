import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plt.rcParams['figure.figsize'] = (10,5)     #altera o tamanho do gráfico

#plotar o gráfico
#fig,ax = plt.subplots()
#ax.plot(10, 10)                   #10 contagens no eixo x e 10 no eixo y
#plt.title('Gráfico')              #título do gráfico
#plt.xlabel('Eixo x')              #alterando o nome dos eixos
#plt.ylabel('Eixo y')
#plt.show()

#-----------------------------------------------------------------------#

dados = np.array([[10, 0.01],
                  [9, 0.05],
                  [8, 0.10],
                  [7, 0.30],
                  [6, 0.70],
                  [5, 1],
                  [4, 1.5],
                  [3, 1.6],
                  [2, 1.65],
                  [1, 1.7]])


df = pd.DataFrame(dados, columns=['Tensão', 'Corrente'])
print(df)

df.plot()
plt.title('Gráfico Tensão x Corrente')
plt.xlabel('Corrente')
plt.ylabel('Tensão')
plt.legend(loc='best')                        #Coloca a legenda no melhor lugar
plt.show()



