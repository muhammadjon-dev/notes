
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

# WHILE Loops

## Variables in T-SQL 

* Variables are needed to set values `DECLARE @variablename data_type`
    * Must start with the character @

### Variable data types in T-SQL
* `VARCHAR(n)` : variable length text eld
* `INT` : integer values from -2,147,483,647 to +2,147,483,647
* `DECIMAL(p ,s)` or `NUMERIC(p ,s)` :
    * `p` : total number of decimal digits that will be stored, both to the le and to the right of
the decimal point
    * `s` : number of decimal digits that will be stored to the right of the decimal point

### Declaring variables in T-SQL
```sql
-- Declare Snack as a VARCHAR with length 10
DECLARE @Snack VARCHAR(10)
```

### Assigning values to variables

```sql
-- Declare the variable
DECLARE @Snack VARCHAR(10)
-- Use SET a value to the variable
SET @Snack = 'Cookies'

-- OR 

-- Use SELECT assign a value
SELECT @Snack = 'Candy'
```

## WHILE Loops

### Syntax:

```sql
-- declare iter as an integer
DECLARE @iter INT

-- assign 1 to iter 
SET @iter = 1

-- condition for loop
WHILE @iter < 10 /* <- condition*/

    -- Begin the code inside the loop
    BEGIN
        -- write code
        SET @iter = @iter + 1
        -- end the loop
    END

-- let's see the value after the loop
SELECT @iter
     
```

>|(No column name) |
>|-|
>|10 |

---
<br>

* You can use `BREAK` to stop the loop or `CONTINUE` to continue the loop

```sql
DECLARE @ctr INT

SET @ctr = 1

WHILE @ctr < 10

    BEGIN
        SET @ctr = @ctr + 1

        IF @ctr = 4
        -- When ctr is equal to 4, the loop will stop
        BREAK
    -- End WHILE loop
    END
```

## Derived tables  in T-SQL

### What are Derived tables?
* Query which is treated like a temporary table
* Always contained within the main query
* They are specied in the FROM clause
* Can contain intermediate calculations to be used the main query or dierent joins than in the main query

```SQL

SELECT a.* FROM Kidney AS a
-- This derived table computes the Average age joined to the actual table
JOIN (SELECT AVG(Age) AS AverageAge
      FROM Kidney) AS b
ON a.Age = b.AverageAge

```

## CTEs in T-SQL
### CTE syntax
```SQL
-- CTE definitions start with the keyword WITH
-- Followed by the CTE names and the columns it contains
WITH CTEName (Col1, Col2)
AS
-- Define the CTE query
(
-- The two columns from the definition above
    SELECT Col1, Col2
    FROM TableName
)
```
**Example:**
```SQL
-- Create a CTE to get the Maximum BloodPressure by Age
WITH BloodPressureAge(Age, MaxBloodPressure)
AS
(SELECT Age, MAX(BloodPressure) AS MaxBloodPressure
FROM Kidney
GROUP BY Age)

-- Create a query to use the CTE as a table
SELECT a.Age, MIN(a.BloodPressure), b.MaxBloodPressure
FROM Kidney a
-- Join the CTE with the table
JOIN BloodpressureAge b
    ON a.Age = b.Age
GROUP BY a.Age, b.MaxBloodPressure
```

# WINDOW Functions in T-SQL 

## Window syntax in T-SQL
* Create the window with OVER clause
* PARTITION BY creates the frame
* If you do not include PARTITION BY the frame is the entire table
* To arrange the results, use ORDER BY
* Allows aggregations to be created at the same time as the window
```SQL
. . .
-- Create a Window data grouping
OVER (PARTITION BY SalesYear ORDER BY SalesYear)
```

### Window functions (SUM)
```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
    SUM(CurrentQuota)
    OVER (PARTITION BY SalesYear) AS YearlyTotal,
    ModifiedDate AS ModDate
FROM SaleGoal
```
>|SalesPerson |SalesYear |CurrentQuota |YearlyTotal | ModDate |
>|-|-|-|-|-
>|Bob |2011 |28000.00 |1551000.00 |2011-04-16|
>|Bob |2011 |7000.00 |1551000.00 |2011-07-17|
>|Mary |2011 |367000.00 |1551000.00 |2011-04-16|
>|Mary |2011 |556000.00 |1551000.00 |2011-07-15|
>|Bob |2012 |70000.00 |1859000.00 |2012-01-15|
>|Bob |2012 |154000.00 |1859000.00 |2012-04-16|
>|Bob |2012 |107000.00 |1859000.00 |2012-07-16|
>|. .   .   .   .|

