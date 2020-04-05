import pytest
from datetime import date

from data_source import DataSourceFormatError, DataSourceNotLoadedError


def test_load_data_source(valid_csv_daily, invalid_csv_daily):
    with pytest.raises(DataSourceFormatError):
        invalid_csv_daily.load_data_source()

    valid_csv_daily.load_data_source()


def test_seek(valid_csv_daily):
    with pytest.raises(DataSourceNotLoadedError):
        valid_csv_daily.seek(date(2019, 1, 1))

    valid_csv_daily.load_data_source()
    data = valid_csv_daily.seek(date(2019, 1, 1))
    assert data['a'] == '1'

    with pytest.raises(KeyError):
        valid_csv_daily.seek(date(2099, 1, 1))


