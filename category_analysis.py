# category_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Generate Category Summary
# -------------------------------
def generate_category_summary(df):
    if 'description' not in df.columns:
        raise ValueError("Missing 'description' column for category analysis")

    df['category'] = df['description'].apply(lambda x: categorize_transaction(x))

    summary = df.groupby('category')['signed_amount'].agg(['sum', 'count']).reset_index()
    summary = summary.rename(columns={'sum': 'total_amount', 'count': 'transaction_count'})

    print("\n[Category Summary]:")
    print(summary)

    return df, summary

# -------------------------------
# Generate Pivot Table (Month x Category)
# -------------------------------
def generate_category_pivot(df):
    if 'category' not in df.columns:
        raise ValueError("Category column missing in dataframe. Run generate_category_summary() first.")

    df['month'] = df['booking_date'].dt.to_period('M')

    pivot_table = df.pivot_table(
        index='month',
        columns='category',
        values='signed_amount',
        aggfunc='sum',
        fill_value=0
    ).reset_index()

    print("\n[Pivot Table]:")
    print(pivot_table.head())

    return pivot_table

# -------------------------------
# Plot Category Trends Over Months
# -------------------------------
def plot_category_trends(pivot_df):
    if pivot_df.empty:
        print("⚠️ No data to plot category trends.")
        return

    pivot_df['month'] = pivot_df['month'].astype(str)

    plt.figure(figsize=(12,6))
    pivot_df.set_index('month').plot(kind='line', marker='o')
    plt.title('Category Trends Over Months')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -------------------------------
# Helper: Categorize Transaction
# -------------------------------
def categorize_transaction(description):
    description = str(description).lower()

    if 'salary' in description:
        return 'Salary'
    elif 'rent' in description:
        return 'Rent'
    elif 'utility' in description or 'electricity' in description:
        return 'Utilities'
    elif 'fuel' in description or 'petrol' in description:
        return 'Fuel'
    elif 'grocery' in description or 'store' in description:
        return 'Groceries'
    else:
        return 'Other'

# -------------------------------
# END OF FILE
# -------------------------------
