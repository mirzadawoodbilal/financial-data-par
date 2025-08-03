import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_basic_eda(df):
    print("\n📊 Shape of DataFrame:", df.shape)
    print("\n📋 Column Data Types:\n", df.dtypes)
    print("\n🕳️ Missing Values:\n", df.isnull().sum())
    print("\n📈 Summary Stats for Numeric Columns:\n", df.describe())

def filter_by_amount(df, threshold):
    print(f"\n[INFO] Filtering data where 'signed_amount' > {threshold}")

    if 'signed_amount' not in df.columns:
        raise ValueError("The column 'signed_amount' does not exist in the DataFrame.")

    df['signed_amount'] = pd.to_numeric(df['signed_amount'], errors='coerce')
    filtered_df = df[df['signed_amount'] > threshold]

    print(filtered_df[['booking_date', 'signed_amount']].head(10))
    return filtered_df

def visualize_data(df, filename_prefix="summary"):
    if 'booking_date' not in df.columns or 'signed_amount' not in df.columns:
        print("⚠️ Required columns missing for visualization.")
        return

    print(f"\n[INFO] Generating Monthly Summary Plot: {filename_prefix}")


    def parse_excel_date(val):
        if pd.isna(val):
            return pd.NaT
        try:
            date = pd.to_datetime(val, errors='coerce')
            if pd.notna(date):
                return date
            if isinstance(val, (int, float)):
                return pd.to_datetime('1899-12-30') + pd.to_timedelta(val, unit='D')
        except Exception as e:
            print(f"Failed to parse date {val}: {e}")
        return pd.NaT

    df['booking_date'] = df['booking_date'].apply(parse_excel_date)

    df['month'] = df['booking_date'].dt.to_period('M')
    monthly_summary = df.groupby('month')['signed_amount'].sum().reset_index()

    if monthly_summary.empty:
        print("⚠️ No data to plot.")
        return

    os.makedirs("visualizations", exist_ok=True)

    # Monthly Summary Plot
    plt.figure(figsize=(10,6))
    sns.barplot(x='month', y='signed_amount', data=monthly_summary)
    plt.title('Monthly Summary of Signed Amounts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    output_path = f"visualizations/{filename_prefix}_monthly_summary.png"
    plt.savefig(output_path)
    plt.close()
    print(f"[SAVED] Monthly Summary plot to: {output_path}")

    # Category Summary Plot (if 'category' exists)
    if 'category' in df.columns:
        category_summary = df.groupby('category')['signed_amount'].sum().reset_index()
        plt.figure(figsize=(10,6))
        sns.barplot(x='category', y='signed_amount', data=category_summary)
        plt.title('Category-wise Transaction Summary')
        plt.xticks(rotation=45)
        plt.tight_layout()
        output_path = f"visualizations/{filename_prefix}_category_summary.png"
        plt.savefig(output_path)
        plt.close()
        print(f"[SAVED] Category Summary plot to: {output_path}")