### Window functions (COUNT)
```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
    COUNT(CurrentQuota)
    OVER (PARTITION BY SalesYear) AS QuotaPerYear,
    ModifiedDate AS ModDate
FROM SaleGoal
```
>|SalesPerson |SalesYear |CurrentQuota |QuotaPerYear | ModDate |
>|-|-|-|-|-
>|Bob |2011 |28000.00 |4 |2011-04-16|
>|Bob |2011 |7000.00 |4 |2011-07-17|
>|Mary |2011 |367000.00 |4 |2011-04-16|
>|Mary |2011 |556000.00 |4 |2011-07-15|
>|Bob |2012 |70000.00 |8 |2012-01-15|
>|Bob |2012 |154000.00 |8 |2012-04-16|
>|Bob |2012 |107000.00 |8 |2012-07-16|
>|. .   .   .   .|

## FIRST_VALUE() and LAST_VALUE()
* `FIRST_VALUE()` returns the first value in the window
* `LAST_VALUE()` returns the last value in the window

* **`Note`** that for `FIRST_VALUE` and `LAST_VALUE` the ORDER BY command is required
```SQL
-- Select the columns
SELECT SalesPerson, SalesYear, CurrentQuota,
    -- First value from every window
    FIRST_VALUE(CurrentQuota)
    OVER (PARTITION BY SalesYear ORDER BY ModifiedDate) AS StartQuota,
    -- Last value from every window
    LAST_VALUE(CurrentQuota)
    OVER (PARTITION BY SalesYear ORDER BY ModifiedDate) AS EndQuota,
    ModifiedDate as ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|StartQuota| EndQuota |ModDate |
>|-|-|-|-|-|-|
>|Bob |2011 |28000.00 |28000.00 |91000.00 |2011-04-16|
>|Bob |2011 |7000.00 |28000.00 |91000.00 |2011-07-17|
>|Bob |2011 |91000.00 |28000.00 |91000.00 |2011-10-17|
>|Bob |2012 |140000.00 |140000.00 |107000.00 |2012-01-15|
>|Bob |2012 |70000.00 |140000.00 |107000.00 |2012-04-15|

## Getting the next value with `LEAD()`
* Provides the ability to query the value from the next row
* NextQuota column is created by using `LEAD()`
* Requires the use of `ORDER BY` to order the rows

![](https://telegra.ph/file/63e00b3a77837187766c4.png)

```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
-- Create a window function to get the values from the next row
    LEAD(CurrentQuota)
    OVER (PARTITION BY SalesYear ORDER BY ModifiedDate) AS NextQuota,
    ModifiedDate AS ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|NextQuota | ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |367000.00 |2011-04-15|
>|Mary |2011 |367000.00 |556000.00 |2011-04-16|
>|Mary |2011 |556000.00 |7000.00 |2011-07-15|
>|Bob |2011 |7000.00 |NULL |2011-07-17|
>|Bob |2012 |70000.00 |502000.00 |2012-01-15|
>|Mary |2012 |502000.00 |154000.00 |2012-01-16|

## Getting the previous value with `LAG()`
* Provides the ability to query the value from the previous row
* PreviousQuota column is created by using `LAG()`
* Requires the use of `ORDER BY` to order the rows

