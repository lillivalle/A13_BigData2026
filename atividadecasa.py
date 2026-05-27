#Relatório de vendas da nova filial. Dados na planilha vendas_roupas.xls
# Qntd de peças vend, média prod, prod com maior faturamento, menor faturamento, prod com nivel de satisfação baixo, 
# prod com nível de satisfação baixo, prod com nível de sats mt alto, prod com faturamento acima da média

import pandas as pd
#pip install openpyxl
#openpyxl -> biblioteca para abrir o excel

#pip install pandas
#pandas -> biblioteca pra fazer análise de dados

df_vendasroupas = pd.read_excel('vendas_roupas.xlsx')
print(df_vendasroupas.head()) 

#Quantidade de peças vendidas e Média dos preços dos produtos
print(f'\nQuantidade de peças total: {df_vendasroupas['Unidades Vendidas'].sum()}') #  indicar dentro da [] o que tu vai medir
print(f'\nMédia de preços dos produtos: {df_vendasroupas['Preço por Unidade (R$)'].mean()}') # 

#Total de vendas
print(f'\nTotal de Faturamento (R$): {df_vendasroupas['Faturamento Total (R$)'].sum()}')

#Produto com maior Faturamento
maiorvenda = df_vendasroupas['Faturamento Total (R$)'].max()
print(f'\nMaior valor de Faturamento: {df_vendasroupas['Faturamento Total (R$)'].max()}')
print(df_vendasroupas[df_vendasroupas['Faturamento Total (R$)'] == maiorvenda][['Produto','Faturamento Total (R$)']]) #uma chave é o que eu quero a outra é a lista

#Produto com menor Faturamento
menorvenda = df_vendasroupas['Faturamento Total (R$)'].min()
print(f'\nMenor valor de Faturamento: {df_vendasroupas['Faturamento Total (R$)'].min()}')
print(df_vendasroupas[df_vendasroupas['Faturamento Total (R$)'] == menorvenda][['Produto','Faturamento Total (R$)']])

#Média de Valor de Faturamento
mediavenda = df_vendasroupas['Faturamento Total (R$)'].mean()
print(f'\nMédia valor de Faturamento: {df_vendasroupas['Faturamento Total (R$)'].mean()}')

#Satisfação baixa
print(f'\nProdutos com Satisfação Baixa: ') 
print(df_vendasroupas[df_vendasroupas['Satisfação'] == 'BAIXO'][['Produto', 'Satisfação']]) # '' baixa texto literal

#Satisfação muito alta
print(f'\nProdutos com Satisfação Muito Alta: ') 
print(df_vendasroupas[df_vendasroupas['Satisfação'] == 'MUITO ALTO'][['Produto', 'Satisfação']]) # '' baixa texto literal

#Produtos faturamento acima da média
print(f'\nProdutos com valor acima da Média:')
print(df_vendasroupas[df_vendasroupas['Faturamento Total (R$)'] > mediavenda][['Produto', 'Faturamento Total (R$)']])

