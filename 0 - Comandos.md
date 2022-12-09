>Nome das colunas
df.columns

>Transformar a coluna em numerica
df2['ESTOQUE'] = pd.to_numeric(df2['ESTOQUE'], errors='coerce')
>Com replace
df2['SELLOUT'] = df2['SELLOUT'].apply(lambda x: float(x.split()[0].replace(',', '.')))

>Verificar schema das colunas
print(df2.dtypes)

>Verificar uma tabela com dados baseados em outra
df2 = df1[df1['BANDEIRA'].isin(rede_semanal)]

>Exportar df para o Excel
df_projecao_m1.to_excel('proj_m1.xlsx')