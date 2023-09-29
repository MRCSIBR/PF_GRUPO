# PF_GRUPO
Proyecto_Final / Data Science

En este repositorio se pueden agregar ideas, comentarios o notebooks, relacionados
al proyecto final de Data Science / SoyHenry.

## Presentacion de propuesta

Somos una consultora de data analisis que ofrece sus servicios para ofrecer un estudio sobre el mercado de alquileres de propiedades utilizando la plataforma Airbnb. Se analizarán los datos de la ciudad de New York en la ventana de tiempo de x a y. Tambien se analiza la evolucion de los valores de las propiedades a lo largo del tiempo.
A partir de los datos extraidos de Airbnb (el cliente entrega los datos), se realizarán distintos analisis:
* Identificacion del los impactos de las crisis en el mercado inmobiliario. como afecta a cada categoria, distintos barrios, propiedades, precios.
* Basados en las tablas de Airbnb tambien, analizar en que zonas es conveniente realizar inversiones. Hay que utilizar los datos del analisis anterior e identificar cuales son inversiones que son mas robustas frente a eventos adversos de crisis. Fortalezas y debilidades de cada tipo de propiedad.

Herramientas utilizadas: para la base de datos en la nube, google cloud.

## KPIs propuestos

1. Variacion interanual % de las media de los precios de los inmuebles. Target % de inflación interanual.
2. Cantidad de propiedades vendidas. Target: que el numero esté por encima del año anterior.
3. Precio promedio alquileres. Target: Mayor al promedio de los dos años anteriores.
4. Número de reservas. Target: que sea un 50 % respecto a la cantidad de noches vendidas el año anterior.

## Metodo de trabajo

para identificar las crisis podemos usar algunos indices de la bolsa de Estados Unidos. En eso puedo aportar porque algo se, ademas hay cientos de fuentes distintas y confiables de donde sacar la info. Identificar si en estos momentos es momento de comprar o no propiedades (para esto podemos usar el dataframe que comentaba Marcos). Es importante destacar que no tenemos de los datos de Airbnb información por tiempo. No podemos estimar que departamentos fueron mas ocupados en momentos de crisis. Para eso deberiamos ver si encontramos otras fuentes de datos como el censo. Leer notas o artículos.

## Guia para crear un almacen de datos en Snowflake

https://github.com/MRCSIBR/PF_GRUPO/blob/main/CrearUnWarehouse.md

