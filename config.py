# config.py

BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY')
BINANCE_API_SECRET = os.environ.get('BINANCE_API_SECRET')

SYMBOL = 'ETHUSDT'
LEVERAGE = 10

# 전략 설정
STOP_LOSS_PERCENT = 2.0  # 손절: -2%
TAKE_PROFIT_PERCENT = 5.0  # 익절: +5%
QUANTITY_PERCENT = 0.95  # 총 자산 대비 몇 % 진입

TIMEFRAME_SIGNAL = '15m'
TIMEFRAME_ENTRY = '1m'
