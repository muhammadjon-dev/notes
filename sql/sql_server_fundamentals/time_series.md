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
* Year / Month / Day - `YEAR`, `MONTH`, `DAY`
* Day of year - `DY`, `DAYOFYEAR`
* Day of week - `WEEKDAY`
* Week of year - `WEEK`
* ISO week of year - `ISO_WEEK`
* Minute / Second - `MINUTE`, `SECOND`
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

> [!NOTE]
> `DATEPART()` and `DATENAME()` have similar syntax but differ slightly in functionality. `DATEPART()` returns only integer data type, while `DATENAME()` returns character data types, even for numerical values such as years

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


## Formatting functions
* `CAST()`
* `CONVERT()`
* `FORMAT()`

### CAST() function
* Supported since at least SQL Server 2000
* Converts one data type to another, including date types
* No control over formatting from dates to strings
* ANSI SQL standard, meaning most relational and most non-relational databases have this function

```sql
DECLARE
    @SomeDate DATETIME2(3) = '1991-06-04 08:00:09',
    @SomeString NVARCHAR(30) = '1991-06-04 08:00:09',
    @OldDateTime DATETIME = '1991-06-04 08:00:09';

SELECT
    CAST(@SomeDate AS NVARCHAR(30)) AS DateToString,
    CAST(@SomeString AS DATETIME2(3)) AS StringToDate,
    CAST(@OldDateTime AS NVARCHAR(30)) AS OldDateToString;
```

>|DateToString |StringToDate |OldDateToString|
>|-|-|-|
>1991-06-04 080009.000| 1991-06-04 080009.000 |Jun 4 1991 800AM

### CONVERT() function
* Supported going back at least to SQL Server 2000
* Useful for converting one data type to another data type, including date types
* Some control over formatting from dates to strings using the style parameter
* Specific to T-SQL

```sql
DECLARE
    @SomeDate DATETIME2(3) = '1793-02-21 11:13:19.033';

SELECT
    CONVERT(NVARCHAR(30), @SomeDate, 0) AS DefaultForm,
    CONVERT(NVARCHAR(30), @SomeDate, 1) AS US_mdy,
    CONVERT(NVARCHAR(30), @SomeDate, 101) AS US_mdyyyy,
    CONVERT(NVARCHAR(30), @SomeDate, 120) AS ODBC_sec;
```

>|DefaultForm |US_mdy |US_mdyyyy |ODBC_sec|
>|-|-|-|-|
>|Feb 21 1793 1113 AM| 02/21/93| 02/21/1793| 1793-02-21 111319|

### `CONVERT()` styles
|Style Code|Format|
|-|-|
1 / 101|United States m/d/y
3 / 103|British/French d/m/y
4 / 104|German d.m.y
11 / 111|Japanese y/m/d
12 / 112|ISO standard yyyymmdd
20 / 120|ODBC standard (121 for ms)
126|ISO8601 yyyy-mm-dd hh:mi:ss.mmm
127|yyyy-mm-ddThh:mi:ss.mmmZ

### FORMAT() function
* Supported as of SQL Server 2012
* Useful for formatting a date or number in a particular way for reporting
* Much more flexibility over formatting from dates to strings than either `CAST()` or `CONVERT()`
* Specific to T-SQL
* Uses the .NET framework for conversion
* Can be slower as you process more rows

```sql
DECLARE
    @SomeDate DATETIME2(3) = '1793-02-21 11:13:19.033';

SELECT
    FORMAT(@SomeDate, 'd', 'en-US') AS US_d,
    FORMAT(@SomeDate, 'd', 'de-DE') AS DE_d,
    FORMAT(@SomeDate, 'D', 'de-DE') AS DE_D,
    FORMAT(@SomeDate, 'yyyy-MM-dd') AS yMd;
```
>|US_d| DE_d| DE_D| yMd|
>|-|-|-|-|
>2/21/1793| 21.02.1793| Donnerstag, 21. February 1793| 1793-02-21|

> [!TIP]
> [Custom date and time format strings](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings)

## Dalendar table `dbo.Calendar`
|DateKey| Date| Day| DayOfWeek| DayName| ...|
|-|-|-|-|-|-|
|20000101| 2000-01-01| 1| 7| Saturday| ...|
|20000102 |2000-01-02 |2 |1 |Sunday |...|
|20000103| 2000-01-03| 3| 2| Monday |...|

