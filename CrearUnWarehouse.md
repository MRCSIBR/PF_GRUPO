To start a new data warehouse in Snowflake, you can follow these general steps:

1. **Create a Snowflake account**: If you don't already have a Snowflake account, you'll need to create one. You can do this by going to the Snowflake website and signing up for a free trial or contacting Snowflake sales to purchase a subscription[5].

2. **Create a warehouse**: Once you have a Snowflake account, you can create a new warehouse by using the CREATE WAREHOUSE command in SQL. This command allows you to specify various parameters for the warehouse, such as the size of the warehouse and the number of clusters it should have[1]. Alternatively, you can use the WORKSHEET feature in Snowflake to create a warehouse using a script[5].

3. **Create a database**: After creating a warehouse, you'll need to create a database to store your data. You can do this using the CREATE DATABASE command in SQL[4].

4. **Create a schema**: Within your database, you can create one or more schemas to organize your tables and views. You can use the CREATE SCHEMA command in SQL to create a new schema[4].

5. **Load data**: Once you have a schema, you can start loading data into your tables. You can do this using various methods, such as using the Snowflake web interface to upload CSV files or using Snowflake's COPY command to load data from an S3 bucket[4].

6. **Run queries**: With data loaded into your tables, you can start running queries to analyze and manipulate your data. You can use SQL to write queries in the Snowflake web interface or using a SQL client[4].

Overall, starting a new data warehouse in Snowflake involves creating a warehouse, database, and schema, and then loading data and running queries. The specific steps you take will depend on your use case and data requirements.

Citations:
[1] https://docs.snowflake.com/en/sql-reference/sql/create-warehouse
[2] https://youtube.com/watch?v=W4qL4eIM_Pw
[3] https://www.blendo.co/documents/setup-snowflake-data-warehouse/
[4] https://www.snowflake.com/trending/data-warehousing-tutorials
[5] https://blog.openbridge.com/snowflake-create-warehouse-876b0855a536
[6] https://www.kdnuggets.com/2022/02/data-warehousing-snowflake-beginners.html