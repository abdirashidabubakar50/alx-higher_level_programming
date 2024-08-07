--  script that converts hbtn_0c_0 database to UTF8


-- Switch to the correct database
USE hbtn_0c_0;

-- Convert the table character set and collation
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8
COLLATE utf8_unicode_ci;

-- Convert the column character set and collation (only specify COLLATE to avoid redundancy)
ALTER TABLE first_table
MODIFY name VARCHAR(256)
COLLATE utf8_unicode_ci;
