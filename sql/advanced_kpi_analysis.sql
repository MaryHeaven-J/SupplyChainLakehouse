-- Advanced KPI Analysis
-- Project: Supply Chain Lakehouse

-- 1. View Advanced Gold KPI Table

SELECT *
FROM gold_country_kpi;


-- 2. Rank Countries by Revenue

SELECT
    Country,
    Total_Revenue,
    RANK() OVER (
        ORDER BY Total_Revenue DESC
    ) AS Revenue_Rank
FROM gold_country_kpi;


-- 3. Find Countries with High Average Order Value

SELECT
    Country,
    Average_Order_Value
FROM gold_country_kpi
WHERE Average_Order_Value > 100000;


-- 4. Revenue Contribution Percentage

SELECT
    Country,
    Total_Revenue,
    ROUND(
        Total_Revenue / SUM(Total_Revenue) OVER () * 100,
        2
    ) AS Revenue_Percentage
FROM gold_country_kpi;


-- 5. Order Volume Analysis

SELECT
    Country,
    Total_Orders
FROM gold_country_kpi
ORDER BY Total_Orders DESC;
