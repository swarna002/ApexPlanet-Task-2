USE apexplanet_task2;

SELECT
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data;

SELECT
    Product,
    SUM(Quantity) AS Total_Quantity_Sold
FROM sales_data
GROUP BY Product
ORDER BY Total_Quantity_Sold DESC;

SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS Category_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Category_Revenue DESC;

SELECT
    City,
    ROUND(SUM(Total_Sales), 2) AS City_Revenue
FROM sales_data
GROUP BY City
ORDER BY City_Revenue DESC;

SELECT
    Gender,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data
GROUP BY Gender
ORDER BY Total_Revenue DESC;

SELECT
    MONTHNAME(STR_TO_DATE(Order_Date, '%Y-%m-%d')) AS Sales_Month,
    MONTH(STR_TO_DATE(Order_Date, '%Y-%m-%d')) AS Month_Number,
    ROUND(SUM(Total_Sales), 2) AS Monthly_Revenue
FROM sales_data
GROUP BY Month_Number, Sales_Month
ORDER BY Month_Number;

SELECT
    Customer_ID,
    Customer_Name,
    ROUND(SUM(Total_Sales), 2) AS Total_Purchase
FROM sales_data
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Purchase DESC
LIMIT 5;
