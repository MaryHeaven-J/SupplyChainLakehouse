-- Revenue Analysis SQL Queries
-- Project: Supply Chain Lakehouse

-- 1. View Gold Layer Revenue Table

SELECT *
FROM gold_country_revenue;


-- 2. Total Company Revenue

SELECT
    SUM(Total_Revenue) AS Company_Revenue
FROM gold_country_revenue;


-- 3. Country-wise Revenue Ranking

SELECT
    Country,
    Total_Revenue,
    RANK() OVER (
        ORDER BY Total_Revenue DESC
    ) AS Revenue_Rank
FROM gold_country_revenue;


-- 4. Highest Revenue Country

SELECT
    Country,
    Total_Revenue
FROM gold_country_revenue
ORDER BY Total_Revenue DESC
LIMIT 1;


-- 5. Revenue Contribution Percentage

SELECT
    Country,
    Total_Revenue,
    ROUND(
        Total_Revenue / SUM(Total_Revenue) OVER () * 100,
        2
    ) AS Revenue_Percentage
FROM gold_country_revenue;
