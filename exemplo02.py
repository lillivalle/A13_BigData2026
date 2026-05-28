#Análise de custos de produtos, valor de compra, imposto, frete taxa operacional
#
import pandas as pd
import numpy as np
#pip install numpy
#numpy é para cálculos 

df_planilhas_custos = pd.read_csv('planilha_de_custos.csv')
print(df_planilhas_custos.head(10)) #quero que mostre só 10 linhas

#Totalizar a coluna de custo somando tudo
df_planilhas_custos['Custo Total (R$)'] = ( # se deixar o mesmo nome (df_planilhas_custos) vai ser substituído
    df_planilhas_custos['Preco de Compra (R$)'] + 
    (df_planilhas_custos['Preco de Compra (R$)'] * df_planilhas_custos['Imposto (%)'] / 100) +
    df_planilhas_custos['Frete (R$)'] +
    df_planilhas_custos['Taxa Operacional (R$)']    
# 50 + (50 * 13 / 100) + 50 + 50 -> é como se fosse isso
)

#print(df_planilhas_custos)
print('\nColunas: Produto e Total')
print(50*'-')
print(df_planilhas_custos[['Produto', 'Custo Total (R$)']].head())

#Médias de Tendência Central
#estrutura array é de ganho computacional
array_custo_total = np.array(df_planilhas_custos['Custo Total (R$)'])
# print(array_custo_total)

# Média 
media = np.mean(array_custo_total)

# Mediana
mediana = np.median(array_custo_total) #ordena os números crescente e pega o do meio

print('\nMédias de Tendência Central')
print(50*'-')
print(f'Média: {media:.2f}')
print(f'Mediana:{mediana:.2f}')


# Medidas de Posição
# Calculando o Quartil
#  Quartil está dentro do conceito de Quantil
q1 = np.quantile(array_custo_total, 0.25 ) #array é ganho computacional
q2 = np.quantile(array_custo_total, 0.50 )
q3 = np.quantile(array_custo_total, 0.75 )

print('\nMédias de Posição (Quartil)')
print(50*'-')
print(f'Quartil 1: {q1:.2f}')
print(f'Quartil 2: {q2:.2f}')
print(f'Quartil 3: {q3:.2f}')

# Filtro de dataframe
print('\nMenores: ')
#df_menores = df_planilhas_custos[df_planilhas_custos['Custo Total (R$)'] < q1]
print(df_planilhas_custos[df_planilhas_custos['Custo Total (R$)'] < q1])

print(100*'-')

#q2 = Mediana

print('\nMaiores: ') 
print(df_planilhas_custos[df_planilhas_custos['Custo Total (R$)'] > q3])

