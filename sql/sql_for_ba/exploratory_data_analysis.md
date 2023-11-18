### A few reminders

|Code |Note|
|----|-----|
|NULL| missing|
|IS NULL , IS NOT NULL| don't use = NULL|
|count(*)| number of rows|
|count(column_name)| number of non- NULL values|
|count(DISTINCT column_name)| number of different non- NULL values|
|SELECT DISTINCT column_name ... |distinct values, including NULL|

----
<br>

# Keys to the database

__`Foreign keys`__ 
* Reference another row
    * In a different table or the same table
    * Via a unique ID
        * \>> Primary key column containing unique, non-NULL values
* Values restricted to values in referenced column OR `NULL`


----
<br>

## Coalesce function
```sql
coalesce(value_1, value_2 [, ...])
```
* Operates row by row
* Returns first non- `NULL` value

<br>

**Examble 1:**
```sql 
SELECT *
FROM prices;
```
|column_1 | column_2|
|----------|----------|
|| 10|
|<br>||
|22 ||
|3 | 4|

```sql 
SELECT coalesce(column_1, column_2)
FROM prices;
```
|coalesce|
|---|
|10|
|<br>|
|22|
|3|

**Examble 2:**
```sql 
SELECT *
FROM prices
```
|column_1 | column_2|
|----------|----------|
|NULL| 10|
|NULL|NULL|
|22 |NULL|
|3 | 4|

```sql 
SELECT coalesce(column_1, column_2, 0)
FROM prices;
```
|coalesce|*explanation*|
|---|-|
|10|column_1 is `null`, returns column_2|
|0| column_1 and column_2 is `null`, returns 0|
|22|column_1 is not `null`, returns column_1|
|3|column_1 is not `null`, returns column_1|


# Column Types and Constraints

### Column constraints
* **Foreign key:** value that exists in the referenced column, or `NULL`
* **Primary key:** unique, not `NULL`
* **Unique:** values must all be different except for `NULL`
* **Not null:** `NULL` not allowed: must have a value
* **Check constraints:** conditions on the values
    * `column1 > 0`
    * `columnA > columnB`

### Data types

**Common**
* Numeric
* Character
* Date/Time
* Boolean

**Special**
* Arrays
* Monetary
* Binary
* Geometric
* Network Address
* XML
* JSON
* and more!

## Casting with `CAST()`

**Format:**
```sql
-- With the CAST function
SELECT CAST (value AS new_type);
```

**Examples:**
```sql
-- Cast 3.7 as an integer
SELECT CAST (3.7 AS integer);
```

>4
---
<br>

```sql
-- Cast a column called total as an integer
SELECT CAST (total AS integer)
FROM prices;
```

### Casting with `::`

**Format:**
```sql
-- With :: notation
SELECT value::new_type;
```

**Examples:**
```sql
-- Cast 3.7 as an integer
SELECT 3.7::integer;
```

>4
---
<br>

```sql
-- Cast a column called total as an integer
SELECT total::integer
FROM prices;
```

---
<br>
<br>

# Numeric Data Types and Summary Functions

**Numeric types: integer**

|Name| Storage Size| Description| Range|
|-|-|-|-|
|`integer` or `int` or `int4`| 4 bytes | typical choice |-2147483648 to +2147483647|
|smallint or int2|2 bytes| small-range| -32768 to +32767|
|`bigint` or `int8`| 8 bytes |large-range|-9223372036854775808 to+9223372036854775807|
|`serial`| 4 bytes| auto-increment| 1 to 2147483647|
|`smallserial`| 2 bytes| small autoincrement|1 to 32767|
|`bigserial`| 8 bytes| large auto-increment| 1 to 9223372036854775807|

**Numeric types: decimal**
|Name| Storage Size| Description| Range|
|-|-|-|-|
|`decimal` or `numeric`| variable| user-specified precision, exact |up to 131072 digits before the decimal point; up to 16383 digits after the decimal point|
|`real`| 4 bytes| variableprecision, inexact| 6 decimal digits precision|
|`double precision`| 8 bytes | variableprecision, inexact |15 decimal digits precision


### Division

```sql
-- integer division
SELECT 10/4;
```

>2
---
<br>

```sql
-- numeric division
SELECT 10/4.0;
```

>2.500000000
---
<br>

### Range: min and max

```sql
SELECT min(question_pct)
FROM stackoverflow;
```

> |&emsp;min|
>|----|
> &emsp;0
> (1 row)
---
<br>

```sql
SELECT max(question_pct)
FROM stackoverflow;
```

> |&emsp;max|
>|----|
> 0.071957428
> (1 row)
---
<br>

### Average or mean

