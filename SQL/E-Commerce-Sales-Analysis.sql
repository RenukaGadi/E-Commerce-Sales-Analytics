-- E-Commerce Sales Analytics
-- SQL Analysis Queries

-- 1. Total Sales
SELECT SUM(total_amount) AS total_sales
FROM ecommerce_sales;


-- 2. Total Orders
SELECT COUNT(*) AS total_orders
FROM ecommerce_sales;


-- 3. Average Order Value
SELECT AVG(total_amount) AS average_order_value
FROM ecommerce_sales;


-- 4. Sales by Category
SELECT
    category,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY category
ORDER BY total_sales DESC;


-- 5. Sales by Region
SELECT
    region,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY region
ORDER BY total_sales DESC;


-- 6. Sales by Payment Method
SELECT
    payment_method,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY payment_method
ORDER BY total_sales DESC;


-- 7. Returned vs Non-returned Orders
SELECT
    returned,
    COUNT(*) AS order_count
FROM ecommerce_sales
GROUP BY returned
ORDER BY order_count DESC;


-- 8. Return Rate
SELECT
    COUNT(CASE WHEN returned = 'Yes' THEN 1 END) * 100.0 / COUNT(*) AS return_rate
FROM ecommerce_sales;


-- 9. Monthly Sales Trend
SELECT
    date_trunc('month', order_date) AS sales_month,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY date_trunc('month', order_date)
ORDER BY sales_month;


-- 10. Top 5 Customers by Sales
SELECT
    customer_id,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY customer_id
ORDER BY total_sales DESC
LIMIT 5;


-- 11. Top 5 Products by Sales
SELECT
    product_id,
    SUM(total_amount) AS total_sales
FROM ecommerce_sales
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;