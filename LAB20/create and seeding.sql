CREATE DATABASE lab20_mysql;
USE lab20_mysql;
SHOW TABLES;
CREATE TABLE CARS (
Car_Table_ID int,
Car_VIN VARCHAR (20),
Manufacturer VARCHAR(100), 
Model VARCHAR(100), 
Year int, 
Color VARCHAR(20));
DROP TABLE CARS;
SHOW TABLES;

CREATE TABLE SALESPERSONS (
Salespersons_Table_ID int,
Staff_ID char(10), 
Salesperson_Name VARCHAR(100), 
Store CHAR(10));
 
ALTER TABLE SALESPERSON
ADD Salesperson_Name VARCHAR(100);
ALTER TABLE SALESPERSON
DROP COLUMN Name;

ALTER TABLE SALESPERSON change Sales_person Salesperson_Name VARCHAR(100) ; 

DESCRIBE SALESPERSONS;

CREATE TABLE CUSTOMERS (
Customers_TABLE_ID int,
Customer_ID char(10), 
Customer_Name VARCHAR(100), 
Phone_Nb int,
Email VARCHAR(30), 
City VARCHAR(100), 
State_Province VARCHAR(100),
Country VARCHAR (100),
Zip_Postal_Code int);

DROP TABLE INVOICE;

CREATE TABLE INVOICE (
Invoice_TABLE_ID int,
Invoice_Number char(10), 
Invoice_Date char(10),
Car_ID char(10),
Customer_ID char(10),
Staff_ID char(10));

INSERT INTO CARS (Car_TABLE_ID, Car_VIN, Manufacturer, Model,Year,Color) VALUES(0,'3K096I98581DHSNUP','Volkswagen','Tiguan',2019,'Blue');
INSERT INTO CARS (Car_TABLE_ID, Car_VIN, Manufacturer, Model,Year,Color) VALUES(1,'ZM8G7BEUQZ97IH46V','Peugeot','Rifter',2019,'Red');
INSERT INTO CARS (Car_TABLE_ID, Car_VIN, Manufacturer, Model,Year,Color) VALUES(2,'RKXVNNIHLVVZOUB4M','Ford','Fusion',2018,'White');
INSERT INTO CARS (Car_TABLE_ID, Car_VIN, Manufacturer, Model,Year,Color) VALUES(3,'HKNDGS7CU31E9Z7JW','Toyota','RAV4',2018,'Silver');

INSERT INTO CUSTOMERS (Customers_TABLE_ID,Customer_ID, Customer_Name, Phone_Nb, Email, City, State_Province, Country,Zip_Postal_Code) 
VALUES (0,'10001','Pablo Picasso',0034636176382,'NULL','Paseo de la Chopera 14','Madrid','Madrid', 'Spain',28045);

INSERT INTO SALESPERSONS (Salespersons_Table_ID,Staff_ID,Salesperson_Name,Store) VALUES (0,'00001','Petey Cruiser','Madrid');

INSERT INTO INVOICE (Invoice_TABLE_ID, Invoice_Number, Invoice_Date,Car_ID,Customer_ID,Staff_ID) VALUES (0,'852399038','22082018',0,3);