### Contents of a calendar table
|General Columns|Calendar Year|Fiscal Year|Specialized Columns|
|-|-|-|-|
|Date |Calendar month|Fiscal week of year|Holiday name
|Day Name | Calendar quarter|Fiscal quarter|Lunar details
|Is Weekend|Calendar year|Fiscal first day of year|ISO week of year

### Building a calendar table
```sql
CREATE TABLE dbo.Calendar
(
    DateKey INT NOT NULL,
    [Date] DATE NOT NULL,
    [Day] TINYINT NOT NULL,
    DayOfWeek TINYINT NOT NULL,
    DayName VARCHAR(10) NOT NULL,
    ...
)
```
```sql
SELECT
    CAST(D.DateKey AS INT) AS DateKey,
    D.[DATE] AS [Date],
    CAST(D.[day] AS TINYINT) AS [day],
    CAST(d.[dayofweek] AS TINYINT) AS [DayOfWeek],
    CAST(DATENAME(WEEKDAY, d.[Date]) AS VARCHAR(10)) AS [DayName],
    ...
```

### Using a calendar table
```sql
SELECT
    c.Date
FROM dbo.Calendar c
WHERE
    c.MonthName = 'April'
    AND c.DayName = 'Saturday'
    AND c.CalendarYear = 2020
ORDER BY
    c.Date;
```
>|Date|
>|-|
>2020-04-04
>2020-04-11
>2020-04-18
>2020-04-25

## APPLY()
```sql
SELECT
    FYStart =
        DATEADD(MONTH, -6,
            DATEADD(YEAR,
                DATEDIFF(YEAR, 0,
                    DATEADD(MONTH, 6, d.[date])), 0)),
    FiscalDayOfYear =
        DATEDIFF(DAY,
            DATEADD(MONTH, -6,
                DATEADD(YEAR,
                    DATEDIFF(YEAR, 0,
                        DATEADD(MONTH, 6, d.[date])), 0)), d.[Date]) + 1,
    FiscalWeekOfYear =
        DATEDIFF(WEEK,
            DATEADD(MONTH, -6,
                DATEADD(YEAR,
                    DATEDIFF(YEAR, 0,
                    DATEADD(MONTH, 6, d.[date])), 0)), d.[Date]) + 1
FROM dbo.Calendar d;
```


```sql
SELECT
    fy.FYStart,
    FiscalDayOfYear = DATEDIFF(DAY, fy.FYStart, d.[Date]) + 1,
    FiscalWeekOfYear = DATEDIFF(WEEK, fy.FYStart, d.[Date]) + 1
FROM dbo.Calendar d
    CROSS APPLY
    (
        SELECT FYStart =
            DATEADD(MONTH, -6,
                DATEADD(YEAR,
                    DATEDIFF(YEAR, 0,
                        DATEADD(MONTH, 6, d.[date])), 0))
    ) AS fy;
```

# Building dates from parts

* `DATEFROMPARTS(year, month, day)`
* `TIMEFROMPARTS(hour, minute, second, fraction, precision)`
* `DATETIMEFROMPARTS(year, month, day, hour, minute, second, ms)`
* `DATETIME2FROMPARTS(year, month, day, hour, minute, second, fraction, precision)`
* `SMALLDATETIMEFROMPARTS(year, month, day, hour, minute)`
* `DATETIMEOFFSETFROMPARTS(year, month, day, hour, minute, second, fraction, hour_offset, minute_offset, precision)`

```sql
SELECT
DATETIMEFROMPARTS(1918, 11, 11, 05, 45, 17, 995) AS DT,
DATETIME2FROMPARTS(1918, 11, 11, 05, 45, 17, 0, 0) AS DT20,
DATETIME2FROMPARTS(1918, 11, 11, 05, 45, 17, 995, 3) AS DT23,
DATETIME2FROMPARTS(1918, 11, 11, 05, 45, 17, 9951234, 7) AS DT27;

```
DT |DT20| DT23| DT27|
|-|-|-|-|
1918-11-11 054517.997 |1918-11-11 054517 |1918-11-11 054517.995| 1918-11-11 054517.9951234

