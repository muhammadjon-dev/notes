CREATE DATABASE 


-- Define the business_type table below
CREATE TABLE business_type (
	id serial PRIMARY KEY,
  	description TEXT NOT NULL
);

-- Define the applicant table below
CREATE TABLE applicant (
	id serial PRIMARY KEY,
  	name TEXT NOT NULL,
  	zip_code CHAR(5) NOT NULL,
  	business_type_id INTEGER references business_type(id)
);


-- Add a schema for Ann Simmons
CREATE SCHEMA ann_simmons;

-- Add a schema for Ty Beck
CREATE SCHEMA ty_beck;

-- Add a schema for production data
CREATE SCHEMA production;

-- Add users table to the public schema for the pod database
CREATE TABLE public.users (
  id serial PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT NOT NULL,
  hashed_password CHAR(72) NOT NULL
);


-- Create a table named 'bank' in the 'loan_504' schema
CREATE TABLE loan_504.bank (
    id serial PRIMARY KEY,
    name VARCHAR (100) NOT NULL
);


-- Create a table named 'bank' in the 'loan_7a' schema
Create TABLE loan_7a.bank  (
    id SERIAL PRIMARY KEY,
    name VARCHAR (100) NOT NULL,
  	express_provider BOOLEAN
);

-- Create a table named 'borrower' in the 'loan_504' schema
CREATE TABLE loan_504.borrower (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR (100) NOT NULL
);


-- Create a table named 'borrower' in the 'loan_7a' schema
CREATE TABLE loan_7a.borrower (
    id serial PRIMARY KEY,
    full_name VARCHAR (100) NOT NULL,
  	individual BOOLEAN
);


-- Create the project table
CREATE TABLE project (
	-- Unique identifier for projects
	id SERIAL PRIMARY KEY,
    -- Whether or not project is franchise opportunity
	is_franchise BOOLEAN DEFAULT FALSE,
	-- Franchise name if project is franchise opportunity
    franchise_name TEXT DEFAULT NULL,
    -- State where project will reside
    project_state TEXT,
    -- County in state where project will reside
    project_county TEXT,
    -- District number where project will reside
    congressional_district NUMERIC,
    -- Amount of jobs projected to be created
    jobs_supported NUMERIC
);


-- Create the appeal table
CREATE TABLE appeal (
    -- Specify the unique identifier column
	id SERIAL PRIMARY KEY,
    -- Define a column for holding the text of the appeals
    content TEXT NOT NULL
);


-- Create the client table
CREATE TABLE client (
	-- Unique identifier column
	id SERIAL PRIMARY KEY,
    -- Name of the company
    name VARCHAR(50),
	-- Specify a text data type for variable length urls
	site_url VARCHAR(50),
    -- Number of employees (max of 1500 for small business)
    num_employees SMALLINT,
    -- Number of customers
    num_customers INTEGER
);


-- Create the campaign table
CREATE TABLE campaign (
  -- Unique identifier column
  id SERIAL PRIMARY KEY,
  -- Campaign name column
  name varchar(50),
  -- The campaign's budget
  budget NUMERIC(7, 2),
  -- The duration of campaign in days
  num_days smallint DEFAULT 30,
  -- The number of new applications desired
  goal_amount integer DEFAULT 100,
  -- The number of received applications
  num_applications integer DEFAULT 0
);

CREATE TABLE appeal (
	id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
  	-- Add received_on column
    received_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  	
  	-- Add approved_on_appeal column
  	approved_on_appeal BOOLEAN DEFAULT NULL,
  	
  	-- Add reviewed column
    reviewed DATE
);

-- Create the loan table
CREATE table loan (
    borrower_id INTEGER REFERENCES borrower(id),
    bank_id INTEGER REFERENCES bank(id),
  	-- 'approval_date': the loan approval date
    approval_date date NOT NULL DEFAULT CURRENT_DATE,
    -- 'gross_approval': amounts up to $5,000,000.00
  	gross_approval DECIMAL(9, 2) NOT NULL,
  	-- 'term_in_months': total # of months for repayment
    term_in_months smallint NOT NULL,
    -- 'revolver_status': TRUE for revolving line of credit
  	revolver_status boolean NOT NULL DEFAULT FALSE,
  	initial_interest_rate DECIMAL(4, 2) NOT NULL
);


-- Create the place table
CREATE TABLE place (
  -- Define zip_code column
  zip_code CHAR(5) PRIMARY KEY,
  -- Define city column
  city VARCHAR(50) NOT NULL,
  -- Define state column
  state CHAR(2) NOT NULL
);

