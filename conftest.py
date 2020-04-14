import pytest

CSV_DAILY_VALID_TEST_FILE = "test/data_source/csv_daily_valid.csv"
CSV_DAILY_INVALID_TEST_FILE = "test/data_source/csv_daily_invalid.csv"


@pytest.fixture
def valid_csv_daily():
    from data_source import CSVDailyDataSource

    csv_data: CSVDailyDataSource = CSVDailyDataSource(CSV_DAILY_VALID_TEST_FILE)
    return csv_data


@pytest.fixture
def invalid_csv_daily():
    from data_source import CSVDailyDataSource

    csv_data: CSVDailyDataSource = CSVDailyDataSource(CSV_DAILY_INVALID_TEST_FILE)
    return csv_data


@pytest.fixture
def market_index(valid_csv_daily):
    from markets import MarketIndex
    from datetime import date

    market_index: MarketIndex = MarketIndex(valid_csv_daily, date(2019, 1, 1))
    return market_index