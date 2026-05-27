import pandas as pd
#pip install openpyxl

df_vendasroupas = pd.read_excel('vendas_roupas.xlsx')
print(df_vendasroupas.head()) 

#Quantidade de peças vendidas e Média dos preços dos produtos
print(f'\nQuantidade de peças total: {df_vendasroupas['Unidades Vendidas'].sum()}') #  indicar dentro da [] o que tu vai medir
print(f'\nMédia de preços dos produtos: {df_vendasroupas['Preço por Unidade (R$)'].mean()}') # 

#Total de vendas
print(f'\nTotal de Faturamento: {df_vendasroupas['Faturamento Total (R$)'].sum()}')