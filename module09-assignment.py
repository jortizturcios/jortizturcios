# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

import pandas as pd
import numpy as np
from io import StringIO

print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# ----- SIMULATED CSV DATA (DO NOT MODIFY) -----
csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No
"""

sales_data_csv = StringIO(csv_content)
# ----- END OF SIMULATION CODE -----


# ============================================================
# TODO 1: Load and Explore the Dataset
# ============================================================

# 1.1 Load the dataset
sales_df = pd.read_csv(sales_data_csv)

# 1.2 Display first 5 rows
print("\nFirst 5 rows:")
print(sales_df.head())

# 1.3 Basic info
print("\nDataFrame Info:")
sales_df.info()

# 1.4 Dimensions
print(f"\nDimensions: {sales_df.shape[0]} rows x {sales_df.shape[1]} columns")

# 1.5 Summary statistics
print("\nSummary Statistics:")
print(sales_df.describe())


# ============================================================
# TODO 2: Column Selection and Basic Analysis
# ============================================================

# 2.1 Select Product, Units, Total_Sales columns
print("\nProduct / Units / Total_Sales:")
print(sales_df[['Product', 'Units', 'Total_Sales']])

# 2.2 Total units sold
total_units = sales_df['Units'].sum()
print(f"\nTotal Units Sold: {total_units}")

# 2.3 Total revenue
total_revenue = sales_df['Total_Sales'].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

# 2.4 Average unit price
avg_unit_price = sales_df['Unit_Price'].mean()
print(f"Average Unit Price: ${avg_unit_price:.2f}")


# ============================================================
# TODO 3: Row Selection and Filtering
# ============================================================

# 3.1 North America sales only
na_sales = sales_df[sales_df['Region'] == 'North America']
print(f"\nNorth America Sales ({len(na_sales)} records):")
print(na_sales)

# 3.2 High volume sales (Units > 20)
high_volume_sales = sales_df[sales_df['Units'] > 20]
print(f"\nHigh Volume Sales - Units > 20 ({len(high_volume_sales)} records):")
print(high_volume_sales)

# 3.3 PhoneX products on promotion
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')]
print(f"\nPhoneX on Promotion ({len(phonex_promo)} records):")
print(phonex_promo)

# 3.4 February 2024 sales
feb_sales = sales_df[sales_df['Date'].str.startswith('2024-02')]
print(f"\nFebruary 2024 Sales ({len(feb_sales)} records):")
print(feb_sales)


# ============================================================
# TODO 4: Advanced Filtering and Analysis
# ============================================================

# 4.1 Product with highest total sales
best_product = sales_df.groupby('Product')['Total_Sales'].sum().idxmax()
print(f"\nBest Performing Product: {best_product}")

# 4.2 Total sales by region (descending)
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(sales_by_region)

# 4.3 Average units sold per category
avg_units_by_category = sales_df.groupby('Category')['Units'].mean()
print("\nAverage Units by Category:")
print(avg_units_by_category)

# 4.4 Promotion effectiveness comparison
promo_df = sales_df[sales_df['Promotion'] == 'Yes']
no_promo_df = sales_df[sales_df['Promotion'] == 'No']

promo_comparison = {
    'promo_avg_sales':        promo_df['Total_Sales'].mean(),
    'no_promo_avg_sales':     no_promo_df['Total_Sales'].mean(),
    'promo_total_revenue':    promo_df['Total_Sales'].sum(),
    'no_promo_total_revenue': no_promo_df['Total_Sales'].sum()
}
print("\nPromotion Comparison:")
for k, v in promo_comparison.items():
    print(f"  {k}: ${v:,.2f}")


# ============================================================
# TODO 5: Missing Value Detection and Reporting
# ============================================================

# 5.1 Missing value counts per column
missing_counts = sales_df.isnull().sum()
print("\nMissing Value Counts:")
print(missing_counts)

# 5.2 Missing value percentages per column
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100
print("\nMissing Value Percentages:")
print(missing_percentages)


# ============================================================
# TODO 6: Insights and Business Analysis
# ============================================================

# 6.1 Top-performing category in each region (by total sales)
top_categories_by_region = (
    sales_df.groupby(['Region', 'Category'])['Total_Sales']
    .sum()
    .groupby(level='Region')
    .idxmax()
    .apply(lambda x: x[1])  # extract category name from (Region, Category) tuple
)
print("\nTop Category by Region:")
print(top_categories_by_region)

# 6.2 Average unit price per product category
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean()
print("\nAverage Unit Price by Category:")
print(avg_price_by_category)

# 6.3 Revenue and percentage of overall sales per product
product_revenue = sales_df.groupby('Product')['Total_Sales'].sum()
product_revenue_analysis = pd.DataFrame({
    'total_revenue': product_revenue,
    'percentage': (product_revenue / total_revenue) * 100
})
product_revenue_analysis = product_revenue_analysis.sort_values('total_revenue', ascending=False)
print("\nProduct Revenue Analysis:")
print(product_revenue_analysis)


# ============================================================
# TODO 7: Generate Analysis Report
# ============================================================

print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Overall sales performance
avg_sale_value = total_revenue / len(sales_df)
print("\nOverall Performance:")
print(f"  - Total Revenue: ${total_revenue:,.2f}")
print(f"  - Total Units Sold: {int(total_units)}")
print(f"  - Average Sale Value: ${avg_sale_value:,.2f}")

# 7.2 Regional performance
print("\nRegional Performance:")
for region, revenue in sales_by_region.items():
    print(f"  {region}: ${revenue:,.2f}")

# 7.3 Category performance
print("\nCategory Performance:")
for category in avg_units_by_category.index:
    avg_units = avg_units_by_category[category]
    avg_price = avg_price_by_category[category]
    print(f"  {category}: Avg Units: {avg_units:.1f}, Avg Price: ${avg_price:.2f}")

# 7.4 Promotion effectiveness
print("\nPromotion Effectiveness:")
print(f"  - Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:,.2f}")
print(f"  - Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:,.2f}")
print(f"  - Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}")

# 7.5 Data quality report
cols_with_missing = missing_counts[missing_counts > 0].index.tolist()
total_missing = missing_counts.sum()
print("\nData Quality Report:")
print(f"  - Missing Values Found: {cols_with_missing}")
print(f"  - Total Missing Entries: {total_missing}")

# 7.6 Business recommendations
print("\nKEY BUSINESS RECOMMENDATIONS:")
print("""
1. PRIORITIZE HIGH-MARGIN SMARTPHONE PROMOTIONS IN NORTH AMERICA
   North America is the top revenue region and PhoneX drives the highest per-product
   revenue. Targeted promotions on PhoneX in NA (currently underused) could lift
   revenue further, as promoted PhoneX units already show strong conversion in
   Latin America and Europe.

2. ADDRESS MISSING PRICE DATA TO PREVENT REVENUE LEAKAGE
   Two records are missing Unit_Price values (Latin America PhoneX and PhoneCase),
   which could indicate POS/data-entry failures. Auditing and correcting pricing
   data ensures accurate revenue reporting and prevents undercharging customers.

3. EXPAND ACCESSORY PROMOTIONS — HIGH VOLUME, UNDERUTILIZED CHANNEL
   Accessories (PhoneCase, ChargingCable) consistently sell in the highest unit
   volumes (35–60 units per transaction) but are rarely promoted. A bundling
   strategy pairing accessories with promoted Smartphones or Computers could
   increase basket size and overall attachment rate.
""")