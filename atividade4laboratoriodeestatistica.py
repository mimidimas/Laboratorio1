#atividade4LaboratorioDeEstatistica.ipynb

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from google.colab import drive
#drive.mount('/content/drive')

dados = pd.read_csv('/content/drive/MyDrive/Arquivos/AtividadeEstatistica/atividade4/heart.csv',
                      sep=',', encoding='UTF-8')
print(dados)

def is_numeric(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def is_string(value):

    if pd.isna(value):
        return False
    if isinstance(value, str):
        try:
            float(value)
            return False
        except ValueError:
            return True
    else:
        return False

dados1 = dados.drop(dados[~dados['Sex'].apply(is_string)].index)
print(dados1)

dados1 = dados.drop(dados[~dados['Cholesterol'].apply(is_numeric)].index)
print(dados1)

dados1 = dados1.drop(dados1[~dados1['Age'].apply(is_numeric)].index)
print(dados1)

# 1)Determine a média, a moda, a mediana, o desvio padrão e a variância da variável idade.

dados1['Age'] = dados1['Age'].astype(int)

media = dados1['Age'].mean()
print(media)

moda = dados1['Age'].mode() #moda
print(moda)

mediana = dados1['Age'].median() #mediana
print(mediana)

variaca =dados1['Age'].var()  # Variância amostral
print(variaca)

desvioPadrao = dados1['Age'].std() # Desvio padrão amostral
print(desvioPadrao)

# 2)	(valor 1,0) Construa um histograma para a variável idade.

# histograma
plt.hist(dados1['Age'], bins=7, color='black', edgecolor='pink')
dados1['Age'].hist(bins=7, color='black', edgecolor='pink')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Histograma da idade')
plt.show()

# 3)Para a variável idade, a média é uma medida que representa a centralidade dos dados? Justifique.

#Sim, a média soma todos os números dividindo pela quantidade, os dados são resumidos e centrado em um unico número.

# 4)Determine a quantidade de pessoas do sexo feminino e do sexo masculino em porcentagem. Faça um gráfico com essa representação.


contagem_cores = dados1['Sex'].value_counts()
print(contagem_cores)
# Criando o gráfico de pizza
plt.pie(contagem_cores, labels=contagem_cores.index, autopct='%1.1f%%')
plt.title('porcentagem Homem e Mulher')
plt.show()

# 5)	(valor 1,0) Determine os valores máximo, mínimo e os quartis para a variável colesterol. Construa um gráfico Boxplot. Essa variável possui valores missing? Se sim, qual a sua ação com relação a isso?

# Mínimo
minimo = dados1['Cholesterol'].min()
print(minimo)

# Máximo
maximo = dados1['Cholesterol'].max()
print(maximo)

# Primeiro Quartil
pQuartil = dados1['Cholesterol'].quantile(q=0.25)
print(pQuartil)

# Segundo Quartil (Mediana)
sQuartil = dados1['Cholesterol'].quantile(q=0.5)
print(sQuartil)

# Terceiro Quartil
tQuartil = dados1['Cholesterol'].quantile(q=0.75)
print(tQuartil)

plt.boxplot(dados1['Cholesterol'])
plt.show()

#Sim, ela possuia valores missing. Eu fiz uma verificação se estava vazio e apaguei as linhas.

## 6) A variável colesterol possui outliers? Se sim, estes valores outliers são coerentes com a realidade? Qual a sua sugestão para lidar com estes outliers (manter, excluir, alterar...)?

#Sim, a variavel colesterol possui alguns outliners, pessoas que estão com o colesterol muito alto ou muito baixo. A melhor opção seria apagar esses dados, se estão muito fora do padrão, não são coerentes

## 7)Qual a média, a moda e a mediana da variável colesterol?


media = dados1['Cholesterol'].mean() #média
print(media)
moda = dados1['Cholesterol'].mode() #moda
print(moda)
mediana = dados1['Cholesterol'].median() #mediana
print(mediana)

# 8)	(valor 1,0) Qual a probabilidade de sortear ao acaso uma pessoa do sexo masculino com idade inferior a 35 anos?

# CRIANDO FUNÇÃO PROBABILIDADE
def probab (A, E): # espaço amostral e eventos
  resultado = (A / E)*100
  print('{:.2f}'.format(resultado))

homem = dados1[(dados1['Sex'] == 'M') & (dados1['Age'] < 35)]
probab (len(homem), len(dados1))

# 9)	(valor 0,5) Qual a probabilidade de sortear ao acaso uma pessoa do sexo feminino dado que essa pessoa possui idade inferior a 35 anos, isto é, com a condição da idade ser inferior a 35 anos?

#Pessoas com idade menor que 35
menor_35 = dados1[dados1['Age'] < 35]
print(menor_35)

# Pessoas do sexo feminino e idade menor que 35
fem_menor_35 = menor_35[menor_35['Sex'] == 'F']
print(fem_menor_35)

# Calcula a probabilidade condicional
prob_condicional = len(fem_menor_35) / len(menor_35) * 100
print(f'Probabilidade condicional: {prob_condicional:.2f}%')

# 10)Em 20 sorteios, qual a probabilidade de saírem até 8 pessoas com doença cardíaca?

from scipy.stats import binom

n = 20
k = 8
p = dados1['HeartDisease'].mean()

prob = binom.cdf(k, n, p) * 100  # em porcentagem
print(f'Probabilidade de até 8 com doença em 20 sorteios: {prob:.2f}%')

# 11)A variável Chest Pain Type (tipo de dor no peito) possui as seguintes classes:"""

valores_unicos = dados1['ChestPainType'].unique()

print(valores_unicos)