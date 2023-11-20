
`Course Description: A majority of data is stored in databases and knowing the necessary tools needed to analyze and clean data directly in databases is indispensable. This course focuses on T-SQL, the version of SQL used in Microsoft SQL Server, needed for data analysis. You will learn several concepts in this course such as dealing with missing data, working with dates, and calculating summary statistics using advanced queries. After completing this course, you will have the skills needed to analyze data and provide insights quickly and easily.`

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
---
<br>

# Counts and Totals
## `COUNT` in T-SQL

```sql
SELECT COUNT(*) FROM Incidents
```

## COUNT with DISTINCT
```sql
COUNT(DISTINCT COLUMN_NAME)
```

### COUNT AGGREGATION
* `GROUP BY` can be used with `COUNT()` in the same way as the other aggregation functionssuch as `AVG()` , `MIN()` , `MAX()`
* Use the `ORDER BY` command to sort the values
    * `ASC` will return the smallest values rst (default)
    * `DESC` will return the largest values first


## SUM() in T-SQL
```SQL
-- Calculate the values subtotaled by Country
SELECT SUM(DurationSeconds) AS TotalDuration, Country
FROM Incidents
GROUP BY Country
```

# Math with Dates
### DATEPART
`DATEPART` is used to determine what part of the date you want to calculate. Some of the
common abbreviations are:
* `DD` for Day
* `MM` for Month
* `YY` for Year
* `HH` for Hour

## Date function in T-SQL (common)

* `DATEADD()` : Add or subtract datetime values
    * Always returns a date
* `DATEDIFF()` : Obtain the dierence between two datetime values
    * Always returns a number

### DATEADD()
>To Add or subtract a value to get a new date use `DATEADD()`

```sql
DATEADD (DATEPART, number, date)
```
* `DATEPART` : Unit of measurement (DD, MM etc.)
* `number` : An integer value to add
* `date` : A datetime value

*What date is 30 days from June 21, 2020?*
```sql
SELECT DATEADD(DD, 30 '2020-06-21')
```

>|(No Column Name) |
>|-----------------|
>|2020-07-21 00:00 |

---
<br>


*What date is 30 days before June 21, 2020?*
```sql
SELECT DATEADD(DD, -30 '2020-06-21')
```

>|(No Column Name) |
>|-----------------|
>|2020-05-22 00:00 |

## DATEDIFF 
Returns a date aer a number has been added or subtracted to a date
```sql
DATEDIFF (datepart, startdate, enddate)
```
* `datepart` : Unit of measurement (DD, MM etc.)
* `startdate` : The starting date value
* `enddate` : An ending datetime value
```sql
SELECT DATEDIFF(DD,'2020-05-22','2020-06-21') AS Difference1,
       DATEDIFF(DD,'2020-07-21','2020-06-21') AS difference2
```

>|Difference1 |Difference2 |
>|------------|------------|
>|30 |-30 |

## Rounding and Truncating

### Rounding
```SQL
ROUND(number, length [,function])
```

```SQL
SELECT DurationSeconds,
ROUND(DurationSeconds, 0) AS RoundToZero,
ROUND(DurationSeconds, 1) AS RoundToOne
FROM Incidents
```

>|DurationSeconds |RoundToZero |RoundToOne |
>|-|-|-|
>|121.6480 |122.0000 |121.6000 |
>|170.3976 |170.0000 |170.4000 |
>|336.0652 |336.0000 |336.1000 |

```SQL
SELECT DurationSeconds,
ROUND(DurationSeconds, -1) AS RoundToTen,
ROUND(DurationSeconds, -2) AS RoundToHundred
FROM Incidents
```

>|DurationSeconds |RoundToZero |RoundToOne |
>|-|-|-|
>|121.6480 |120.0000 |100.0000 |
>|170.3976 |170.0000 |200.0000 |
>|336.0652 |340.0000 |300.0000 |

### Truncating numbers
TRUNCATE
>17.85 → 17

ROUND
>17.85 → 18

The `ROUND()` function can be used to truncate values when you specify the third argument
```SQL
ROUND(number, length [,function])
```
* Set the third value to a non-zero numbe

```SQL
SELECT Profit,
       ROUND(DurationSeconds, 0) AS RoundingtoWhole,
       ROUND(DurationSeconds, 0, 1) AS Truncating
FROM Incidents
```

>|Profit |RoundingtoWhole |Truncating |
>|-|-|-|
>|15.6100 |16.0000 |15.0000 |
>|13.2444 |13.0000 |13.0000 |
>|17.9260 |18.0000 |17.0000 |

* Truncating just cuts all numbers o aer the specied digit

## More math functions

### Absolute value
Use ABS() to return non-negative values
```SQL
ABS(number)
```

```SQL
SELECT ABS(-2.77), ABS(3), ABS(-2)
```
>2.77 &emsp;|&emsp; 3&emsp; |&emsp; 2

### Squares and square roots in T-SQL

```sql
SELECT SQRT(9) AS Sqrt,
       SQUARE(9) AS Square
```

>|Sqrt |Square |
>|-|-|
>|3 |81 |

### Logs
* `LOG()` returns the natural logarithm
* Optionally, you can set the base, which if not set is `2.718281828`

```sql
LOG(number [,Base])
```

```sql
SELECT DurationSeconds, LOG(DurationSeconds, 10) AS LogSeconds
FROM Incidents
```

>|DurationSeconds |LogSeconds |
>|-|-|
>|37800 |4.577491799837225 |
>|5 |0.6989700043360187 |
>|20 |1.301029995663981 |


### Log of 0
You cannot take the log of 0 as it will give you an error
```sql
SELECT LOG(0, 10)

An invalid floating point operation occurred.
```