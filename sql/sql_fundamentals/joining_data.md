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

![Alt text](image.png)
