import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 또는 Render 환경 변수 로드

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')

SYMBOL = os.getenv('SYMBOL', 'ETH/USDT')
LEVERAGE = int(os.getenv('LEVERAGE', 10))
QUANTITY_PERCENT = float(os.getenv('QUANTITY_PERCENT', 0.95))

TIMEFRAME_SIGNAL = os.getenv('TIMEFRAME_SIGNAL', '15m')
TIMEFRAME_ENTRY = os.getenv('TIMEFRAME_ENTRY', '1m')

STOP_LOSS_PERCENT = float(os.getenv('STOP_LOSS_PERCENT', 2))
TAKE_PROFIT_PERCENT = float(os.getenv('TAKE_PROFIT_PERCENT', 3))
