import pytest
from datetime import date

from data_source import DataSourceFormatError, DataSourceNotLoadedError


def test_load_data_source(valid_csv_daily, invalid_csv_daily):
    # Invalid case - load a CSV that is missing data or poorly formatted
    with pytest.raises(DataSourceFormatError):
        invalid_csv_daily.load_data_source()

    # Valid case - load a valid CSV
    valid_csv_daily.load_data_source()


def test_seek(valid_csv_daily):
    # Invalid case - try and seek before 'loading' the data source
    with pytest.raises(DataSourceNotLoadedError):
        valid_csv_daily.seek(date(2019, 1, 1))

    # Valid case - seek a date that exists from a loaded data source
    valid_csv_daily.load_data_source()
    data = valid_csv_daily.seek(date(2019, 1, 1))
    assert data['a'] == '1'

    # Invalid case - seek a non-existent date from a loaded data source
    with pytest.raises(KeyError):
        valid_csv_daily.seek(date(2099, 1, 1))


