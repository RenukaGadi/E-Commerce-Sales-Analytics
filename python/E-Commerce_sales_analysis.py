import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("ecommerce_sales_cleaned.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])


# -----------------------------
# 1. Basic Dataset Information
# -----------------------------

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# -----------------------------
# 2. Total Sales
# -----------------------------

total_sales = df["total_amount"].sum()

print("\nTotal Sales:")
print(total_sales)


# -----------------------------
# 3. Total Orders
# -----------------------------

total_orders = len(df)

print("\nTotal Orders:")
print(total_orders)


# -----------------------------
# 4. Average Order Value
# -----------------------------

average_order_value = df["total_amount"].mean()

print("\nAverage Order Value:")
print(average_order_value)


# -----------------------------
# 5. Sales by Category
# -----------------------------

category_sales = (
    df.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Category:")
print(category_sales)


# -----------------------------
# 6. Sales by Region
# -----------------------------

region_sales = (
    df.groupby("region")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Region:")
print(region_sales)


# -----------------------------
# 7. Sales by Payment Method
# -----------------------------

payment_sales = (
    df.groupby("payment_method")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Payment Method:")
print(payment_sales)


# -----------------------------
# 8. Returned Orders
# -----------------------------

returned_orders = df["returned"].value_counts()

print("\nReturned Orders:")
print(returned_orders)


# -----------------------------
# 9. Return Rate
# -----------------------------

return_rate = (df["returned"] == "Yes").mean() * 100

print("\nReturn Rate:")
print(return_rate)


# -----------------------------
# 10. Monthly Sales Trend
# -----------------------------

monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)


# -----------------------------
# 11. Top 5 Customers
# -----------------------------

top_customers = (
    df.groupby("customer_id")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Customers by Sales:")
print(top_customers)


# -----------------------------
# 12. Top 5 Products
# -----------------------------

top_products = (
    df.groupby("product_id")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products by Sales:")
print(top_products)