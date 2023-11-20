```py
# Course Description
# A majority of data is stored in databases and knowing the necessary tools needed to analyze and clean data directly in databases is indispensable. This course focuses on T-SQL, the version of SQL used in Microsoft SQL Server, needed for data analysis. You will learn several concepts in this course such as dealing with missing data, working with dates, and calculating summary statistics using advanced queries. After completing this course, you will have the skills needed to analyze data and provide insights quickly and easily.
```

## Detecting missing values
* When you have no data, the empty database eld contains the word `NULL`
* Because `NULL` is not a number, it is not possible to use `=`, `<` , or `>` to nd or compare missing values
* To determine if a column contains a `NULL` value, use `IS NULL` and `IS NOT NULL`

### Blank is not NULL
* A blank is not the same as a NULL value
* May show up in columns containing text
* An empty string `''` can be used to nd blank values
* The best way is to look for a column where the Length or LEN > 0

```sql
SELECT Country, GDP, Year
FROM EconomicIndicators
WHERE LEN(GDP) > 0
```

### `ISNULL()`


```sql
SELECT GDP, Country,
ISNULL(Country, 'Unknown') AS NewCountry
FROM EconomicIndicators
```

>|GDP |Country |NewCountry |
>|-----|---|-|
>|5867920022 |NULL |Unknown |
>|597873038497 |South Africa |South Africa |
>|1474091271101 |NULL |Unknown |


```sql
/*Substituting values from one column for another with ISNULL*/
SELECT TradeGDPPercent, ImportGoodPercent,
ISNULL(TradeGDPPercent, ImportGoodPercent) AS NewPercent
FROM EconomicIndicators
```

>|TradeGDPPercent |ImportGoodPercent |NewPercent |
>|-------------------|-----------------|----------------|
>|NULL |56.7 |56.7 |
>|52.18720739 |51.75273421 |52.18720739 |
>|NULL |NULL |NULL |

>NOTE. `ISNULL()` takes exactly two arguments and returns the second argument if the first one is NULL.

### `COALESCE()`
`COALESCE` returns the rst non-missing value
```sql
COALESCE( value_1, value_2, value_3, ... value_n )
```
* If `value_1` is `NULL` and `value_2` is not `NULL` , return `value_2`
* If `value_1` and `value_2` are `NULL` and `value_3` is not `NULL` , return `value_3`
* ...

## CASE
```sql
CASE
    WHEN Boolean_expression THEN result_expression [ ...n ]
    [ ELSE else_result_expression ]
END
```

```sql
SELECT Continent,
CASE WHEN Continent = 'Europe' or Continent = 'Asia' THEN 'Eurasia'
     ELSE 'Other'
     END AS NewContinent
FROM EconomicIndicators
```

>|Continent |NewContinent |
>|----------|------------|
>|Europe |Eurasia |
>|Asia |Eurasia |
>|Americas |Other |

