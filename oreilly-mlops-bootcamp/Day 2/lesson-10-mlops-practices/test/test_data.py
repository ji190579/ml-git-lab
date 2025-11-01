
import pandas as pd


def load_data():
    columns = [
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race",
        "sex", "capital-gain", "capital-loss", "hours-per-week",
        "native-country", "income"
    ]
    df = pd.read_csv("data/adult.data", header=None, names=columns, na_values=" ?")
    return df

def test_valid_income_labels():
    df =load_data()
    df["income"] = df["income"].str.strip()  
    valid_labels = {"<=50K", ">50K"} 
    assert set(df["income"].unique()).issubset(valid_labels), "Unexpected income labels found"

def test_dataset_shape():
    df = load_data()
    expected_columns = 15
    assert df.shape[1] == expected_columns, f"Expected {expected_columns} columns but got {df.shape[1]}"
    
    # Optional: check if the number of rows is above a threshold
    assert df.shape[0] > 30000, f"Too few rows: {df.shape[0]}"
