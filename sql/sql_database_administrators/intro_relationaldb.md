# Constraints

**Integrity constraints**
1. **Attribute constraints**, e.g. data types on columns (Chapter 2)
1. **Key constraints**, e.g. primary keys (Chapter 3)
1. **Referential integrity constraints**, enforced through foreign keys (Chapter 4)

### Why constraints?
* Constraints give the data structure
* Constraints help with consistency, and thus data quality
* Data quality is a business advantage / data science prerequisite
* Enforcing is difficult, but PostgreSQL helps

![](https://telegra.ph/file/59fff4bb9d1f926a52a3d.png)

From the [**PostgreSQL documentation**](https://www.postgresql.org/docs/10/datatype.html).

## The most common types
* `text` : character strings of any length
* `varchar [ (x) ]` : a maximum of `n` characters
* `char [ (x) ]` : a fixed-length string of `n` characters
* `boolean` : can only take three states, e.g. `TRUE` , `FALSE` and `NULL` (unknown)

* `date` , `time` and `timestamp` : various formats for date and time calculations
* `numeric` : arbitrary precision numbers, e.g. `3.1457`
* `integer` : whole numbers in the range of `-2147483648` and `+2147483647`

## Alter types after table creation
```sql
ALTER TABLE students
ALTER COLUMN name
TYPE varchar(128);


ALTER TABLE students
ALTER COLUMN average_grade
TYPE integer
-- Turns 5.54 into 6, not 5, before type conversion
USING ROUND(average_grade);
```

## The not-null constraint
* Disallow `NULL` values in a certain column
* Must hold true for the current state
* Must hold true for any future state

### add or remove a not-null constraint

* When creating a table...
```sql
CREATE TABLE students (
    ssn integer not null,
    lastname varchar(64) not null,
    home_phone integer,
    office_phone integer
);
```

* After the table has been created...
```sql
ALTER TABLE students
ALTER COLUMN home_phone
SET NOT NULL;

ALTER TABLE students
ALTER COLUMN ssn
DROP NOT NULL;
```

## Adding **unique** constraints
```sql
CREATE TABLE table_name (
    column_name UNIQUE
);

ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE(column_name);
```

