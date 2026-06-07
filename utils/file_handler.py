import pandas as pd
import json


def load_csv(file_path):
    try:
        df = pd.read_csv(file_path, dtype=str)
        df.fillna("", inplace=True)

        # Clean spaces
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()

        return df.to_dict("records")

    except Exception as e:
        print(f"CSV Load Error: {e}")
        return []


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:
        print(f"JSON Load Error: {e}")
        return []