### offsets
```sql
SELECT
    DATETIMEOFFSETFROMPARTS(2009, 08, 14, 21, 00, 00, 0, 5, 0, 0) AS IST,
    DATETIMEOFFSETFROMPARTS(2009, 08, 14, 21, 00, 00, 0, 5, 30, 0) AT TIME ZONE 'UTC' AS UTC;
```

>IST |UTC
>|-|-|
>2009-08-14 210000 +0530 |2009-08-14 153000 +0000

## Translating date strings

* `CAST('09/14/99' AS DATE)`
>1999-09-14
* `CONVERT(DATETIME2(3), 'April 4, 2019 11:52:29.998 PM')`
>2019-04-04 235229.998
* `PARSE('25 Dezember 2014' AS DATE USING 'de-de') `
> 2014-12-25

Function| Conversions Per Second
|-|-|
`CONVERT()`| 251,997
`CAST()` |240,347
`PARSE()` |12,620

## Setting languages
```SQL
SET LANGUAGE 'FRENCH'

DECLARE
    @FrenchDate NVARCHAR(30) = N'18 avril 2019',
    @FrenchNumberDate NVARCHAR(30) = N'18/4/2019';

SELECT
    CAST(@FrenchDate AS DATETIME),
    CAST(@FrenchNumberDate AS DATETIME);
```
>2019-04-18 00:00:00.000

## DATETIMEOFFSET (date data type)
### Components
Date Part| Example|
|-|-|
Date |2019-04-10
Time |12:59:02.3908505
UTC Offset| -04:00

>2019-04-10 12:59:02.3908505 -04:00

### Changing offsets
```sql
DECLARE @SomeDate DATETIMEOFFSET =
    '2019-04-10 12:59:02.3908505 -04:00';

SELECT
    SWITCHOFFSET(@SomeDate,'-07:00') AS LATime;
```
>|LATime|
>|-|
>2019-04-10 09:59:02.3908505 -07:00

### Converting to DATETIMEOFFSET (`TODATETIMEOFFSET()`)

```sql
DECLARE @SomeDate DATETIME2(3) =
    '2019-04-10 12:59:02.390';
SELECT
    TODATETIMEOFFSET(@SomeDate,'-04:00') AS EDT;
```

>EDT|
>|-|
>2019-04-10 12:59:02.390 -04:00

## Error-safe date conversion functions

"Unsafe" Functions|Safe Functions|
|-|-|
`CAST()`|`TRY_CAST()`
`CONVERT()`|`TRY_CONVERT()`
`PARSE()`|`TRY_PARSE()`

> [!NOTE]
> If something happens wrong with converting date string to date then these safe functions will return NULL

## Key aggregation functions
**Counts**
* `COUNT()`
* `COUNT_BIG()`
* `COUNT(DISTINCT)`

**Other Aggregates**
* `SUM()`
* `MIN()`
* `MAX()`

### counts with `COUNT()`

Number of Rows|Non-NULL Values
|-|-|
`COUNT(*)`|`COUNT(d.YR)`
`COUNT(1)`|`COUNT(NULLIF(d.YR, 1990))`
`COUNT(1/0)`|

>[!tip]
>`NULLIF()` returns `NULL` if the two expressions are equal; otherwise, it returns the first expression. 
> Example: `NULLIF(10, 10)` > `NULL`; `NULLIF(20, 10)` > `20`.

## Statistical aggregate functions
|||
|-|-|
|AVG()|Mean
STDEV()|Standard Deviation
STDEVP()|Population Standard Deviation
VAR()|Variance
VARP()|Population Variance

### calculating median
```sql
SELECT TOP(1)
    PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY l.SomeVal DESC)
        OVER () AS MedianIncidents
FROM dbo.LargeTable l;
```

## Grouping by
### `ROLLUP`, `CUBE`, and `GROUPING SETS`

* `ROLLUP` - generates subtotals from left to right, producing results for each level of aggregation

**EXAMPLE:**
`ROLLUP(a, b)`
|a|b|
|-|-|
|a1|b1|
|a2|b2|
|a3|b3|

result:
||||
|-|-|-|
|a1|b1|aggregation
|a1|b2|aggregation
|a1|b3|aggregation
|a2|b1|aggregation
|a2|b2|aggregation
|a2|b3|aggregation
|a3|b1|aggregation
|a3|b2|aggregation
|a3|b3|aggregation
|a1|null|aggregation
|a2|null|aggregation
|a3|null|aggregation
|null|null|aggregation

