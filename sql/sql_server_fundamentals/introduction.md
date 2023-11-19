# STRINGS IN SQL 
```sql
SELECT
description,
LEN(description) AS description_length
FROM grid;
```
`NOTE: `In PostgreSQL `LENGTH (description)`
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