![](https://telegra.ph/file/d2235fba6be1cc88f9e9f.png)
```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
-- Create a window function to get the values from the previous row
    LAG(CurrentQuota)
    OVER (PARTITION BY SalesYear ORDER BY ModifiedDate) AS PreviousQuota,
    ModifiedDate AS ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|PreviousQuota |ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |NULL |2011-04-15|
>|Mary |2011 |367000.00 |28000.00 |2011-04-16|
>|Mary |2011 |556000.00 |367000.00 |2011-07-15|
>|Bob |2011 |7000.00.00 |556000.00 |2011-07-17|
>|Bob |2012 |7000.00 |NULL |2012-01-15|
>|Mary |2012 |502000.00 |7000.00 |2012-01-16|
>.      .       .

## More complex WINDOW functions 
```sql
SELECT SalesPerson, SalesYear, CurrentQuota,
SUM(CurrentQuota)
OVER (PARTITION BY SalesYear) AS YearlyTotal,
ModifiedDate as ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|YearlyTotal | ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |1551000.00 |2011-04-16|
>|Bob |2011 |7000.00 |1551000.00 |2011-07-17|
>|Bob |2011 |91000.00 |1551000.00 |2011-10-17|
>|Mary |2011 |140000.00 |1551000.00 |2012-04-15|
>|Mary |2011 |70000.00 |1551000.00 |2012-07-15|
>|Mary |2011 |154000.00 |1551000.00 |2012-01-15|
>|Mary |2012 |107000.00 |1859000.00 |2012-01-16|

* `NOTE:` When we change column in or add `ORDER BY` we get new results

##### Here, we are adding ORDER BY SalesPerson, causing the values in the YearlyTotal column to change whenever the SalesPerson is modified.

```sql
SELECT SalesPerson, SalesYear, CurrentQuota,
SUM(CurrentQuota)
OVER (PARTITION BY SalesYear ORDER BY SalesPerson) AS YearlyTotal,
ModifiedDate as ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|YearTotal | ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |35000.00 |2011-04-16|
>|Bob |2011 |7000.00 |35000.00 |2011-07-17|
>|Mary |2011 |367000.00 |958000.00 |2011-10-17|
>|Mary |2011 |556000.00 |958000.00 |2012-04-15|
>|Bob |2012 |70000.00 |401000.00 |2012-07-15|
>|Bob |2012 |154000.00 |401000.00 |2012-10-16|

##### We are changing the ORDER BY column to ModifiedDate, and as a result, the values in the RunningTotal column are changing whenever the ModifiedDate (ModDate) is modified.

```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
SUM(CurrentQuota)
OVER (PARTITION BY SalesYear ORDER BY ModifiedDate) as RunningTotal,
ModifiedDate as ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|RunningTotal| ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |28000.00 |2011-04-16|
>|Mary |2011 |367000.00 |395000.00 |2011-07-17|
>|Mary |2011 |556000.00 |951000.00 |2011-10-17|
>|Bob |2011 |7000.00 |958000.00 |2012-04-15|
>|Bob |2012 |70000.00 |70000.00 |2012-01-15|
>|Mary |2012 |502000.00 |572000.00 |2012-01-16|

## Adding row numbers
* `ROW_NUMBER()` sequentially numbers the rows in the window
* `ORDER BY` is required when using `ROW_NUMBER()`

![](https://telegra.ph/file/040c29060cb7d5b7c3b54.png)

```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
    ROW_NUMBER()
    OVER (PARTITION BY SalesPerson ORDER BY SalesYear) AS QuotabySalesPerson
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|QuotabySalesPerson|
>|-|-|-|-|
>|Bob |2011 |28000.00 |1 |
>|Bob |2011 |7000.00 |2 |
>|Bob |2011 |70000.00 |3 |
>|Bob |2011 |154000.00 |4 |
>|Bob |2012 |70000.00 |5 |
>|Bob |2012 |107000.00 |6 |
>|Bob |2012 |91000.00 |7 |
>|Mary |2011 |367000.00 |1 |

## Calculating statistics using Window functions

### standard deviation `STDEV()`
```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
    STDEV(CurrentQuota)
    OVER () AS StandardDev,
    ModifiedDate AS ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|StandardDev | ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |267841.370964233 |2011-04-16|
>|Bob |2011 |7000.00 |267841.370964233 |2011-07-17|
>|Bob |2011 |91000.00 |267841.370964233 |2011-10-17|
>|Bob |2012 |140000.00 |267841.370964233 |2012-01-15|
>|Bob |2012 |70000.00 |267841.370964233 |2012-04-15|

<br>

```SQL
SELECT SalesPerson, SalesYear, CurrentQuota,
STDEV(CurrentQuota)
OVER (PARTITION BY SalesYear ORDER BY SalesYear) AS StDev,
ModifiedDate AS ModDate
FROM SaleGoal
```

>|SalesPerson |SalesYear |CurrentQuota|StDev | ModDate |
>|-|-|-|-|-|
>|Bob |2011 |28000.00 |267841.54080 |2011-04-16|
>|Bob |2011 |7000.00 |267841.54080 |2011-07-17|
>|Mary |2011 |91000.00 |267841.54080 |2011-04-16|
>|Mary |2011 |140000.00 |267841.54080 |2011-07-15|
>|Bob |2012 |70000.00 |246538.86248 |2012-01-15|
>|Bob |2012 |154000.00 |246538.86248 |2012-04-15|
>|Bob |2012 |107000.00 |246538.86248 |2012-07-16|

### calculating mode 

* Mode is the value which appears the most oen in your data
* To calculate mode:
    * Create a CTE containing an ordered count of values using ROW_NUMBER
    * Write a query using the CTE to pick the value with the highest row number

```sql
WITH QuotaCount AS (
SELECT SalesPerson, SalesYear, CurrentQuota,
    ROW_NUMBER()
    OVER (PARTITION BY CurrentQuota ORDER BY CurrentQuota) AS QuotaList
FROM SaleGoal
)
SELECT * FROM QuotaCount
```

>|SalesPerson |SalesYear |CurrentQuota|QuotaList |
>|-|-|-|-|
>|Bob |2011 |7000.00 |1 |
>|Bob |2011 |28000.00 |1 |
>|Bob |2011 |70000.00 |1 |
>|Bob |2012 |70000.00 |2 |
>|Mary |2012 |73000.00 |1 |

* Notice there are two values for `70,000.00`
<br><br>

```sql
WITH QuotaCount AS (
SELECT SalesPerson, SalesYear, CurrentQuota,
       ROW_NUMBER()
       OVER (PARTITION BY CurrentQuota ORDER BY CurrentQuota) AS QuotaList
FROM SaleGoal
)
SELECT CurrentQuota, QuotaList AS Mode
FROM QuotaCount
WHERE QuotaList IN (SELECT MAX(QuotaList) FROM QuotaCount)
```

>|CurrentQuota|Mode |
>|-|-|
>|70000.00 |2 |