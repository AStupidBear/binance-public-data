from datetime import *

YEARS = ['2019', '2020', '2021']
INTERVALS = ["1m"]
DAILY_INTERVALS = ["1m"]
MONTHS = list(range(1,13))
MAX_DAYS = 35
BASE_URL = 'https://data.binance.vision/'
START_DATE = date(int(YEARS[0]), MONTHS[0], 1)
END_DATE = datetime.date(datetime.now())