-- Athlete count by country and region
SELECT reg.region
  , reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes -- Athletes can compete in multiple events
FROM athletes as ath
INNER JOIN oregions as reg
  ON reg.olympic_cc = ath.country_code
GROUP BY reg.region, reg.country
ORDER BY no_athletes;


SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM regions reg
LEFT JOIN athletes ath
  ON reg.olympic_cc = ath.country_code
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;

SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM athletes ath
RIGHT JOIN regions reg
  ON ath.country_code = reg.olympic_cc
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;


SELECT reg.region, reg.country
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
FROM regions reg
INNER JOIN athletes ath
  ON ath.country_code = reg.olympic_cc
GROUP BY reg.region, reg.country
ORDER BY no_athletes DESC;



SELECT reg.region
  , ath.season
  , COUNT(DISTINCT ath.athlete_id) AS no_athletes
  , COUNT(DISTINCT reg.olympic_cc) AS no_countries
  , COUNT(DISTINCT ath.athlete_id)/COUNT(DISTINCT reg.olympic_cc) AS athletes_per_country
FROM athletes ath
INNER JOIN oregions reg
  ON ath.country_code = reg.olympic_cc
GROUP BY reg.region, ath.season -- Group by region and season
ORDER BY reg.region, athletes_per_country;



-- Countries cold enough for snow year-round
SELECT country_code
  , country
  , COUNT (DISTINCT athlete_id) AS winter_athletes -- Athletes can compete in multiple events 
FROM athletes
WHERE country_code IN (SELECT olympic_cc FROM oclimate WHERE temp_annual < 0)
AND season = 'Winter'
GROUP BY country_code, country;


-- cte

WITH south_cte AS -- CTE
(
  SELECT region
    , ROUND(AVG(temp_06),2) AS avg_winter_temp
    , ROUND(AVG(precip_06),2) AS avg_winter_precip
  FROM oclimate
  WHERE region IN ('Africa','South America','Australia and Oceania')
  GROUP BY region
)

SELECT south.region, south.avg_winter_temp, south.avg_winter_precip
  , COUNT(DISTINCT ath.athlete_id)
FROM south_cte as south
INNER JOIN athletes_recent ath
  ON south.region = ath.region
  AND ath.season = 'Winter'
GROUP BY south.region, south.avg_winter_temp, south.avg_winter_precip
ORDER BY south.avg_winter_temp;



WITH countries_cte AS -- CTE
(
    SELECT olympic_cc
      , country
      , temp_06
      , precip_06
    FROM climate
    WHERE region = 'Africa'
)

SELECT DISTINCT cte.country
  , cte.temp_06
  , cte.precip_06
FROM athletes_wint AS wint
INNER JOIN countries_cte AS cte
  ON wint.country_code = cte.olympic_cc
ORDER BY temp_06;






-- Create a temp table of Canadians
CREATE TEMP TABLE canadians AS
    SELECT *
    FROM athletes_recent
    WHERE country_code = 'CAN'
    AND season = 'Winter'; -- The table has both summer and winter athletes

-- Find the most popular sport
SELECT sport
  , COUNT(DISTINCT athlete_id) as no_athletes
FROM canadians
GROUP BY sport 
ORDER BY no_athletes DESC;


-- Create temp countries table
CREATE TEMP TABLE countries AS
    SELECT DISTINCT o.region, a.country_code, o.country
    FROM athletes a
    INNER JOIN oregions o
      ON a.country_code = o.olympic_cc;
      
ANALYZE countries; -- Collect the statistics

-- Count the entries
SELECT COUNT(*) FROM countries;


-- numeric filters are better than text filters
-- Shorter length
-- Smaller storage
-- Speeds performance

-- Good | Better
------------------
-- Text | Numeric
-- OR   | IN, ARRAY



-- Aggregating with different data granularities

-- Number of competing athletes (Changing the table granularity)
WITH athletes as (
  SELECT country_code, year, COUNT(athlete_id) AS no_athletes
  FROM athletes
  GROUP BY country_code, year
)

-- (Matching data granularity when joining)
SELECT demos.country, ath.year, ath.no_athletes
    , demos.gdp_rank
    , demos.population_rank
FROM athletes ath
INNER JOIN demographics_rank demos  
  ON ath.country_code = demos.olympic_cc -- Country
  AND ath.year = demos.year -- Year
ORDER BY ath.no_athletes DESC;

-- advs of matching data granularity when joining
-- No repeats or duplicates
-- Minimum needed results
-- No double counting



-- South African athletes by year
WITH athletes_cte AS 
(
    SELECT year
      , season
      , COUNT(DISTINCT athlete_id) AS no_athletes
    FROM athletes
    WHERE country_code = 'RSA' -- South Africa filter
    GROUP BY year, season
)

SELECT ath.year
  , ath.season
  , ath.no_athletes
  , demos.gdp_rounded
  , demos.gdp_rank
  , demos.population_rounded
  , demos.population_rank
FROM athletes_cte ath
INNER JOIN demographics_rank demos
  ON ath.year = demos.year
  AND olympic_cc = 'RSA' -- Filter to South Africa
ORDER BY ath.season, ath.year;




SELECT *
FROM information_schema.tables 
WHERE table_catalog = 'olympics_aqi' 
AND table_name = 'annual_aqi';




EXPLAIN
SELECT * 
FROM daily_aqi
WHERE state_code = 15; -- Hawaii state code

-- Seq Scan on daily_aqi  (cost=0.00..561.98 rows=72 width=182)
--   Filter: (state_code = 15)


SELECT tablename, indexname
FROM pg_indexes

-- tablename	| indexname
-----------------------------------------------
-- pg_proc		| pg_proc_proname_args_nsp_index
-- pg_type		| pg_type_typname_nsp_index
-- pg_attribute	| pg_attribute_relid_attnam_index
-- demographics	| demographics_pkey



-- creating indexes 
CREATE INDEX defining_parameter_index -- index name
 ON daily_aqi (defining_parameter); -- Define the index creation (ON table_name (column_name))

SELECT indexname -- Check for the index
FROM pg_indexes
WHERE tablename = 'daily_aqi';