CREATE TABLE borrower (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  approved BOOLEAN DEFAULT NULL,
  
  -- Remove zip_code column (defined below)
  -- zip_code CHAR(5) NOT NULL,
  
  -- Remove city column (defined below)
  -- city VARCHAR(50) NOT NULL,
  
  -- Remove state column (defined below)
  -- state CHAR(2) NOT NULL,
  
  -- Add column referencing place table
  place_id char(5) references place(zip_code)
);


-- Create the contact table
CREATE TABLE contact (
  	-- Define the id primary key column
	id SERIAL PRIMARY KEY,
  	-- Define the name column
  	name VARCHAR(50) NOT NULL,
    -- Define the email column
  	email VARCHAR(50) NOT NULL
);

-- Add contact_id to the client table
ALTER TABLE client ADD contact_id INTEGER NOT NULL;

-- Add a FOREIGN KEY constraint to the client table
ALTER TABLE client ADD CONSTRAINT fk_c_id FOREIGN KEY (contact_id) REFERENCES contact(id);



CREATE TABLE ingredient (
  -- Add PRIMARY KEY for table
  id serial PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE meal (
    -- Make id a PRIMARY KEY
	id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,

	-- Remove the 2 columns (below) that do not satisfy 2NF
  	-- ingredients VARCHAR(150), -- comma separated list
    avg_student_rating NUMERIC,
    -- date_served DATE,
    total_calories SMALLINT NOT NULL
);

CREATE TABLE meal_date (
    -- Define a column referencing the meal table
  	meal_id INTEGER REFERENCES meal(id),
    date_served DATE NOT NULL
);

CREATE TABLE meal_ingredient (
  	meal_id INTEGER REFERENCES meal(id),
  
    -- Define a column referencing the ingredient table
    ingredient_id INTEGER REFERENCES ingredient(id)
);


-- Complete the definition of the table for zip codes
CREATE TABLE zip (
	code INTEGER PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL
);

-- Complete the definition of the "zip_code" column
CREATE TABLE school (
	id serial PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    street_address VARCHAR(100) NOT NULL,
    zip_code INTEGER REFERENCES zip(code)
);


-- creating users

-- Create sgold with a temporary password
CREATE USER sgold WITH PASSWORD 'changeme';

-- Update the password for sgold
ALTER USER sgold WITH PASSWORD 'kxqr478-?egH%&FQ';

-- Grant the INSERT privilege
GRANT INSERT ON loan TO sgold;

-- Grant the UPDATE privilege
GRANT UPDATE ON loan TO sgold;

-- Grant the SELECT privilege
GRANT SELECT ON loan TO sgold;

-- Grant the DELETE privilege
GRANT DELETE ON loan TO sgold;

-- Provide sgold with the required table privileges
ALTER TABLE loan owner TO sgold;






-- Create a user account for Ronald Jones
CREATE USER rjones WITH PASSWORD 'changeme';

-- Create a user account for Kim Lopez
CREATE USER klopez WITH PASSWORD 'changeme';

-- Create a user account for Jessica Chen
CREATE USER jchen WITH PASSWORD 'changeme';

-- Create the dev_team group
CREATE GROUP dev_team;

-- Grant privileges to dev_team group on loan table
GRANT INSERT, UPDATE, DELETE, SELECT ON loan TO dev_team;

-- Add the new user accounts to the dev_team group
ALTER GROUP dev_team ADD USER rjones, klopez, jchen;




-- Create the development schema
CREATE SCHEMA development;

-- Grant usage privilege on new schema to dev_team
GRANT usage ON SCHEMA development TO dev_team;

-- Create a loan table in the development schema
CREATE TABLE development.loan (
	borrower_id INTEGER,
	bank_id INTEGER,
	approval_date DATE,
	program text NOT NULL,
	max_amount DECIMAL(9,2) NOT NULL,
	gross_approval DECIMAL(9, 2) NOT NULL,
	term_in_months SMALLINT NOT NULL,
	revolver_status BOOLEAN NOT NULL,
	bank_zip VARCHAR(10) NOT NULL,
	initial_interest_rate DECIMAL(4, 2) NOT NULL
);

-- Grant privileges on development schema
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA development TO dev_team;


-- Remove the specified privileges for Kim
REVOKE INSERT, UPDATE, DELETE ON development.loan FROM klopez;




-- Create the project_management group
CREATE GROUP project_management;

-- Grant project_management SELECT privilege
GRANT SELECT ON loan TO project_management;

-- Add Kim's user to project_management group
ALTER GROUP project_management ADD USER klopez;

-- Remove Kim's user from dev_team group
REVOKE dev_team FROM klopez;
















