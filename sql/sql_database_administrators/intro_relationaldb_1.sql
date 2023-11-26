

-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT * 
FROM professors

-- Create a table for the universities entity type
CREATE TABLE universities (
    university_shortname text,
    university text,
    university_city text
);

-- CREATE TABLE organizations

-- Print the contents of this table
SELECT * 
FROM universities


-- ALTER TABLE table_name
-- ADD COLUMN column_name data_type;

-- Add the university_shortname column
ALTER TABLE professors
ADD university_shortname text;

-- Print the contents of this table
SELECT * 
FROM professors

-- To rename columns:
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;

-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;


-- To delete columns:
ALTER TABLE table_name
DROP COLUMN column_name;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;


-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM  university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM  university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;

-- Delete the university_professors table
DROP TABLE university_professors;

