-- You will find a dump of a sample database (misspellings.sql) in our
-- shared data folder. This is essentially the same list of misspellings
-- we used in our Python lab, so you can use that source data file to 
-- check your accuracy.
-- 
-- We will use a more extensive database on our server
-- for official scoring. You can assume the table and column names
-- remain the same.


-- You can uncomment this for testing, but leave it commented out
-- when you submit your script.
-- USE misspellings;


-- You can uncomment this for testing, but leave it commented out
-- when you submit your script. The system will set this variable to 
-- various target words when scoring your query.
-- SET @word = 'immediately';

-- Here is a very basic approach (removing double m's) that returns
-- 2 of the 6 variants in the sample database when searching for 
-- 'immediately'.

-- v1
SELECT id, misspelled_word
  FROM word 
 WHERE REPLACE(misspelled_word, 'mm', 'm') = REPLACE(@word, 'mm', 'm')
 OR REPLACE(misspelled_word, 'nn', 'n') = REPLACE(@word, 'nn', 'n')
 OR REPLACE(misspelled_word, 'ei', 'ie') = REPLACE(@word, 'ei', 'ie');
 
-- SELECT soundex("bcak"), soundex("back");


-- WITH match_sounds AS 
-- (

-- )
-- SELECT * FROM match_sounds;

 -- Your query only needs to return the id column. Any additional 
 -- columns returned by your query will be ignored.