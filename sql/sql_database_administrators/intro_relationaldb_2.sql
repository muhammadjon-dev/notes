-- Changing type of columns after creation
-- Specify the correct fixed-length character type
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE CHAR(3);

-- Change the type of firstname
ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

-- converting data to new type of column 
ALTER TABLE table_name
ALTER COLUMN column_name
TYPE varchar(x)
USING SUBSTRING(column_name FROM 1 FOR x)

-- setting not null for firstname after creation
-- Disallow NULL values in firstname
ALTER TABLE professors 
ALTER COLUMN firstname SET NOT NULL;

-- setting not null
ALTER TABLE students
ALTER COLUMN home_phone
SET NOT NULL;

-- dropping not null
ALTER TABLE students
ALTER COLUMN ssn
DROP NOT NULL;


-- unique
CREATE TABLE table_name (
 column_name UNIQUE
);

-- unique in already created table
ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE(column_name);

-- Make universities.university_shortname unique
ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE(university_shortname);

-- Make organizations.organization unique
ALTER TABLE organizations
ADD CONSTRAINT organization_unq UNIQUE(organization)