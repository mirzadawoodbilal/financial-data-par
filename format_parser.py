import pandas as pd
import re
from dateutil import parser

class FormatParser:
    def __init__(self):
        pass

    def clean_text_columns(self, df):
        """
        Strips whitespace and converts all text columns to lowercase
        """
        for col in df.select_dtypes(include='object').columns:
            try:
                df[col] = df[col].astype(str).str.strip().str.lower()
            except Exception as e:
                print(f"⚠️ Skipping column '{col}' due to error: {e}")
        return df

    def clean_amount_column(self, df, amount_col):
        """
        Removes currency symbols, commas, and converts amount column to float
        """
        df[amount_col] = df[amount_col].astype(str).str.replace(r'[^\d.-]', '', regex=True)
        df[amount_col] = pd.to_numeric(df[amount_col], errors='coerce')
        return df

    def standardize_dates(self, df, date_col):
        """
        Converts all recognized date strings to standard yyyy-mm-dd format
        """
        def parse_date(val):
            try:
                return parser.parse(val).date()
            except:
                return pd.NaT

        df[date_col] = df[date_col].apply(parse_date)
        return df

    def clean_dataframe(self, df, amount_col=None, date_col=None):
        """
        Apply all cleaning functions: text, amount, and date normalization
        """
        df = self.clean_text_columns(df)
        if amount_col and amount_col in df.columns:
            df = self.clean_amount_column(df, amount_col)
        if date_col and date_col in df.columns:
            df = self.standardize_dates(df, date_col)
        return df