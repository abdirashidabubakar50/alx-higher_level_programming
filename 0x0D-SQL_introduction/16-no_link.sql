-- script that  lists all records of the table second_table

-- listing all records of the second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;