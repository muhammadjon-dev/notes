# STRINGS IN SQL 
```sql
SELECT
description,
LEN(description) AS description_length
FROM grid;
```
`NOTE:` In PostgreSQL `LENGTH (description)`
>description | description_length |
>|---------|--------------------|
>| Severe Weather Thunderstorms | 29 |
>| Severe Weather Thunderstorms | 29 |
>| Severe Weather Thunderstorms | 29 |
>| Fuel Supply Emergency Coal | 27|


```sql
SELECT
    CHARINDEX ('_', url) AS char_location,
    url
FROM courses;
```

>| char_location | url |
>|-----------|--------------------------|
>| 34 | datacamp.com/courses/introduction_ |
>| 34 | datacamp.com/courses/intermediate_ |
>| 29 | datacamp.com/courses/writing_ |
>| 29 | datacamp.com/courses/joining_|

```sql
SELECT
    SUBSTRING(url, 12, 12) AS target_section,
    url
FROM courses;
```


>| target_section | url |
>|-|-|
>| datacamp.com |https//www.datacamp.com/courses |

```SQL
SELECT
TOP(3) REPLACE(url,'_','-') AS replace_with_hyphen
FROM courses;
```

>| replace_with_hyphen |
>|-------------------|
>| datacamp.com/courses/introduction- |
>| datacamp.com/courses/intermediate- |
>| datacamp.com/courses/writing- |

## HAVING
* Can use aggregate functions in `SELECT`
* Filter data using `WHERE`
* Split data into groups using `GROUP BY`
* What if we want to sum values based on groups?
* ... and then filter on those sums?

## Summary
* `GROUP` BY splits the data up into combinations of one or more values
* `WHERE` filters on row values
* `HAVING` appears after the `GROUP BY` clause and filters on groups or aggregates

<br>

# UNION & UNION ALL

### Union 
```sql
SELECT
    album_id,
    title,
    artist_id
FROM album
WHERE artist_id IN (1, 3)
UNION
SELECT
    album_id,
    title,
    artist_id
FROM album
WHERE artist_id IN (1, 4, 5);
```

>| album_id | title | artist_id |
>|------------|-----|------------|
>| 1 | For Those About To Rock | 1 |
>| 4 | Let There Be Rock | 1 |
>| 5 | Big Ones | 3 |
>| 6 | Jagged Little Pill | 4 |
>| 7 | Facelift | 5 |

* **Duplicate rows are *excluded***

<br><br>

### Union all

```sql
SELECT
    album_id,
    title,
    artist_id
FROM album
WHERE artist_id IN (1, 3)
UNION ALL
SELECT
    album_id,
    title,
    artist_id
FROM album
WHERE artist_id IN (1, 4, 5);
```

>| album_id | title | artist_id |
>|------------|-----|------------|
>| 1 | For Those About To Rock | 1 |
>| 4 | Let There Be Rock | 1 |
>| 5 | Big Ones | 3 |
>| 1 | For Those About To Rock | 1 |
>| 4 | Let There Be Rock | 1 |
>| 6 | Jagged Little Pill | 4 |
>| 7 | Facelift | 5 |

* ***Includes* duplicate rows**

## Summary
* `UNION` or `UNION ALL` : Combines queries from the same table or different tables
* If combining data from different tables:
* Select the same number of columns in the same order
* Columns should have the same data types
* If source tables have different column names
* Alias the column names
* `UNION` : Discards duplicates (slower to run)
* `UNION ALL` : Includes duplicates (faster to run)

# CRUD operations
**C**REATE
* Databases, Tables or views
* Users, permissions, and security groups

**R**EAD
* Example: SELECT statements

**U**PDATE
* Amend existing database records

**D**ELETE

## CREATE
* `CREATE TABLE` `unique table name`
* (column name, data type, size)

```sql
CREATE TABLE test_table(
    test_date date,
    test_name varchar(20),
    test_int int
    )
```

**A few considerations when creating a table**
* Table and column names
* Type of data each column will store
* Size or amount of data stored in the column

### Data types
Dates:
* date ( `YYYY-MM-DD` ), datetime ( `YYYY-MM-DD hh:mm:ss` )
* time

Numeric:
* integer, decimal, float
* bit ( `1` = `TRUE` , `0` = `FALSE` . Also accepts `NULL` values)

Strings:
* `char` , `varchar` , `nvarchar`

## INSERT
```sql
INSERT INTO table_name
```
```sql
INSERT INTO table_name (col1, col2, col3)
```
```sql
INSERT INTO table_name (col1, col2, col3)
VALUES
    ('value1', 'value2', value3)
```

### INSERT SELECT
```sql
INSERT INTO table_name (col1, col2, col3)
SELECT
    column1,
    column2,
    column3
FROM other_table
WHERE
    -- conditions apply
```
* Don't use `SELECT *`
* Be specific in case table structure changes

## UPDATE
```sql
UPDATE table
SET column = value
WHERE
-- Condition(s);
```
* Don't forget the `WHERE` clause!
```sql
UPDATE table
SET
    column1 = value1,
    column2 = value2
WHERE
-- Condition(s);
```

## DELETE
```sql
DELETE
FROM table
WHERE
    -- Conditions
```
* Test beforehand!
```sql
TRUNCATE TABLE table_name
```
* Clears the entire table at once

## Variables

### Declare
```sql
DECLARE @name type_data
```
Integer variable:
```sql
DECLARE @test_int INT
```
Varchar variable:
```sql
DECLARE @my_artist VARCHAR(100)
```

### SET
Integer variable:
```sql
DECLARE @test_int INT

SET @test_int = 5
```

Assign value to @my_artist :
```sql
DECLARE @my_artist varchar(100)

SET @my_artist = 'AC/DC'
```

### Example

```sql
DECLARE @my_artist varchar(100)
DECLARE @my_album varchar(300);

SET @my_artist = 'AC/DC'
SET @my_album = 'Let There Be Rock' ;

SELECT --
FROM --
WHERE artist = @my_artist
AND album = @my_album;
```

## Temporary tables
```sql
SELECT
    col1,
    col2,
    col3 INTO #my_temp_table
FROM my_existing_table
WHERE
    -- Conditions
```
* #my_temp_table exists until connection or session ends

```sql
-- Remove table manually
DROP TABLE #my_temp_table
```

