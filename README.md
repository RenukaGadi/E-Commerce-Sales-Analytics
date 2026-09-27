# E-Commerce Sales Analytics

## Project Overview

This project analyzes e-commerce transaction data to understand sales performance, customer behavior, product performance, payment preferences, regional sales, and return patterns.

The project follows an end-to-end Data Analytics workflow:

**Excel → Python (Pandas/Jupyter) → SQL → Power BI**

## Dataset

The dataset contains **34,500 e-commerce transactions** with **17 columns**.

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
- **Python / Pandas / Jupyter Notebook** – Data cleaning and exploratory analysis
- **MonetDB SQL** – SQL-based business analysis
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

### 2. Python / Jupyter Notebook

Used Python and Pandas for data cleaning and exploratory data analysis.

Tasks performed:

- Loaded the dataset
- Converted order dates to datetime format
- Checked dataset shape and columns
- Checked missing values
- Checked duplicate records
- Calculated total sales
- Calculated total orders
- Calculated average order value
- Analyzed sales by category
- Analyzed sales by region
- Analyzed payment methods
- Calculated return rate
- Analyzed monthly sales
- Identified top customers
- Identified top products

The Jupyter Notebook contains the Python analysis along with the generated outputs and results.

### 3. SQL

Used MonetDB SQL to perform business analysis.

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

The dashboard includes:

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
- **South** had the highest sales among regions.
- **Central** had the lowest sales among regions.
- **Credit Card** generated the highest sales among payment methods.
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
│   ├── ecommerce_sales_analysis.py
│   └── ecommerce_sales_analysis.ipynb
│
├── SQL
│   └── ecommerce_sales_analysis.sql
│
├── PowerBI
│   └── E-Commerce-Sales-Dashboard.pbix
│
├── dashboard.png
└── README.md
