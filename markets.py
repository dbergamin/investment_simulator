from datetime import date
import data_source


class MarketIndex:
    # Source data for index values at a given date
    def __init__(self,
                 market_data: data_source.CSVDailyDataSource,
                 start_date: date):
        self.market_data = market_data
        self.start_date = start_date
        self.current_tick = 0
        self._setup()

    def tick(self):
        self.current_tick += 1

    def _setup(self):
        self.market_data.load_data_source()
        data = self.market_data.seek(self.start_date)
