import pandas as pd

def test_data_not_empty():
    df = pd.read_csv("data/data.csv")
    assert not df.empty

def test_required_columns():
    df = pd.read_csv("data/data.csv")
    required_columns = [
        "order_id",
        "customer_name",
        "email",
        "phone",
        "amount",
        "payment_mode"
    ]
    for col in required_columns:
        assert col in df.columns

def test_no_missing_values():
    df = pd.read_csv("data/data.csv")
    assert df.isnull().sum().sum() == 0

def test_amount_positive():
    df = pd.read_csv("data/data.csv")
    assert (df["amount"] > 0).all()