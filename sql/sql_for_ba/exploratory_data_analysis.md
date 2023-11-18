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