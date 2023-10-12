import pandas as pd
import numpy as np
import os

allhomes = pd.read_csv("archivos/Housing Market + Real State/datos venta/Copy of Zillow House Price Data/City_Zhvi_AllHomes.csv")
allhomesNy = allhomes[allhomes["RegionName"] == "New York"]
allhomesrenta = pd.read_csv("archivos/Housing Market + Real State/datos venta/Copy of Zillow House Price Data/City_MedianRentalPrice_AllHomes.csv")
allhomesrentany = allhomesrenta[allhomes["RegionName"] == "New York"]
salesprice = pd.read_csv("archivos/Housing Market + Real State/datos venta/Copy of Zillow House Price Data/Sale_Prices_City.csv")
salespriceNY = salesprice[salesprice["RegionName"] == "New York"]
calendar = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/calendar.csv")
calendar["date"] = pd.to_datetime(calendar["date"], format="%Y-%m-%d")
listing  = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/listings.csv")
listing_detailed  = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/listings_detailed.csv")
neighnourhoods = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/neighbourhoods.csv")
review = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/reviews.csv")
review["date"] = pd.to_datetime(review["date"], format="%Y-%m-%d")
reviews_detailed = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/reviews_detailed.csv")
ventas = pd.read_csv("archivos/Housing Market + Real State/datos venta/realtor-data.csv")

review["Año"] = review["date"].dt.year
rev = review.groupby(["listing_id","Año"]).agg(
    count_rev=pd.NamedAgg(column='date', aggfunc='count'))
rev.reset_index(inplace = True)

calendar["Año"] = calendar["date"].dt.year
calendar["ocupado"] = np.where(calendar["available"] == "f",1,0 )
cal = calendar.groupby(["listing_id","Año"]).agg(
    count_cal=pd.NamedAgg(column='ocupado', aggfunc='sum'))
cal.reset_index(inplace = True)

# Unir listing_detailed con cal por la columna "id"
cal_2023 = cal[cal["Año"] == 2023]
cal_2023.rename(columns={'count_cal':"count_cal_2023"}, inplace=True)
cal_2024 = cal[cal["Año"] == 2024]
cal_2024.rename(columns={'count_cal':"count_cal_2024"}, inplace=True)
listing_cal = listing_detailed.merge(cal_2023, left_on='id', right_on='listing_id', how='left')
listing_cal = listing_cal.merge(cal_2024, left_on='id', right_on='listing_id', how='left')

rev_2022 = rev[rev["Año"] == 2022]
listing_combined = listing_cal.merge(rev_2022, left_on='id', right_on='listing_id', how='left')

# Eliminar columnas duplicadas y renombrar según sea necesario
listing_combined.drop(['listing_id_x', 'Año_x', 'listing_id_y', 'Año_y'], axis=1, inplace=True)
listing_combined.rename(columns={'count_rev_x': 'count_cal', 'count_rev_y': 'count_rev'}, inplace=True)



lista = listing_combined.groupby(["neighbourhood_group_cleansed", "neighbourhood_cleansed"]).agg(
    count_neighbourhood_group=pd.NamedAgg(column='neighbourhood_group_cleansed', aggfunc='count'),
    sum_reviews=pd.NamedAgg(column='number_of_reviews', aggfunc='sum'),
    mean_nights=pd.NamedAgg(column="minimum_nights", aggfunc="mean"),
    id_list=pd.NamedAgg(column='id', aggfunc=lambda x: list(x.unique())),
    promedio_dias_disponibles = pd.NamedAgg("availability_365", aggfunc="mean"),
    promedio_dias_alquilados_2023 = pd.NamedAgg("count_cal_2023", aggfunc = "mean"),
    promedio_dias_alquiler_2024 = pd.NamedAgg("count_cal_2024", aggfunc = "mean"),
    promedio_cantidad_reservas_2022 = pd.NamedAgg("count_rev", aggfunc = "mean")
)
precio_medio = listing.groupby(["neighbourhood_group", "neighbourhood"]).agg(
    mean_price=pd.NamedAgg(column='price', aggfunc='mean'),
)
lista["Precio Medio"] = precio_medio
lista["Precio Medio"] = lista["Precio Medio"].round(0)
lista['mean_nights'] = lista['mean_nights'].round(0)
lista["alquileres_maximos_por_lugar"] = (lista["promedio_dias_disponibles"] / lista['mean_nights']).round(0)
lista["ganacia_anual_promedio"] = lista["alquileres_maximos_por_lugar"]*lista['mean_nights']*lista["Precio Medio"]
lista = lista.reset_index()
for i in range(len(lista)):
    if lista["promedio_cantidad_reservas_2022"][i] > lista["alquileres_maximos_por_lugar"][i]:
        lista["promedio_cantidad_reservas_2022"][i] = lista["promedio_cantidad_reservas_2022"][i]/ lista["alquileres_maximos_por_lugar"][i]
lista["promedio_dias_2022"] = lista['mean_nights'] * lista["promedio_cantidad_reservas_2022"]
for i in range(len(lista)):
    if lista["promedio_dias_2022"][i] > lista["promedio_dias_disponibles"][i]:
        lista["promedio_dias_2022"][i] = lista["promedio_dias_2022"][i]/ lista["alquileres_maximos_por_lugar"][i]


lista_promedios = []
for i in range(len(lista)):
    ids = lista["id_list"][i]
    promedios = []
    for num in ids:
        prom = listing_detailed.loc[listing_detailed["id"] == num, "review_scores_location"].iloc[0]
        if not pd.isna(prom):
            promedios.append(prom)
    try:
        lista_promedios.append((sum(promedios)/len(promedios)).round(2))
    except:
        lista_promedios.append(0)
lista["scores_location"] = lista_promedios

lista.drop("id_list",axis = 1,inplace = True)
lista = lista.round(0)

lista["Acronimo"] = "NYC" 

columnas_originales = lista.columns.tolist()
columnas_originales.insert(0, "Acronimo")
columnas_originales = columnas_originales[:-1]
lista = lista[columnas_originales]

if not os.path.exists("gcp/New_York"):
    os.makedirs("gcp/New_York")
    print("La carpeta gcp/New_York se ha creado exitosamente.")
else:
    print("La carpeta gcp/New_York ya existe.")

lista.to_csv("gcp/New_York/New_York_City_KPI34.csv",index = False)