```sql
SELECT avg(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;&emsp;&emsp;avg|
>|-|
> 0.00379494620059319
> (1 row)
---
<br>

## Variance
**Population Variance**
```sql
SELECT var_pop(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;&emsp;&emsp;var_pop|
>|-|
> 0.000140268640974167
> (1 row)

<br>

**Sample Variance**

```sql
SELECT var_samp(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;&emsp;&emsp;var_samp|
>|-|
> 0.000140271571051059
> (1 row)

---
<br>

```sql
SELECT variance(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;&emsp;&emsp;variance|
>|-|
> 0.000140271571051059
> (1 row)
---
<br>

## Standard deviation
**Sample Standard Deviation**
```sql
SELECT stddev_samp(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;stddev_samp|
>|-|
> 0.0118436299778007
> (1 row)

----
<br>

```sql
SELECT stddev(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;stddev|
>|-|
> 0.0118436299778007
> (1 row)

<br>

**Population Standard Deviation**

```sql
SELECT stddev_pop(question_pct)
FROM stackoverflow;
```

> |&emsp;&emsp;stddev_pop|
>|-|
> 0.0118435062787237
> (1 row)
---
<br>

## Round 
```sql
SELECT round(42.1256, 2);
```
>42.13

## Truncate
```sql
SELECT trunc(42.1256, 2);
```
>42.12
```sql
SELECT trunc(12345, -3);
```
>12000

<br>

## Truncating and grouping
```sql
SELECT trunc(unanswered_count,-1) AS trunc_ua,
    count(*)
FROM stackoverflow
WHERE tag='amazon-ebs'
GROUP BY trunc_ua -- column alias
ORDER BY trunc_ua; -- column alias
```
|trunc_ua | count|
|---------|-------|
30 | 74
40 | 194
50 | 480
(3 rows)

---
<br>

## Generate series
```sql
SELECT generate_series(start, end, step);
```

**Example**
```sql
SELECT generate_series(1, 10, 2);
```
>|generate_series|
>|-----------------|
>1
>3
>5
>7
>9
>(5 rows)

<br>

```sql
SELECT generate_series(0, 1, .1);
```
>|generate_series|
>|-----------------|
>0
>0.1
>0.2
>0.3
>0.4
>0.5
>0.6
>0.7
>0.8
>0.9
>1.0
>(11 rows)

### Create bins: output

```sql
-- Create bins
WITH bins AS (
SELECT generate_series(30,60,5) AS lower,
generate_series(35,65,5) AS upper),
-- Subset data to tag of interest
ebs AS (
SELECT unanswered_count
FROM stackoverflow
WHERE tag='amazon-ebs')
-- Count values in each bin
SELECT lower, upper, count(unanswered_count)
-- left join keeps all bins
FROM bins
LEFT JOIN ebs
ON unanswered_count >= lower
AND unanswered_count < upper
-- Group by bin bounds to create the groups
GROUP BY lower, upper
ORDER BY lower;
```
|lower | upper | count|
|------|-------|-------|
30 | 35 | 0
35 | 40 | 74
40 | 45 | 155
45 | 50 | 39
50 | 55 | 445
55 | 60 | 35
60 | 65 | 0
(7 rows)

<br>

## Correlation function

```sql
SELECT corr(assets, equity)
FROM fortune500;
```
>|corr|
>|-|
>|0.637710143588615|
>|(1 row)|

<br>

![](https://www.simplypsychology.org/wp-content/uploads/correlation.jpg)
---
<br>

## Percentile functions
```sql
SELECT percentile_disc(percentile) WITHIN GROUP (ORDER BY column_name)
FROM table;
-- percentile between 0 and 1
```
* Returns a value from column

```sql
SELECT percentile_cont(percentile) WITHIN GROUP (ORDER BY column_name)
FROM table;
```
* Interpolates between values

**Examples**
```sql
SELECT val
FROM nums;
-- val = (1,3,4,5)
```

```sql
SELECT percentile_disc(.5) WITHIN GROUP (ORDER BY val),
        percentile_cont(.5) WITHIN GROUP (ORDER BY val)
FROM nums;
```

|percentile_disc | percentile_cont|
|-----|-----------|
3 | 3.5

### Common issues
* Error codes
    * Examples: 9, 99, -99
* Missing value codes
    * NA, NaN, N/A, #N/A
    * 0 = missing or 0?
* Outlier (extreme) values
    * Really high or low?
    * Negative values?
* Not really a number
    * Examples: zip codes, survey response categories

---
<br>

# Creating Temporary Tables
### Syntax
Create Temp Table Syntax

```sql
-- Create table as
CREATE TEMP TABLE new_tablename AS
-- Query results to store in the table
SELECT column1, column2
FROM table;
```
Select Into Syntax
```sql
-- Select existing columns
SELECT column1, column2
-- Clause to direct results to a new temp table
INTO TEMP TABLE new_tablename
-- Existing table with exisitng columns
FROM table;
```

**Example**

```sql
CREATE TEMP TABLE top_companies AS
SELECT rank, title
FROM fortune500
WHERE rank <= 3;
```

```sql
SELECT *
FROM top_companies;
```

>|rank | title|
>|------|-|
>1 | Walmart
>2 | Berkshire Hathaway
>3 | Apple

<br>

## Insert into table
```sql
INSERT INTO top_companies
SELECT rank, title
FROM fortune500
WHERE rank BETWEEN 9 AND 11;
```

```sql
SELECT *
FROM top_companies;
```

>|rank | title|
>|------|-|
>1 | Walmart
>2 | Berkshire Hathaway
>3 | Apple
>9 | AT&T
>10 | Ford Motor
>11| AmerisourceBergen

<br>

## Delete (drop) table
```sql
DROP TABLE top_companies;
```
```sql
DROP TABLE IF EXISTS top_companies;
```


