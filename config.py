import os

BINANCE_API_KEY = 'your_api_key'
BINANCE_API_SECRET = 'your_api_secret'

SYMBOL = 'ETH/USDT'  # 또는 BTC/USDT
LEVERAGE = 10
QUANTITY_PERCENT = 0.95

# ✅ 아래 2줄 추가
TIMEFRAME_SIGNAL = '15m'   # 신호 확인용 캔들 차트 주기
TIMEFRAME_ENTRY = '1m'     # 진입 가격 확인용

# 리스크 관리 설정
STOP_LOSS_PERCENT = 2      # 손절 비율 (%)
TAKE_PROFIT_PERCENT = 3    # 익절 비율 (%)
