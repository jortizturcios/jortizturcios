# Module 10 Assignment: Data Manipulation and Cleaning with Pandas
# UrbanStyle Customer Data Cleaning

# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Welcome message
print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
from io import StringIO

# Simulated CSV content with intentional data issues
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver
"""

# Create a StringIO object (simulates a file)
customer_data_csv = StringIO(csv_content)
# ----- END OF SIMULATION CODE -----


# ─────────────────────────────────────────────────────────────
# TODO 1: Load and Explore the Dataset
# ─────────────────────────────────────────────────────────────

# 1.1 Load the dataset
raw_df = pd.read_csv(customer_data_csv)

print("\n[1.1] Dataset Shape:", raw_df.shape)
print("\n[1.1] Column dtypes:\n", raw_df.dtypes)
print("\n[1.1] First 5 rows:\n", raw_df.head())
print("\n[1.1] Dataset Info:")
raw_df.info()

# 1.2 Assess data quality
initial_missing_counts = raw_df.isnull().sum()
print("\n[1.2] Initial Missing Values:\n", initial_missing_counts)

initial_duplicate_count = raw_df.duplicated().sum()
print(f"\n[1.2] Initial Duplicate Rows: {initial_duplicate_count}")


# ─────────────────────────────────────────────────────────────
# TODO 2: Handle Missing Values
# ─────────────────────────────────────────────────────────────

# 2.1 Missing value report
missing_value_report = raw_df.isnull().sum()
missing_value_report = missing_value_report[missing_value_report > 0]
print("\n[2.1] Missing Value Report:\n", missing_value_report)

# Work on a copy
df = raw_df.copy()

# 2.2 Fill missing satisfaction_rating with median
satisfaction_median = df['satisfaction_rating'].median()
df['satisfaction_rating'] = df['satisfaction_rating'].fillna(satisfaction_median)
print(f"\n[2.2] satisfaction_rating median used: {satisfaction_median}")

# 2.3 Handle missing last_purchase dates with forward fill
date_fill_strategy = 'forward_fill'
df['last_purchase'] = df['last_purchase'].ffill()
print(f"\n[2.3] Date fill strategy: {date_fill_strategy}")

# 2.4 Handle remaining missing values
# last_name: fill with empty string (Amanda has no last name)
df['last_name'] = df['last_name'].fillna('')

# phone: fill with 'Unknown'
df['phone'] = df['phone'].fillna('Unknown')

# age: fill with median age
age_median = df['age'].median()
df['age'] = df['age'].fillna(age_median)

# loyalty_status: fill with 'Bronze' (lowest tier, safest default)
df['loyalty_status'] = df['loyalty_status'].fillna('Bronze')

df_no_missing = df.copy()
print(f"\n[2.4] Missing values after handling:\n{df_no_missing.isnull().sum()}")


# ─────────────────────────────────────────────────────────────
# TODO 3: Correct Data Types
# ─────────────────────────────────────────────────────────────

df_typed = df_no_missing.copy()

# 3.1 Convert join_date and last_purchase to datetime (handle mixed formats)
df_typed['join_date'] = pd.to_datetime(df_typed['join_date'], format='mixed', dayfirst=False)
df_typed['last_purchase'] = pd.to_datetime(df_typed['last_purchase'], format='mixed', dayfirst=False)
print("\n[3.1] Date columns converted to datetime.")

# 3.2 Convert total_spent to numeric (remove $, commas)
df_typed['total_spent'] = (
    df_typed['total_spent']
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)
print("\n[3.2] total_spent converted to float.")

# 3.3 Ensure numeric types for total_purchases and age
df_typed['total_purchases'] = pd.to_numeric(df_typed['total_purchases'], errors='coerce').fillna(0).astype(int)
df_typed['age'] = pd.to_numeric(df_typed['age'], errors='coerce').fillna(age_median).astype(int)
print("\n[3.3] total_purchases and age confirmed as numeric.")
print("\n[3.3] Updated dtypes:\n", df_typed.dtypes)


# ─────────────────────────────────────────────────────────────
# TODO 4: Clean and Standardize Text Data
# ─────────────────────────────────────────────────────────────

df_text_cleaned = df_typed.copy()

# 4.1 Standardize name case (proper/title case)
df_text_cleaned['first_name'] = df_text_cleaned['first_name'].str.title()
df_text_cleaned['last_name'] = df_text_cleaned['last_name'].str.title()
print("\n[4.1] Names standardized to title case.")

# 4.2 Standardize category names (title case)
df_text_cleaned['preferred_category'] = df_text_cleaned['preferred_category'].str.title()
print("\n[4.2] Categories standardized:", df_text_cleaned['preferred_category'].unique())

# 4.3 Standardize phone numbers to (XXX) XXX-XXXX format
phone_format = "(XXX) XXX-XXXX"

def standardize_phone(phone):
    if phone == 'Unknown':
        return 'Unknown'
    digits = re.sub(r'\D', '', str(phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return 'Unknown'

df_text_cleaned['phone'] = df_text_cleaned['phone'].apply(standardize_phone)
print(f"\n[4.3] Phone format standardized to: {phone_format}")
print(df_text_cleaned['phone'].head(10))


# ─────────────────────────────────────────────────────────────
# TODO 5: Remove Duplicates
# ─────────────────────────────────────────────────────────────

# 5.1 Identify duplicates
duplicate_count = df_text_cleaned.duplicated().sum()
print(f"\n[5.1] Duplicate records found: {duplicate_count}")

# 5.2 Remove duplicates, keeping the first occurrence
df_no_duplicates = df_text_cleaned.drop_duplicates(keep='first').reset_index(drop=True)
print(f"[5.2] Records after deduplication: {len(df_no_duplicates)}")


# ─────────────────────────────────────────────────────────────
# TODO 6: Add Derived Features
# ─────────────────────────────────────────────────────────────

# Reference date for calculations
reference_date = pd.Timestamp('2024-01-01')

# 6.1 Days since last purchase
df_no_duplicates['days_since_last_purchase'] = (
    (reference_date - df_no_duplicates['last_purchase']).dt.days
)
print("\n[6.1] days_since_last_purchase calculated.")

# 6.2 Average purchase value
df_no_duplicates['average_purchase_value'] = np.where(
    df_no_duplicates['total_purchases'] > 0,
    df_no_duplicates['total_spent'] / df_no_duplicates['total_purchases'],
    0.0
)
df_no_duplicates['average_purchase_value'] = df_no_duplicates['average_purchase_value'].round(2)
print("[6.2] average_purchase_value calculated.")

# 6.3 Purchase frequency category
def freq_category(n):
    if n >= 10:
        return 'High'
    elif n >= 5:
        return 'Medium'
    else:
        return 'Low'

df_no_duplicates['purchase_frequency_category'] = df_no_duplicates['total_purchases'].apply(freq_category)
print("[6.3] purchase_frequency_category assigned.")
print(df_no_duplicates['purchase_frequency_category'].value_counts())


# ─────────────────────────────────────────────────────────────
# TODO 7: Clean Up the DataFrame
# ─────────────────────────────────────────────────────────────

# 7.1 Rename columns
column_renames = {
    'customer_id': 'Customer ID',
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'email': 'Email',
    'phone': 'Phone',
    'join_date': 'Join Date',
    'last_purchase': 'Last Purchase Date',
    'total_purchases': 'Total Purchases',
    'total_spent': 'Total Spent ($)',
    'preferred_category': 'Preferred Category',
    'satisfaction_rating': 'Satisfaction Rating',
    'age': 'Age',
    'city': 'City',
    'state': 'State',
    'loyalty_status': 'Loyalty Status',
    'days_since_last_purchase': 'Days Since Last Purchase',
    'average_purchase_value': 'Avg Purchase Value ($)',
    'purchase_frequency_category': 'Purchase Frequency'
}
df_renamed = df_no_duplicates.rename(columns=column_renames)
print("\n[7.1] Columns renamed.")

# 7.2 No columns need to be dropped — all are meaningful for segmentation
df_final = df_renamed.copy()
print("[7.2] No unnecessary columns to remove.")

# 7.3 Sort by Total Spent descending
df_final = df_final.sort_values('Total Spent ($)', ascending=False).reset_index(drop=True)
print("[7.3] DataFrame sorted by Total Spent (descending).")


# ─────────────────────────────────────────────────────────────
# TODO 8: Generate Insights from Cleaned Data
# ─────────────────────────────────────────────────────────────

# 8.1 Average spent by loyalty status
avg_spent_by_loyalty = df_final.groupby('Loyalty Status')['Total Spent ($)'].mean().round(2)
print("\n[8.1] Avg Spent by Loyalty Status:\n", avg_spent_by_loyalty)

# 8.2 Top categories by total revenue
category_revenue = df_final.groupby('Preferred Category')['Total Spent ($)'].sum().sort_values(ascending=False)
print("\n[8.2] Revenue by Category:\n", category_revenue)

# 8.3 Correlation between satisfaction rating and total spent
satisfaction_spend_corr = df_final['Satisfaction Rating'].corr(df_final['Total Spent ($)'])
print(f"\n[8.3] Correlation (satisfaction vs total spent): {satisfaction_spend_corr:.4f}")


# ─────────────────────────────────────────────────────────────
# TODO 9: Generate Final Report
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING REPORT")
print("=" * 60)

# 9.1 Data quality issues found
total_missing = initial_missing_counts.sum()
print(f"""
Data Quality Issues:
- Missing Values: {total_missing} total missing entries
  * satisfaction_rating: {int(initial_missing_counts.get('satisfaction_rating', 0))} missing → filled with median ({satisfaction_median})
  * last_purchase: {int(initial_missing_counts.get('last_purchase', 0))} missing → forward filled
  * last_name: {int(initial_missing_counts.get('last_name', 0))} missing → filled with empty string
  * phone: {int(initial_missing_counts.get('phone', 0))} missing → filled with 'Unknown'
  * age: {int(initial_missing_counts.get('age', 0))} missing → filled with median age
  * loyalty_status: {int(initial_missing_counts.get('loyalty_status', 0))} missing → filled with 'Bronze'
