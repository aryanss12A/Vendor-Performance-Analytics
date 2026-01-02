# Vendor-Performance-Analytics

## Overview

This project delivers an end to end **vendor, inventory, and profitability analytics solution** using Python, SQL, and Power BI. It integrates raw transactional data, performs feature engineering and statistical analysis, and presents actionable business insights through an interactive Power BI dashboard.

The primary objective is to help retail and wholesale businesses **optimize pricing, vendor strategy, inventory turnover, and profitability**, while reducing dependency on a small set of suppliers.

---

## Business Problem

Efficient inventory and sales management are critical for sustainable profitability. Businesses often face challenges such as:

* Losses due to inefficient pricing and heavy discounting
* Excess capital locked in slow moving inventory
* Over dependence on a few vendors
* Poor visibility into vendor level profitability

This project addresses these challenges by analyzing vendor performance across purchases, sales, margins, logistics costs, and inventory turnover.

---

## Key Objectives

* Identify underperforming brands that require pricing or promotional adjustments
* Detect top vendors contributing to revenue and gross profit
* Analyze the impact of bulk purchasing on unit cost savings
* Evaluate inventory turnover to reduce holding costs
* Compare profitability models of high performing and low performing vendors
* Statistically validate differences in profit margins

---

## Tech Stack

**Programming & Analysis**

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* SQLite, SQLAlchemy

**Data Storage**

* SQLite Database

**Visualization**

* Power BI (.pbix dashboard)

**Logging & Pipelines**

* Python logging
* Modular ingestion and transformation scripts

---

## Project Architecture

```
Raw CSV Files
   ↓
Python Ingestion Pipeline
   ↓
SQLite Database (inventory.db)
   ↓
Feature Engineering & Cleaning
   ↓
Exploratory Data Analysis & Statistics
   ↓
Power BI Dashboard
```

---

## Data Pipeline

### 1. Data Ingestion

* Raw CSV files are ingested using SQLAlchemy into SQLite tables
* Automated ingestion with logging and execution time tracking

### 2. Vendor Summary Creation

* Multiple tables are merged using SQL CTEs
* Freight, purchase, and sales data are consolidated at vendor and brand level

### 3. Data Cleaning & Feature Engineering

New analytical features created:

* **GrossProfit** = TotalSalesDollars − TotalPurchaseDollars
* **ProfitMargin (%)** = GrossProfit / TotalSalesDollars
* **StockTurnover** = TotalSalesQuantity / TotalPurchaseQuantity
* **SalesToPurchaseRatio** = TotalSalesDollars / TotalPurchaseDollars

Data quality improvements:

* Removed zero and negative profit records
* Eliminated unsold inventory records for profitability analysis
* Handled missing values and datatype inconsistencies

---

## Exploratory Data Analysis Highlights

### Distribution & Outliers

* Extreme variations observed in freight costs, indicating logistics inefficiencies
* Premium products identified through high purchase and selling price outliers
* Several brands showed zero sales despite purchases, highlighting dead stock

### Correlation Insights

* Purchase price has negligible correlation with total sales and gross profit
* Strong correlation between purchase quantity and sales quantity confirms inventory flow efficiency
* Negative correlation between profit margin and sales price suggests competitive pricing pressure
* Faster stock turnover does not always translate into higher profitability

---

## Research Questions & Key Findings

### 1. Brands for Pricing or Promotion

* 198 brands identified with **low sales but high profit margins**
* Opportunity to increase volume through targeted promotions without sacrificing margin

### 2. Vendor Concentration Risk

* Top 10 vendors contribute **~65.7% of total purchases**
* Indicates over reliance on a limited supplier base

### 3. Bulk Purchasing Impact

* Large orders result in **~72% lower unit cost** compared to small orders
* Confirms effectiveness of bulk pricing strategies

### 4. Inventory Turnover Risks

* Unsold inventory capital estimated at **$2.71M**
* Slow moving stock increases holding costs and reduces cash flow efficiency

### 5. Profitability Model Comparison

* Low performing vendors show higher margins but lower sales volume
* High performing vendors rely on volume driven profitability

### 6. Statistical Validation

* Hypothesis testing confirms **significant difference in profit margins** between vendor groups
* Vendors operate under distinct profitability strategies

---

## Power BI Dashboard

The Power BI report provides:

* Vendor and brand level performance overview
* Purchase vs sales contribution analysis
* Profit margin and gross profit breakdown
* Inventory turnover monitoring
* Interactive filters for vendor, brand, and price segments

This dashboard enables quick decision making for procurement, pricing, and inventory teams.

---

## Business Recommendations

* Re evaluate pricing for low sales, high margin brands to unlock volume growth
* Diversify vendor partnerships to mitigate supply chain risk
* Leverage bulk purchasing to maintain competitive pricing
* Optimize slow moving inventory through clearance sales and revised order quantities
* Strengthen marketing and distribution for underperforming vendors

---

## How to Run the Project

1. Place raw CSV files inside the `data/` directory
2. Run the ingestion script to populate SQLite database
3. Execute vendor summary and cleaning scripts
4. Perform EDA using provided notebooks
5. Open the Power BI `.pbix` file to explore insights

---

## Skills Demonstrated

* Data modeling and SQL joins
* Feature engineering for business metrics
* Exploratory data analysis and visualization
* Statistical hypothesis testing
* End to end data pipeline design
* Business oriented analytical thinking

---

## Author

Aryan Sachdeva

Data Analyst | Python | SQL | Power BI

---

## License

This project is intended for educational and portfolio demonstration purposes.
