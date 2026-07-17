import pandas as pd

def analyze(df: pd.DataFrame) -> dict:
    summary = {}

    # Basic info
    summary["shape"] = df.shape
    summary["columns"] = list(df.columns)
    summary["dtypes"] = df.dtypes.astype(str).to_dict()

    # Missing values
    summary["missing_values"] = df.isnull().sum().to_dict()

    # Statistical summary
    summary["statistics"] = df.describe(include="all").fillna("").astype(str).to_dict()

    # Duplicate rows
    summary["duplicate_rows"] = int(df.duplicated().sum())

    return summary


def summary_to_text(summary: dict) -> str:
    text = f"""
Dataset has {summary['shape'][0]} rows and {summary['shape'][1]} columns.
Columns: {', '.join(summary['columns'])}
Duplicate rows: {summary['duplicate_rows']}

Missing Values:
{pd.Series(summary['missing_values']).to_string()}

Statistical Summary:
{pd.DataFrame(summary['statistics']).to_string()}
"""
    return text