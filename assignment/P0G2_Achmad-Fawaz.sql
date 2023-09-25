-- Creating Database
DROP DATABASE IF EXISTS assignment22;
CREATE DATABASE IF NOT EXISTS assignment22;
USE assignment22;

BEGIN;
-- Creating ONLY table, not including importing the data from CSV
DROP TABLE IF EXISTS financial_filtered;
CREATE TABLE IF NOT EXISTS financial_filtered (
	id int NOT NULL AUTO_INCREMENT primary key,
    Segment VARCHAR(255),
    Country VARCHAR(255),
    Product VARCHAR(255),
    Discount_Band VARCHAR(255),
    Units_Sold FLOAT,
    Manufacturing_Price FLOAT,
    Sale_Price FLOAT,
    Gross_Sales FLOAT,
    Discounts FLOAT,
    Sales FLOAT,
    COGS FLOAT,
    Profit FLOAT,
    Date DATETIME,
    Use_Currency VARCHAR(255)
);

-- Creating 2 User, 1 admin and 1 normal user
CREATE USER 'admin_acc'@'LOCALHOST'
IDENTIFIED BY 'admin_acc_pass';
GRANT ALL PRIVILEGES ON assignment22.*
TO 'admin_acc'@'LOCALHOST';

CREATE USER 'user_acc'@'LOCALHOST'
IDENTIFIED BY 'user_acc_pass';
GRANT SELECT on
assignment22.* TO
'user_acc'@'LOCALHOST';

FLUSH privileges;
COMMIT;