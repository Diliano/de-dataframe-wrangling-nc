from src.json_data import create_df, increase_price, get_best_value
import pandas as pd


class TestCreateDf:
    def test_creates_df_from_json(self):
        # Act
        test_input = "./data/doughnuts.json"
        expected_columns = ["doughnut_type", "price", "calories", "contains_nuts"]
        # Assert
        result = create_df(test_input)
        # Act
        assert isinstance(result, pd.DataFrame)
        assert list(result.columns) == expected_columns
        assert len(result) == 10
