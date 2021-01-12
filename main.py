# Import the necessary packages and modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

'''

Casos de Covid em pato branco - PR (n[i] - n[i-1]) = novos casos, desconsiderando n[0] - ...
30 -  nov = 2018
1-  dez =  2123
2 - dez =  2164
3 - dez =  2234
4 - dez =  2282
5 - dez =  2407
6 - dez =  2417
7 - dez =  2443
8 - dez =  2561
9 - dez =  2622 
10 - dez = 2654
11 - dez = 2704 
12 - dez = 2720
13 - dez = 2749 
14 - dez = 2779
15 - dez = 2863 
16 - dez = 2889
17 - dez = 2915 
18 - dez = 2960
19 - dez = 3002 
20 - dez = 3021
21 - dez = 3047
22 - dez = 3067
23 - dez = 3086
24 - dez = 3103
25 - dez = 3136
26 - dez = 3140
27 - dez = 3155
28 - dez = 3160
29 - dez = 3205
5 - jan =  3338

lista
[0, 2018, 2123, 2164, 2234, 2282, 2407, 2417, 2443, 2561, 2622, 2654, 2704, 2720, 2749, 2779, 2863, 2889, 2915, 2960, 3002, 3021, 3047, 3067, 3086, 3103, 3136, 3140, 3155,3160, 3205, 3338]


'''

# exemplo de como incluir label no retângulo do gráfico 
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# lista do total de casos, iniciando em 30 de novembro de 2020
x = [2018, 2123, 2164, 2234, 2282, 2407, 2417, 2443, 2561, 2622, 2654, 2704, 2720, 2749, 2779, 2863, 2889, 2915, 2960, 3002, 3021, 3047, 3067, 3086, 3103, 3136, 3140, 3155,3160, 3205, 3338]

# inicializacao da lista de objetos que serao submetidos ao teste
laws = []
laws.append({
    # indice (1, 2, 3, 4, 5, 6, 7, 8, 9), count: quantas vezes aparecem na populacao, law -> percentual benford do indice em questao, perc: percentual do indice na populacao
    'index': 0, 'ct': 0, 'law': 0.0, 'message': '', 'perc': 0.0
})

# inicializa lista com seus indices e os percentuais de referencia
for i in range(1, 10):
    d = float(i)
    l = math.log10(1 + (1/d))
    print ("k______________________________b(k)")
    print (str(d) + '----------------------' + str(l))
    laws.append({
    'index': i, 'ct': 0, 'law': l, 'message': '', 'perc': 0.0
})

# realiza a contagem dos dados na populacao
nant = 0
totalOccurs = 0
for n in x:
    if nant == 0:
        nant = n
        print ('descartado o primeiro numero ' + str(n))
        continue
    nr = n - nant
    ndx = int(str(nr)[0])
    laws[ndx]['ct'] += 1
    totalOccurs += 1
    nant = n
    print (nr)

labels = []    
lawBars = []
realbars = []
x = np.arange(len(laws)-1)

width = 0.50 

for o in laws:

    if o['index'] == 0:
        continue
    o['perc'] = ((o['ct']*100)/totalOccurs)*0.01

    labels.append(str(o['index']))
    lawBars.append(round(o['law']*100,2) )
    realbars.append(round(o['perc']*100, 2))

matplotlib.use('Agg') # sem UI


fig = plt.figure()

ax = fig.add_subplot(111)

print (lawBars)
print(realbars)

rects1 = ax.bar(x - width/2, lawBars, width, label='Benford')
rects2 = ax.bar(x + width/2, realbars, width, label='Ocorrências')


# --- retirado de um exemplo da matplotlib --- Adicao de títulos e lavels na imagem
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('benford %')
ax.set_title('Covid PB casos Dezembro/5 JAN')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# --- retirado de um exemplo da matplotlib --- como colocar labels em cada retângulo
autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.savefig("benford.png")

print (laws)


