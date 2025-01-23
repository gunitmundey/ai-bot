import yfinance as yf
import logging

class DataFetcher:
    def __init__(self, symbol='BTC-USD'):
        self.symbol = symbol

    def fetch_historical_data(self, start_date, end_date):
        try:
            data = yf.download(self.symbol, start=start_date, end=end_date)
            logging.info(f"Fetched historical data for {self.symbol} from {start_date} to {end_date}.")
            return data
        except Exception as e:
            logging.error(f"An error occurred while fetching historical data: {e}")
            return None

    def fetch_real_time_data(self):
        try:
            data = yf.Ticker(self.symbol)
            real_time_data = data.history(period='1d')
            logging.info(f"Fetched real-time data for {self.symbol}.")
            return real_time_data
        except Exception as e:
            logging.error(f"An error occurred while fetching real-time data: {e}")
            return None