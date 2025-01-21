import pytest
from flexkey.dataframe import DataFrame

def test_dataframe_aliasing():
    data = {
        'Age Group': [25, 30, 45],
        'Name': ['Alice', 'Bob', 'Charlie']
    }
    df = DataFrame(data)

    # all these variants should return the same column
    test_keys = [
        'Age Group',
        'age group',
        'age-group',
        'age_group',
        'AGE_GROUP',
        'AgeGroup',
        'ageGroup',
        'AGE.GROUP',
    ]
    for key in test_keys:
        col = df[key]
        assert list(col) == [25, 30, 45], f"df[{key!r}] did not match"
# cast from pd.DataFrame to DataFrame
def test_cast():
    import pandas as pd


if __name__ == "__main__":
    pytest.main([__file__])
