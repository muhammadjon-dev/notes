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