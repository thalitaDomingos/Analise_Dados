import pandas as pd
import matplotlib.pyplot as plt


# Importando o csv
paises = pd.read_csv('paises.csv', delimiter=';')


# País, Região, População e Área dos países da América Latina e Caribe
americaLatinaCaribe = paises[paises['Region'].str.contains('LATIN AMER. & CARIB')]
pais = americaLatinaCaribe['Country']
regiao = americaLatinaCaribe['Region']
populacao = americaLatinaCaribe['Population']
area = americaLatinaCaribe['Area (sq. mi.)']


print(f'Nome dos Paises: \n{pais}\n')
print(f'Regiao (repectivamente): \n{regiao}\n')
print(f'Populacao (repectivamente): \n{populacao}\n')
print(f'Area (repectivamente): \n{area}\n')


# Contando e mostrando as diferentes Regiões do planeta segundo este dataset
regioesPlaneta = paises['Region'].unique()
print(f'O planeta possui {regioesPlaneta.size} regioes diferentes, sendo elas:')
for i in regioesPlaneta:
    print(f'-{i}')



# Taxa de alfabetização do planeta - Metodo 1
alfabetizacao = paises['Literacy (%)'].mean()
print(f'\nA taxa de media de alfabetizacao e de {alfabetizacao:.2f}%')


# Taxa de alfabetização do planeta - Metodo 2
literacy = paises.iloc[:,9]   # pega todas as linhas da coluna 9
worldLiteracy = pd.Series(literacy)
print(f"A taxa média de alfabetização do planeta é de {worldLiteracy.mean():.4f}%.")


# Gráfico em barras mostrando a renda per capita (GDP) de dois países da América do Norte:
# o que possui a maior e o que possui a menor população

americaNorte = paises.loc[paises['Region'].str.contains('NORTHERN AMERICA')]
infoAmericaNorte = americaNorte.loc[:,['Country','Population','GDP ($ per capita)']]
print(" ")
print(infoAmericaNorte)

maiorPopulacao = americaNorte['Population'].max()
menorPopulacao = americaNorte['Population'].min()

print(f'\nMaior populacao: {maiorPopulacao}')
print(f'Menor populacao: {menorPopulacao}\n')

country_low = infoAmericaNorte['Country'].values[3]
gpd_low = infoAmericaNorte['GDP ($ per capita)'].values[3]

country_high = infoAmericaNorte['Country'].values[4]
gpd_high = infoAmericaNorte['GDP ($ per capita)'].values[4]


plt.title(" Renda per Capita - Países da Norte America ")
plt.xlabel('Países')
plt.ylabel('Renda  per  capita  (GDP)')
plt.bar(country_low, gpd_low, color="Blue")
plt.bar(country_high, gpd_high, color="Green")
plt.show()

