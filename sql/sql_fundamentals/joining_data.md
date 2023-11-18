# Joining data in SQL

## Inner join
```sql
INNER JOIN
``` 
looks for records in both tables which match on a given field


<br>

`before inner join`
|left_table| | |right_table||
|-----|----|-----|-----|----|
|id|left_val||id|right_val|
|1|L1||1|R1|
|2|L2||4|R2|
|3|L3||5|R3|
|4|L4||6|R4|

<br>

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*lq8yHCIAo4-EYc14Nrnr2w.png)

```sql
FROM left_table AS lt 
INNER JOIN right_table AS rt
ON lt.id = rt.id
``` 

`after inner join`

|id|left_val|right_val|
|-----|-----|-----|
|1|L1|R1|
|4|L4|R2|

### Using **USING**

```sql
--Inner join of presidents and prime_ministers, joining on country
SELECT p1.country, p1.continent, prime_minister, president
FROM prime_ministers AS p1
INNER JOIN presidents AS p2
USING(country);
```

| country | continent | prime_minister | president |
|----------------|-----------|------------------|-------------------------|
| Egypt | Africa | Mostafa Madbouly | Abdel Fattah el-Sisi |
| Portugal | Europe | António Costa | Marcelo Rebelo de Sousa |
| Pakistan | Asia | Shehbaz Sharif | Arif Alvi |
| India | Asia | Narendra Modi | Ram Nath Kovind |


### Relationships
* One-to-Many relationships <small>(authors -> books)</small>
* One-to-one relationships <small>(individuals -> fingerprints)</small>
* Many-to-Many relationships <small>(countries -> languages)</small>

### Multiple Joins 
```sql
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id
INNER JOIN another_table
ON left_table.id = another_table.id;
```

`Note. Depending on the use case, left_table or right_table can be used in the ON clause`

### Joining on multiple keys
```sql
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id
    AND left_table.date = right_table.date;
```


___
<br>

## LEFT and RIGHT JOINs

```sql
LEFT JOIN
``` 
will return all records in the left table, and those records in the right table that match on the joining field provided

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*2wSOXRXritBbiSJRZ0YtSA.jpeg)

### LEFT JOIN syntax
```sql
SELECT p1.country, prime_minister, president
FROM prime_ministers AS p1
LEFT JOIN presidents AS p2
USING(country);
```
`Note. LEFT JOIN can also be written as LEFT OUTER JOIN`

----
<br>

```sql
RIGHT JOIN
``` 
will return all records in the right table, and those records in the left table that match on the joining field provided

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*otALwRC1--ppxbXI1wQ6eQ.jpeg)

### RIGHT JOIN syntax
```sql
SELECT p1.country, prime_minister, president
FROM prime_ministers AS p1
RIGHT JOIN presidents AS p2
USING(country);
```
`Note. RIGHT JOIN can also be written as RIGHT OUTER JOIN`

----
<br>

### LEFT JOIN or RIGHT JOIN?
* RIGHT JOIN is less commonly used than LEFT JOIN
* Any RIGHT JOIN can be re-written as a LEFT JOIN
* LEFT JOIN feels more intuitive to users when typing from left to right

----
<br>

## FULL JOIN

A `FULL JOIN` combines a `LEFT JOIN` and a `RIGHT JOIN`

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*pBdMUFb6OybesRA5zPkokw.jpeg)

### FULL JOIN syntax

```SQL
SELECT left_table.id AS L_id,
    right_table.id AS R_id,
    left_table.val AS L_val,
    right_table.val AS R_val
FROM left_table
FULL JOIN right_table
USING (id);
```
`Note. The keyword FULL OUTER JOIN can also be used`

----
<br>

## CROSS JOIN

`CROSS JOIN` creates all possible combinations of `two tables`.

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*bK942OIGAl_pr1v0jsclVg.jpeg)


### CROSS JOIN syntax
```sql
SELECT id1, id2
FROM table1
CROSS JOIN table2;
```

More information: [medium.com](https://spardhax.medium.com/all-the-joins-in-sql-visualised-and-simplified-3df0687a8624)

----
<br>

## Self joins
* `Self joins` are tables joined with `themselves` 
* They can be used to `compare parts` of the same table

```sql
SELECT
p1.country AS country1,
p2.country AS country2,
p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent
LIMIT 10;
```

`result:`

| country1 | country2 | continent |
|------------|------------|---------------|
| Egypt | Egypt | Africa |
| Portugal | Spain | Europe |
| Portugal | Norway | Europe |
| Portugal | Portugal | Europe |
| Vietnam | Oman | Asia |
| Vietnam | Brunei | Asia |
| Vietnam | India | Asia |
| Vietnam | Vietnam | Asia |
| Haiti | Haiti | North America |
| India | Oman | Asia |
| India | Brunei | Asia |

---

