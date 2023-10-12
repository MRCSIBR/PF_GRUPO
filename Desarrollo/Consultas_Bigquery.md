## Consultas BIGQUERY

Las siguientes consultas estan en cloud.google > Bigquery > Espacio trabajo SQL

```SQL

-- Mostrar fecha mas antigua y mas nueva en la tabla

SELECT MIN(Date) AS Oldest_Date
FROM `insightfuldata.market.FactorMacro`;

SELECT MAX(Date) AS Newest_Date
FROM `insightfuldata.market.FactorMacro`

```

```SQL
-- Comprobar que la tasa de hipoteca es mayor cuando aumenta la tasa de desempleo

SELECT Date, Unemployment_Rate, Mortgage_Rate
FROM `insightfuldata.market.FactorMacro`
WHERE Date >= '1977-01-01' AND Date <= '2021-01-01'
ORDER BY Date ASC
```

```SQL
-- Desempleo desde 1977 hasta 2020

SELECT Date, Unemployment_Rate FROM `insightfuldata.market.FactorMacro`
WHERE Date >= '1977-01-01' AND Date <= '2021-01-01'
ORDER By Date ASC
```

```SQL
--- Datos de Vanguard VMBS 
SELECT date, Open 
FROM `insightfuldata.market.Mortgage` 
WHERE date BETWEEN '2014-03-01' AND '2023-09-30'
ORDER BY date;

```


```SQL
-- VNQ + VMBS

SELECT date, Open
FROM `insightfuldata.market.Mortgage`
WHERE date BETWEEN '2014-03-01' AND '2023-09-30'
UNION ALL
SELECT date, Open
FROM `insightfuldata.market.VNQ`
WHERE date BETWEEN '2014-03-01' AND '2023-09-30'
ORDER BY date;
```

```SQL
-- Total casas vendidas desde 2017 a 2022

SELECT EXTRACT(YEAR FROM period_begin) AS Year, SUM(total_homes_sold) AS Total_Houses_Sold
FROM `insightfuldata.weekly_house_market.most_recent`
GROUP BY Year
ORDER BY Year;
```
