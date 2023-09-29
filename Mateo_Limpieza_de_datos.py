import pandas as pd
import os
from archivos_barrios import barrios_nueva_york

calendar = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/calendar.csv")
listing  = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/listings.csv")
listing_detailed  = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/listings_detailed.csv")
neighnourhoods = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/neighbourhoods.csv")
review = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/reviews.csv")
reviews_detailed = pd.read_csv("archivos/Housing Market + Real State/usa/New York City/reviews_detailed.csv")
ventas = pd.read_csv("archivos/Housing Market + Real State/datos venta/realtor-data.csv")


lista_venta = ventas[(ventas["state"] == "New York") & (ventas["city"] == "New York City")]
lista = listing.groupby(["neighbourhood_group", "neighbourhood"]).agg(
    count_neighbourhood_group=pd.NamedAgg(column='neighbourhood_group', aggfunc='count'),
    counts_reviews=pd.NamedAgg(column='number_of_reviews', aggfunc='sum'),
    mean_price=pd.NamedAgg(column='price', aggfunc='mean'),
    mean_nights=pd.NamedAgg(column="minimum_nights", aggfunc="mean"),
    room_type_list=pd.NamedAgg(column='room_type', aggfunc=lambda x: list(x.unique())),
    id_list=pd.NamedAgg(column='id', aggfunc=lambda x: list(x.unique()))
)
lista['mean_nights'] = lista['mean_nights'].round(0)
lista["gente_por_año"] = lista["counts_reviews"]/10
lista["gente_por_mes"] = lista["gente_por_año"]/12
lista = lista.reset_index()


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


def asignar_todos_codigos_postales(row):
    codigo_postal_por_grupo = []
    for borough, neighborhoods in barrios_nueva_york.items():
        if row["neighbourhood_group"] == borough:
            for zip_codes in neighborhoods.values():
                codigo_postal_por_grupo.extend(zip_codes)
    return ", ".join(codigo_postal_por_grupo)
lista["Codigo_Postal"] = lista.apply(asignar_todos_codigos_postales, axis=1)


