"""
This dataset consists of six files with Airbnb rental listings of six cities: Barcelona, Málaga, Madrid, Sevilla, Valencia, and Mallorca. \
Each row represents a listing with details such as coordinates, neighborhood, host id, price per night, number of reviews, and so on.
- What is the distribution of prices across a city's neighborhoods? How does it change when you segment it further by room_type?
- Create a map with a dot for each listing in a city and add a color scale based on price on the dots.
- How do listings that require a minimum stay of a week or longer differ from those that don't?
"""
import pandas as pd
import folium
import matplotlib.pyplot as plt

def price_group(dict_df,x):
    g=dict_df[x].groupby(['neighbourhood','room_type','price'])['price'].count()
    print(f'{x}: \n {g} \n')

def drawMap(df,x,coord):
    myMap = folium.Map(location=coord[x], zoom_start=12)
    for i in range(0,len(df[x])):
        if df[x].iloc[i]["price"] <= df[x]["price"].mean():
            folium.Marker(location=[df[x].iloc[i]["latitude"],df[x].iloc[i]["longitude"]], popup=df[x].iloc[i]["id"],icon=folium.Icon(icon='home',color='green')).add_to(myMap)
        else:
            folium.Marker(location=[df[x].iloc[i]["latitude"],df[x].iloc[i]["longitude"]], popup=df[x].iloc[i]["id"],icon=folium.Icon(icon='home',color='red')).add_to(myMap)      
    myMap.show_in_browser()

def impr_graph(df,i):
    x=df[i]['minimum_nights'].tolist()
    y=df[i]['number_of_reviews'].tolist()
    plt.bar(x,y)
    plt.title(f'Nº reviews per minimum of nights')
    plt.xlabel('Minium of nights')
    plt.ylabel('Number of reviews total')
    plt.show()

#Las muestras se han tomado de los primeros 100 Airbnbn listados. 
bcn = pd.read_csv('CSV_airbnb/listings_barcelona.csv').head(100) #Barcelona
agp = pd.read_csv('CSV_airbnb/listings_malaga.csv').head(100) #Málaga
mad = pd.read_csv('CSV_airbnb/listings_madrid.csv').head(100) #Madrid
svq = pd.read_csv('CSV_airbnb/listings_sevilla.csv').head(100) #Sevilla
vlc = pd.read_csv('CSV_airbnb/listings_valencia.csv').head(100) #Valencia
pmi = pd.read_csv('CSV_airbnb/listings_mallorca.csv').head(100) #Mallorca

#Diccionario con los DataFrames de cada ciudad
dictDF={'Barcelona': bcn, 'Málaga': agp, 'Madrid': mad, 'Sevilla': svq, 'Valencia': vlc, 'Mallorca': pmi}
#Diccionario con las coordenadas de cada ciudad
coord={'Barcelona': [41.3828939,2.1774322], 'Málaga': [36.7213028,-4.4216366], 'Madrid': [40.4167047,-3.7035825], 'Sevilla': [37.3886303,-5.9953403], 'Valencia': [39.4697065,-0.3763353], 'Mallorca': [39.613432,2.8829184529439633]}

print(f'Ciudades disponibles:')
for x in dictDF:
    print(x, end=" | ")
print('\n')
n=input(f'Introduce el nombre de la ciudad: ')
price_group(dictDF,n) #Imprime los precios de los Airbnb según el tipo de habitación y el barrio en el que se sitúan
drawMap(dictDF,n,coord) #Crea un mapa de la ciudad ubicando los Airbnb. Verde si el precio está por debajo del precio medio de la zona, rojo si está por encima.

impr_graph(dictDF,n) #Diagrama de barras que muestra el número de reviews de los Airbnb en función del número mínimo de noches necesario para alquilarlo.
                     #Las tendencias indican que tienen muchas mas reviews los alquileres que requieren menos días. Podemos aproximar, nºreviews = nºusuarios.


#Devuelve la info de un Airbnb conocido el id de la vivienda en el mapa mostrado
num=int(input('Introduce el id: '))
ind=dictDF[n].loc[dictDF[n]["id"]==num].index
info=dictDF[n].loc[ind]
print(info)

