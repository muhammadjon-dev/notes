# Building dates
```sql
SELECT
    GETDATE() AS DateTime_LTz,
    GETUTCDATE() AS DateTime_UTC;

SELECT
    SYSDATETIME() AS DateTime2_LTz
    SYSUTCDATETIME() AS DateTime2_UTC;
```

>Results

|DateTime_LTz| DateTime_UTC| DateTime2_LTz |DateTime2_UTC|
|-|-|-|-|
|2019-03-07 212133.670|2019-03-08 022133.670|2019-03-07 212133.6716402| 2019-03-08 022133.6716402|

## Breaking down a date
```sql
DECLARE 
    @SomeDate DATETIME2(3) = '2019-03-01 08:17:19.332';
```
```sql
SELECT YEAR(@SomeDate);
```
```sql
SELECT MONTH(@SomeDate);
```
```sql
SELECT DAY(@SomeDate);
```

* `YEAR` = 2019
* `MONTH` = 3
* `DAY` = 1

### Parsing dates with date parts
#### Parts
* Year / Month / Day
* Day of year
* Day of week
* Week of year
* ISO week of year
* Minute / Second
* Millisecond / Nanosecond

#### Functions
`DATEPART()`
```sql
SELECT
    DATEPART(YEAR, @dt) AS TheYear;
```
`DATENAME()`
```sql
SELECT
    DATENAME(MONTH, @dt) AS TheMonth;
```
