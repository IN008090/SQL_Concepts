Note_database_001
CREATE TABLE retent(
returned VARCHAR(35),
order_Id VARCHAR(35)
);

SELECT*FROM retent;

------------------------------------------------------------------------------
PowerBi_dataset
CREATE TABLE people(
person VARCHAR(30),
region VARCHAR(30)
);

SELECT*FROM person;
-------------------------------------------------------------------------
CREATE TABLE reads(
Order_ID VARCHAR(255),	
Order_Date DATE,	
Ship_Date DATE,	
Ship_Mode VARCHAR(255),	
Customer_ID VARCHAR(255),
Customer_Name VARCHAR(255),
Segment	VARCHAR(255),
Country	VARCHAR(255),
City VARCHAR(255),
State VARCHAR(255),
Postal_Code INT,	
Region VARCHAR(255),
Product_ID VARCHAR(255),
Category VARCHAR(255),	
Sub_Category VARCHAR(255),
Product_Name VARCHAR(255),
Sales FLOAT,	
Quantity INT,	
Discount FLOAT,	
Profit FLOAT
);
SELECT*FROM reads;
---------------------------------------------------------------------------
CREATE TABLE stock(
serial_no INT,
machine_learning VARCHAR(30),	
academic_engineering VARCHAR(30),	
minilism_frugality VARCHAR(30),
dink VARCHAR(30),
status VARCHAR(30)
);
SELECT*FROM stock;

\COPY orders FROM 'C:\Users\Joshi's.DESKTOP-JTVUBQS\OneDrive\Desktop\.ipynb_checkpoints\orders.csv' DELIMITER ',' CSV HEADER;
\COPY orders FROM 'C:\orders.csv' DELIMITER ',' CSV HEADER;
-------------------------------------------------------------------------
Sample_sales_data
CREATE TABLE sales_report(
Region	VARCHAR(100),
Country	VARCHAR(100),
Item_Type VARCHAR(100),
Sales_Channel VARCHAR(100),
Order_Priority	VARCHAR(100),
Order_Date DATE,
Order_ID INT,	
Ship_Date DATE,	
Units_Sold INT,	
Unit_Price FLOAT,	
Unit_Cost FLOAT,	
Total_Revenue FLOAT,
Total_Cost FLOAT,
Total_Profit FLOAT
);
SELECT*FROM sales_report;
-----------------------------------------------------------------------------
Sample_student_data
CREATE TABLE student_data(
student_name VARCHAR(60),
school_name VARCHAR(60),
address_city VARCHAR(60),
city VARCHAR(60),	
country	VARCHAR(60),
postal	VARCHAR(60),
phone	INT,
email VARCHAR(60)
);
SELECT*FROM student_data;
-----------------------------------------------------------------------------
PRACTISE_SET1
CREATE TABLE orders(
Order_ID VARCHAR(256),
Order_Date DATE,
Ship_Date  DATE,
Ship_Mode VARCHAR(256),
Customer_ID VARCHAR(256),
Customer_Name	VARCHAR(256),
Segment  VARCHAR(256),
Country  VARCHAR(256),
City	VARCHAR(256),
State	VARCHAR(256),
Postal_Code	INT,
Region	VARCHAR(256),
Product_ID	VARCHAR(256),
Category	VARCHAR(256),
Sub-Category	VARCHAR(256),
Product_Name	VARCHAR(256),
Sales	FLOAT,
Quantity INT,	
Discount  FLOAT,	
Profit  FLOAT
);
-----------------------------------------------------------------------------------------
CREATE TABLE people(
Order_ID VARCHAR(260),
Order_Date DATE,	
Ship_Date  DATE,	
Ship_Mode VARCHAR(260),	
Customer_ID VARCHAR(260),		
Customer_Name VARCHAR(260),	
Segment	VARCHAR(260),	
Country	VARCHAR(260),
City VARCHAR(260),	
State	VARCHAR(260),
Postal_Code	INT,
Region	VARCHAR(260),
Product_ID	VARCHAR(260),
Category VARCHAR(260),	
Sub_Category	VARCHAR(260),
Product_Name	VARCHAR(260),
Sales	FLOAT,
Quantity INT,
Discount FLOAT,	
Profit FLOAT,
);
SELECT*FROM people;
