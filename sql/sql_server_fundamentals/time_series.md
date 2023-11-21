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

## Adding and subtracting dates
```sql
DECLARE
    @SomeTime DATETIME2(7) = '1992-07-14 14:49:36.2294852';
SELECT
    DATEADD(DAY, 1, @SomeTime) AS NextDay,
    DATEADD(DAY, -1, @SomeTime) AS PriorDay;
SELECT
    DATEADD(HOUR, -3, DATEADD(DAY, -4, @SomeTime)) AS Minus4Days3Hours;
```

|NextDay |PriorDay|
|-|-|
|1992-07-15 144936.2294852 |1992-07-13 144936.2294852|
|**Minus4Days3Hours**||
|1992-07-10 114936.2294852|

### Comparing dates
```sql
DECLARE
    @StartTime DATETIME2(7) = '2012-03-01 14:29:36',
    @EndTime DATETIME2(7) = '2012-03-01 18:00:00';
```    
```sql
SELECT
    DATEDIFF(SECOND, @StartTime, @EndTime) AS SecondsElapsed,
    DATEDIFF(MINUTE, @StartTime, @EndTime) AS MinutesElapsed,
    DATEDIFF(HOUR, @StartTime, @EndTime) AS HoursElapsed;
```
>|SecondsElapsed| MinutesElapsed| HoursElapsed|
>|-|-|-|
>|12624| 211| 4|

### Rounding dates
```sql
DECLARE @SomeTime DATETIME2(7) = '2017-05-12 16:25:16.2248991';

SELECT
    DATEADD(DAY, DATEDIFF(DAY, 0, @SomeTime), 0) AS RoundedToDay,
    DATEADD(HOUR, DATEDIFF(HOUR, 0, @SomeTime), 0) AS RoundedToHour,
    DATEADD(MINUTE, DATEDIFF(MINUTE, 0, @SomeTime), 0) AS RoundedToMinute;
```
>|RoundedToDay| RoundedToHour| RoundedToMinute|
>|-|-|-|
>2017-05-12 00:00:00| 2017-05-12 16:00:00| 2017-05-12 16:25:00

