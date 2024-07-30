-- A script  that lists all records with score >= 10 of the table second_table of the database hbtn_0c_0


-- listing all records with score >= 10 in the table second_table in descending order
SELECT score, name
FROM second_table
WHERE score >= 10 ORDER BY score DESC;
