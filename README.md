# E-Commerce Sales Analytics

## Project Overview

This project analyzes e-commerce sales transaction data to identify sales trends, customer behavior, product performance, payment preferences, and return patterns.

The project was developed as an end-to-end Data Analytics project using:

**Excel → Python (Pandas) → SQL → Power BI**

## Dataset

The dataset contains **34,500 e-commerce transactions** with 17 columns.

### Main Columns

- Order ID
- Customer ID
- Product ID
- Category
- Price
- Discount
- Quantity
- Payment Method
- Order Date
- Delivery Time
- Region
- Returned
- Total Amount
- Shipping Cost
- Profit Margin
- Customer Age
- Customer Gender

## Tools Used

- **Microsoft Excel** – Data analysis and dashboard
- **Python / Pandas** – Data cleaning and analysis
- **MonetDB SQL** – SQL-based analysis
- **Power BI** – Interactive dashboard
- **GitHub** – Project documentation and version control

## Project Workflow

### 1. Excel

Created an initial sales dashboard containing:

- Total Sales
- Total Orders
- Average Order Value
- Returned Orders
- Category-wise Sales
- Region-wise Sales
- Payment Method-wise Sales
- Monthly Sales Trend
- Return Analysis

### 2. Python

Used Pandas for data cleaning and exploratory analysis.

Tasks performed:

- Loaded the dataset
- Converted order dates to datetime format
- Checked dataset shape and columns
- Checked missing values
- Checked duplicate records
- Calculated total sales
- Calculated average order value
- Analyzed category and regional sales
- Analyzed payment methods
- Calculated return rate
- Analyzed monthly sales
- Identified top customers and products

### 3. SQL

Used MonetDB to perform SQL analysis.

Queries included:

- Total Sales
- Total Orders
- Average Order Value
- Sales by Category
- Sales by Region
- Sales by Payment Method
- Returned vs Non-returned Orders
- Return Rate
- Monthly Sales Trend
- Top 5 Customers
- Top 5 Products

### 4. Power BI

Created an interactive **E-Commerce Sales Analytics Dashboard**.

Dashboard includes:

- Total Sales – **5.87M**
- Total Orders – **34.5K**
- Average Order Value – **170.01**
- Returned Orders – **1.903K**
- Sales by Category
- Sales by Region
- Sales by Payment Method
- Top 5 Customers by Sales
- Sales by Return Status
- Monthly Sales Trend
- Yearly Sales Trend

## Key Insights

- **Electronics** generated the highest sales among categories.
- **Grocery** generated the lowest sales among categories.
- **South** was the highest-performing region.
- **Central** had the lowest sales among regions.
- **Credit Card** was the highest-sales payment method.
- There were **1,903 returned orders**.
- The overall return rate was approximately **5.52%**.
- Total sales were approximately **5.87 million**.

## Project Structure

```text
E-Commerce-Sales-Analytics
│
├── Data
│   └── ecommerce_sales_cleaned.csv
│
├── Excel
│   └── E-Commerce-Sales-Dashboard.xlsx
│
├── Python
│   └── ecommerce_sales_analysis.py
│
├── SQL
│   └── ecommerce_sales_analysis.sql
│
├── PowerBI
│   └── E-Commerce-Sales-Dashboard.pbix
│
└── README.md
