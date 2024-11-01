from src.json_data import create_df, increase_price, get_best_value
import pandas as pd


class TestCreateDf:
    def test_creates_df_from_json(self):
        # Arrange
        test_input = "./data/doughnuts.json"
        expected_columns = ["doughnut_type", "price", "calories", "contains_nuts"]
        # Act
        result = create_df(test_input)
        # Assert
        assert isinstance(result, pd.DataFrame)
        assert list(result.columns) == expected_columns
        assert len(result) == 10


class TestIncreasePrice:
    def test_increases_price_by_given_percentage(self):
        # Arrange
        test_df = create_df("./data/doughnuts.json")
        test_percentage = 10
        expected_prices = list(test_df["price"] * 1.10)
        # Act
        result = increase_price(test_df, test_percentage)
        # Assert
        assert list(result["price"]) == expected_prices
