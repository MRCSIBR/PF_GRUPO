#  Insightful Data Partners
## Proyecto_Final / Analisis de Mercado inmobiliario


<p align="center">
  <img src="Logo.png" alt="Logo" width="200">
</p>
En este repositorio se pueden agregar ideas, comentarios o notebooks, relacionados
al proyecto grupal de Data Science / SoyHenry.


## Presentacion de propuesta

Somos una consultora de data analisis que ofrece sus servicios para ofrecer un estudio sobre el estado del negocio inmobilidario en la ciudad de Nueva York. Este estudio comprende dos ramas principales:
* La variacion del precio de las propiedades (capital).
* Los precios y la demanda de alquileres.
Para el mercado de alquileres de propiedades utilizando big data de la plataforma Airbnb. Se analizarán cantidad masiva de información de la ciudad de New York en la ventana de tiempo de 2013 a 2023.

Tambien se analiza la evolución de los valores de las propiedades a lo largo del tiempo.
A partir de los datos extraidos de Airbnb (el cliente entrega los datos), se realizarán distintos analisis:
* Identificacion del los impactos de las crisis en el mercado inmobiliario. como afecta a cada categoria, distintos barrios, propiedades, precios.
* Basados en las tablas de Airbnb tambien, analizar en que zonas es conveniente realizar inversiones. Hay que utilizar los datos del analisis anterior e identificar cuales son inversiones que son mas robustas frente a eventos adversos de crisis. Fortalezas y debilidades de cada tipo de propiedad.

Herramientas utilizadas: para la base de datos en la nube, google cloud.

## KPIs propuestos

1. Variación interanual (%) de las media de los precios de los inmuebles. **Target** % de inflación interanual.
2. Cantidad de propiedades vendidas. **Target**: que el numero esté por encima del año anterior.
3. Precio promedio alquileres. **Target**: Mayor al promedio de los dos años anteriores.
4. Número de reservas. **Target**: que sea un 50 % respecto a la cantidad de reviews el año anterior.

## Metodo de trabajo

Para determinar si existe una crisis utilizaremos indices de la bolsa de Estados Unidos como VBQ (ETF real-state) y otros similares.
Para definir si es momento de comprar o no propiedades se analizarán correlaciones entre precio de pie cuadrado (square foot) y tendencias en los precios de los indices. Es importante destacar que no contamos con los datos de Airbnb de manera completa por lo tanto se realizaran estimaciones, y se complementará la informacion con datos que puedan extraerse de distintas fuentes. 


## Guia para crear un almacen de datos en Snowflake

https://github.com/MRCSIBR/PF_GRUPO/blob/main/Desarrollo/CrearUnWarehouse.md

