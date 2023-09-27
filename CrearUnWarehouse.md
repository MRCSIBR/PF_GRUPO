## Para comenzar un nuevo data warehouse en Snowflake, se pueden seguir los siguientes pasos: 

1. **Crear una cuenta en Snowflake**: Si aún no tienes una cuenta en Snowflake, necesitarás crear una. Puedes hacerlo yendo al sitio web de Snowflake y registrándote para una prueba gratuita o contactando a ventas de Snowflake para adquirir una suscripción[5].

2. **Crear un almacén (warehouse)**: Una vez que tengas una cuenta en Snowflake, puedes crear un nuevo almacén utilizando el comando `CREATE WAREHOUSE <nombre>` en SQL. Este comando te permite especificar varios parámetros para el almacén, como el tamaño del almacén y la cantidad de clústeres que debe tener[1]. Alternativamente, puedes usar la función WORKSHEET en Snowflake para crear un almacén utilizando un script[5].

3. **Crear una base de datos**: Después de crear un almacén, necesitarás crear una base de datos para almacenar tus datos. Puedes hacerlo utilizando el comando `CREATE DATABASE <nombre>` en SQL[4].

4. **Crear un esquema (schema)**: Dentro de tu base de datos, puedes crear uno o más esquemas para organizar tus tablas y vistas. Puedes utilizar el comando `CREATE SCHEMA` en SQL para crear un nuevo esquema[4].

5. **Cargar datos**: Una vez que tengas un esquema, puedes comenzar a cargar datos en tus tablas. Puedes hacerlo utilizando diversos métodos, como usar la interfaz web de Snowflake para cargar archivos CSV o utilizar el comando COPY de Snowflake para cargar datos desde un depósito S3[4].

6. **Ejecutar consultas**: Con los datos cargados en tus tablas, puedes comenzar a ejecutar consultas para analizar y manipular tus datos. Puedes utilizar SQL para escribir consultas en la interfaz web de Snowflake o mediante un cliente SQL[4].

En resumen, comenzar un nuevo almacén de datos en Snowflake implica crear un almacén, una base de datos y un esquema, y luego cargar datos y ejecutar consultas. 
Los pasos específicos que tomes dependerán de tu caso de uso y requisitos de datos.


EJEMPLO: Luego de crear nuestro worksheet podemos escribir comandos

```SQL
/* Crear Almacen de consultoria */
CREATE WAREHOUSE consultoria WITH WAREHOUSE_SIZE='SMALL';


CREATE DATABASE housemarket;

/* Documentacion : https://docs.snowflake.com/en/sql-reference/sql/create-schema */
CREATE SCHEMA zillow;


CREATE TABLE zillow.HOUSEPRICE (
  regionid INT,
  address VARCHAR,
  price DECIMAL(10,2),
  bedrooms INT,
  bathrooms INT,
  sqft INT
);
```
Referencias:
[1] https://docs.snowflake.com/en/sql-reference/sql/create-warehouse
[2] https://youtube.com/watch?v=W4qL4eIM_Pw
[3] https://www.blendo.co/documents/setup-snowflake-data-warehouse/
[4] https://www.snowflake.com/trending/data-warehousing-tutorials
[5] https://blog.openbridge.com/snowflake-create-warehouse-876b0855a536
[6] https://www.kdnuggets.com/2022/02/data-warehousing-snowflake-beginners.html
