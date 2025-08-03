import pandas as pd
import numpy as np
from dateutil.parser import parse
import re

class DataTypeDetector:
    def __init__(self):
        pass

    def detect_column_type(self, series):
        cleaned_series = series.dropna().astype(str).str.strip()
        if cleaned_series.empty:
            return "Unknown"
        
        sample_values = cleaned_series.head(20).tolist()

        if self._is_date(sample_values):
            return "Datetime"
        elif self._is_number(sample_values):
            return "Numeric"
        elif self._is_text(sample_values):
            return "Text"
        else:
            return "Unknown"

    def _is_date(self, values):
        date_count = 0
        for val in values:
            try:
                _ = parse(val, fuzzy=False)
                date_count += 1
            except Exception:
                continue
        return date_count / len(values) >= 0.6

    def _is_number(self, values):
        num_count = 0
        for val in values:
            cleaned = val.replace(",", "").replace("(", "-").replace(")", "").replace("₹", "").replace("$", "").replace("€", "")
            cleaned = re.sub(r"[^\d\.\-KMBkmb]", "", cleaned)
            try:
                float(cleaned)
                num_count += 1
            except Exception:
                continue
        return num_count / len(values) >= 0.6

    def _is_text(self, values):
        # Consider it text if >60% of values are long strings
        text_like = [v for v in values if len(v) > 2 and not v.isdigit()]
        return len(text_like) / len(values) > 0.6
