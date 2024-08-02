--  script that converts hbtn_0c_0 database to UTF8

-- converting  database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;


USE hbtn_0c_0

-- convert the table character set and collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- convert the column character set and collation
ALTER TABLE first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;