```sql
SELECT rental_rate, rating, COUNT(*)
FROM film
GROUP BY 
    rental_rate, rating
WITH ROLLUP
ORDER BY rental_rate
```

|rental_rate|rating|count
|-|-|-|
0.99	|NC-17|	73|
0.99	|G	|64
0.99	|R	|70
0.99	|PG	|62
**0.99**	|**NULL**|	**341**
0.99	|PG-13|	72
2.99	|PG-13|	74
2.99	|NC-17|	66
2.99	|PG	|64
2.99	|R	|60
**2.99**	|**NULL**|	**323**
2.99	|G	|59
4.99	|R	|65
4.99	|G	|55
4.99	|NC-17|	71
4.99	|PG-13|	77
4.99	|PG	|68
**4.99**	|**NULL**|	**336**
**NULL**|**NULL**|		**1000**


* `CUBE` is similar to ROLLUP but generates all possible combinations of grouping sets. It computes subtotals for all possible combinations of columns specified in the GROUP BY clause. It's more comprehensive than ROLLUP.

**EXAMPLE:**
`CUBE(a, b)`
|a|b|
|-|-|
|a1|b1|
|a2|b2|

result:
||||
|-|-|-|
|a1|b1|aggregation
|a1|b2|aggregation
|a2|b1|aggregation
|a2|b2|aggregation
|a1|null|aggregation
|a2|null|aggregation
|null|b1|aggregation
|null|b2|aggregation
|null|null|aggregation

```SQL
SELECT
    t.IncidentType,
    t.Office,
    SUM(t.Events) AS Events
FROM Table
GROUP BY
    t.IncidentType,
    t.Office
WITH CUBE
ORDER BY
    t.IncidentType,
    t.Office;
```

IncidentType| Office| Events|
|-|-|-|
NULL |NULL| 250
NULL |NY |70
NULL |CT| 180
T1 |NULL |55
T1 |NY| 30
T1 |CT |25

* `GROUPING SETS` - allows the specification of multiple grouping sets within a single GROUP BY clause. Unlike ROLLUP and CUBE, it gives more control over which subsets of data you want to aggregate.

```sql
SELECT
    t.IncidentType,
    t.Office,
    SUM(t.Events) AS Events
FROM Table
GROUP BY GROUPING SETS
(
    (t.IncidentType, t.Office),
    ()
)
ORDER BY
    t.IncidentType,
    t.Office;
```

IncidentType| Office| Events|
|-|-|-|
T1 |NY| 30
T1 |CT| 25
T2 |NY| 10
T2 |CT| 110
T3 |NY| 30
T3 |CT| 45

# WINDOW functions
## Ranking functions
* `ROW_NUMBER()` - 
Unique, ascending integer value starting from 1.
* `RANK()` - Ascending integer value starting from 1. Can
have ties. Can skip numbers.
* `DENSE_RANK()` - Ascending integer value starting from 1. Can have ties. Will not skip numbers.

```sql
SELECT
    s.RunsScored,
    ROW_NUMBER() OVER (
        ORDER BY s.RunsScored DESC
    ) AS rn,
    RANK() OVER (
        ORDER BY s.RunsScored DESC
    ) AS rk,
    DENSE_RANK() OVER (
        ORDER BY s.RunsScored DESC
    ) AS dr
FROM dbo.Scores s
ORDER BY
    s.RunsScored DESC;
```

|RunsScored| rn|rk| dr|
|-|-|-|-|
8 |1|1| 1
7 |2|2| 2
7 |3|2| 2
6 |4|4| 3
6 |5|4| 3
3 |6|6| 4

### Partitions

```sql
SELECT
    s.Team,
    s.RunsScored,
    ROW_NUMBER() OVER (
        PARTITION BY s.Team
        ORDER BY s.RunsScored DESC
    ) AS rn
FROM dbo.Scores s
ORDER BY
    s.RunsScored DESC;
```

Team| RunsScored| rn|
|-|-|-|
AZ |8| 1
AZ |6| 2
AZ |3| 3
FLA |7| 1
FLA |7| 2
FLA |6| 3


## Aggregate functions

```sql
SELECT
    s.Team,
    s.RunsScored,
    MAX(s.RunsScored) OVER (
        PARTITION BY s.Team
    ) AS MaxRuns
FROM dbo.Scores s
ORDER BY
    s.RunsScored DESC;
```

