from datetime import date
import sys
from csv import DictReader, Error as CSVError, Sniffer
from collections import OrderedDict
import errno
import os
from pathlib import Path
from typing import Dict


class CSVDailyDataSource:

    def __init__(self, path_string: str):
        self.path: Path = self._validate_path(path_string)
        self.data: Dict[date, OrderedDict] = {}

    # Load a source of daily data values
    # We need a column named 'date' with unique values
    def load_data_source(self):
        # Read the first 1024 bytes and look for a header
        has_headers = Sniffer().has_header(open(self.path).read(1024))
        if not has_headers:
            raise DataSourceFormatError("CSV does not have headers")

        with open(self.path, 'r') as csv_file:
            try:
                csv_dict_reader = DictReader(csv_file)
                for row in csv_dict_reader:
                    # Expect format YYYY-mm-dd
                    self._parse_row_and_add_to_data(row)
            except CSVError as e:
                sys.exit('file {}, line {}: {}'.format(self.path, csv_dict_reader.line_num, e))

    def seek(self, seek_date: date):
        if not self.data:
            raise DataSourceNotLoadedError("Data source not loaded or empty."
                                           "Invoke 'load_data_source' before using this data provider.")
        return self.data[seek_date]

    def _parse_row_and_add_to_data(self, row: OrderedDict):
        row_date = row['date'].split('-')
        entry_date = date(int(row_date[0]), int(row_date[1]), int(row_date[2]))
        if entry_date not in self.data:
            self.data[entry_date] = row
        else:
            raise DataSourceFormatError(f'Duplicate dates in the data source {self.path}')

    @staticmethod
    def _validate_path(path_string: str) -> Path:
        path = Path(path_string)
        if not path.exists():
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), path_string)
        else:
            return path


class DataSourceNotLoadedError(Exception):
    pass

class DataSourceFormatError(Exception):
    pass