- Duplicates: {initial_duplicate_count} duplicate records found and removed
- Data Type Issues: mixed date formats (YYYY-MM-DD and MM/DD/YYYY), currency symbols
  and commas in total_spent, inconsistent phone number formats
""")

# 9.2 Standardization changes
print(f"""Standardization Changes:
- Names: Converted to proper/title case (e.g., JESSICA → Jessica, jones → Jones)
- Categories: Standardized to title case (e.g., ACCESSORIES → Accessories, womenswear → Womenswear)
- Phone Numbers: Standardized to {phone_format} format using regex digit extraction
- Dates: Unified to pandas datetime objects (handled both YYYY-MM-DD and MM/DD/YYYY)
- Total Spent: Removed '$' symbols and commas, converted to float
""")

# 9.3 Business insights
top_category = category_revenue.index[0]
top_category_revenue = category_revenue.iloc[0]
total_customers = len(df_final)

print(f"""Key Business Insights:
- Customer Base: {total_customers} total customers (after deduplication)
- Revenue by Loyalty Status (avg spend):""")
for status, val in avg_spent_by_loyalty.sort_values(ascending=False).items():
    print(f"    {status}: ${val:,.2f}")
print(f"- Top Category: {top_category} with ${top_category_revenue:,.2f} total revenue")
print(f"- Satisfaction ↔ Spend Correlation: {satisfaction_spend_corr:.4f} "
      f"({'positive' if satisfaction_spend_corr > 0 else 'negative'} relationship)")

# 9.4 Final cleaned dataset preview
print("\n[9.4] Final Cleaned Dataset (first 5 rows):")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 140)
print(df_final.head())
print(f"\nFinal dataset shape: {df_final.shape}")