Team| RunsScored| MaxRuns|
|-|-|-|
AZ |8| 8
AZ |6| 8
AZ |3| 8
FLA |7| 7
FLA |7| 7
FLA |6| 7

## Aggregations with empty windows

```sql
SELECT
    s.Team,
    s.RunsScored,
    MAX(s.RunsScored) OVER () AS MaxRuns
FROM dbo.Scores s
ORDER BY
    s.RunsScored DESC;
```

Team| RunsScored| MaxRuns|
|-|-|-|
AZ |8| 8
AZ |6| 8
AZ |3| 8
FLA |7| 8
FLA |7| 8
FLA |6| 8

```sql
SELECT
    s.Team,
    s.Game,
    s.RunsScored,
    SUM(s.RunsScored) OVER (
        PARTITION BY s.Team
        ORDER BY s.Game ASC
        RANGE BETWEEN
            UNBOUNDED PRECEDING
            AND CURRENT ROW
    ) AS TotalRuns, 
    AVG(s.RunsScored) OVER (
        PARTITION BY s.Team
        ORDER BY s.Game ASC
            ROWS BETWEEN 1 PRECEDING
            AND CURRENT ROW
    ) AS AvgRuns
FROM #Scores s;
```

|Team| Game| RunsScored| TotalRuns|AvgRuns
|-|-|-|-|-|
|AZ |1| 8| 8|8
|AZ |2| 6| 14|7
|AZ |3| 3| 17|4
|FLA |1| 7| 7|7
|FLA |2| 7| 14|7
|FLA |3| 6| 20|6

## RANGE and ROWS
* `RANGE`
    * Specify a range of results
    * "Duplicates" processed all at once
    * Only supports `UNBOUNDED` and `CURRENT ROW`
* `ROWS`
    * Specify number of rows to include
    * "Duplicates" processed a row at a time
    * Supports `UNBOUNDED` , `CURRENT ROW` , and number of rows

## `LAG()` and `LEAD()`
```sql
SELECT
    dsr.CustomerID,
    dsr.MonthStartDate,
    LAG(dsr.NumberOfVisits, 2) OVER (PARTITION BY dsr.CustomerID ORDER BY dsr.MonthStartDate) AS Prior2,
    LAG(dsr.NumberOfVisits, 1) OVER (PARTITION BY dsr.CustomerID ORDER BY dsr.MonthStartDate) AS Prior1,
    dsr.NumberOfVisits, 
    LEAD(dsr.NumberOfVisits, 1) OVER (PARTITION BY dsr.CustomerID ORDER BY dsr.MonthStartDate) AS Next1,
    LEAD(dsr.NumberOfVisits, 2) OVER (PARTITION BY dsr.CustomerID ORDER BY dsr.MonthStartDate) AS Next2
FROM dbo.DaySpaRollup dsr;
```

CustomerID| MonthStartDate| Prior2| Prior| NumberOfVisits|Next1|Next2|
|-|-|-|-|-|-|-|
1 |2018-12-01| NULL| NULL| 49| 117|104|
1 |2019-01-01| NULL| 49| 117|  104|NULL|
1 |2019-02-01| 49| 117| 104|   NULL|NULL|

## Windows and filters

```SQL
SELECT
    Date,
    LAG(Val, 1) OVER(ORDER BY DATE) AS PriorVal,
    Val
FROM t;
```
Date| PriorVal| Val|
|-|-|-|
2019-01-01 |NULL| 3
2019-01-02 |3| 6
2019-01-03 |6| 4

```SQL
SELECT
Date,
LAG(Val, 1) OVER(ORDER BY DATE) AS PriorVal,
Val
FROM t
WHERE
t.Date > '2019-01-02';
```
Date| PriorVal| Val|
|-|-|-|
2019-01-03 |NULL| 4

### Windows and filters and CTEs
```SQL
WITH records AS (
    SELECT
        Date,
        LAG(Val, 1) OVER(ORDER BY Date) AS PriorVal,
        Val
    FROM t
)
SELECT
    r.Date,
    r.PriorVal,
    r.Val
FROM records r
WHERE
    r.Date > '2019-01-02';
```

Date| PriorVal| Val|
|-|-|-|
2019-01-03 |6| 4