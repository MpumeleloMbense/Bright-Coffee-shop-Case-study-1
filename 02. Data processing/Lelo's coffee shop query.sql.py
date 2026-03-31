# Databricks notebook source
# MAGIC %sql
# MAGIC -- I want to see my table in the coding to start exploryting each column
# MAGIC SELECT *
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study
# MAGIC LIMIT 10;
# MAGIC
# MAGIC ------------------------------------------------
# MAGIC -- 1. Checking the Date Range
# MAGIC -------------------------------------------------
# MAGIC -- They started collecting the data 2023-01-01
# MAGIC SELECT MIN(transaction_date) AS min_date 
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC -- the duration of the data is 6 months
# MAGIC --  They last collected the data 2023-06-30
# MAGIC
# MAGIC SELECT MAX(transaction_date) AS latest_date 
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC -------------------------------------------------
# MAGIC -- 2. Checking the names of the different stores
# MAGIC ------------------------------------------------
# MAGIC -- we have 3 stores and their names are Lower Manhattan, Hell's Kitchen, Astoria
# MAGIC SELECT DISTINCT store_location
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC SELECT COUNT(DISTINCT store_id) AS number_of_stores
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC -------------------------------------------------
# MAGIC -- 3. Checking products sold at our stores 
# MAGIC ------------------------------------------------
# MAGIC SELECT DISTINCT product_category
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC SELECT DISTINCT product_detail
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC SELECT DISTINCT product_type
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC SELECT DISTINCT product_category AS category,
# MAGIC                 product_detail AS product_name
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC -------------------------------------------------
# MAGIC -- 1. Checking product prices
# MAGIC ------------------------------------------------
# MAGIC SELECT MIN(unit_price) As cheapest_price
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC SELECT MAX(unit_price) As expensive_price
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC ------------------------------------------------
# MAGIC SELECT 
# MAGIC COUNT(*) AS number_of_rows,
# MAGIC       COUNT(DISTINCT transaction_id) AS number_of_sales,
# MAGIC       COUNT(DISTINCT product_id) AS number_of_products,
# MAGIC       COUNT(DISTINCT store_id) AS number_of_stores
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC ------------------------------------------------
# MAGIC SELECT *
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study
# MAGIC LIMIT 10;
# MAGIC
# MAGIC SELECT 
# MAGIC       transaction_id,
# MAGIC       transaction_date,
# MAGIC       Dayname(transaction_date) AS Day_name,
# MAGIC       Monthname(transaction_date) AS Month_name,
# MAGIC       transaction_qty*unit_price AS revenue_per_tnx
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC -----------------------------------------------------
# MAGIC SELECT COUNT(*)
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study;
# MAGIC
# MAGIC
# MAGIC
# MAGIC SELECT 
# MAGIC -- Dates
# MAGIC       transaction_date AS purchase_date,
# MAGIC       Dayname(transaction_date) AS Day_name,
# MAGIC       Monthname(transaction_date) AS Month_name,
# MAGIC       Dayofmonth(transaction_date) AS day_of_month,
# MAGIC
# MAGIC       CASE 
# MAGIC             WHEN Dayname(transaction_date) IN ('Sun','Sat') THEN 'Weekend'
# MAGIC             ELSE 'Weekday'
# MAGIC       END AS day_classifiction,
# MAGIC
# MAGIC       --date_format(transaction_time, 'HH:mm:ss') AS purchase_time,
# MAGIC       CASE
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') BETWEEN '00:00:00' AND '11:59:59' THEN '01. Morning Rush'
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') BETWEEN '12:00:00' AND '16:59:59' THEN '02. Afternoon'
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') >= '17:00:00' THEN '03. Evening Rush'
# MAGIC       END AS time_buckets,
# MAGIC
# MAGIC -- Counts of IDS
# MAGIC       COUNT(DISTINCT transaction_id) AS Number_of_sales,
# MAGIC       COUNT(DISTINCT product_id) AS number_of_products,
# MAGIC       COUNT(DISTINCT store_id) AS number_of_stores,
# MAGIC -- Revenue
# MAGIC       SUM(transaction_qty*unit_price) AS revenue_per_day,
# MAGIC
# MAGIC       CASE
# MAGIC             WHEN revenue_per_day <=50 THEN '01. Low Spend'
# MAGIC             WHEN revenue_per_day BETWEEN 51 AND 100 THEN '02. Med Spend'
# MAGIC             ELSE '03. High Spend'
# MAGIC       END AS spend_bucket,
# MAGIC
# MAGIC -- Categorical columns
# MAGIC       store_location,
# MAGIC       product_category,
# MAGIC       product_detail
# MAGIC
# MAGIC FROM workspace.default.bright_coffee_shop_analysis_case_study
# MAGIC GROUP BY transaction_date,
# MAGIC          Dayname(transaction_date),
# MAGIC          Monthname(transaction_date),
# MAGIC          Dayofmonth(transaction_date),
# MAGIC
# MAGIC          CASE 
# MAGIC             WHEN Dayname(transaction_date) IN ('Sun','Sat') THEN 'Weekend'
# MAGIC             ELSE 'Weekday'
# MAGIC          END,
# MAGIC
# MAGIC          CASE
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') BETWEEN '00:00:00' AND '11:59:59' THEN '01. Morning Rush'
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') BETWEEN '12:00:00' AND '16:59:59' THEN '02. Afternoon'
# MAGIC             WHEN date_format(transaction_time, 'HH:mm:ss') >= '17:00:00' THEN '03. Evening Rush'
# MAGIC          END,
# MAGIC
# MAGIC          store_location,
# MAGIC          product_category,
# MAGIC          product_detail;
# MAGIC