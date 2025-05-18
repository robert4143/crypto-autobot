import ccxt
import time
import threading
from flask import Flask
from config import *
from strategy import fetch_ohlcv, generate_signal

exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET,
    'enableRateLimit': True,
    'options': {'defaultType': 'future'}
})

exchange.set_leverage(LEVERAGE, SYMBOL)

def get_balance():
    balance = exchange.fetch_balance({'type': 'future'})
    usdt = balance['total']['USDT']
    return usdt

def calculate_position_size(usdt):
    return round((usdt * QUANTITY_PERCENT), 2)

def place_order(direction, price, quantity):
    if direction == 'buy':
        order = exchange.create_market_buy_order(SYMBOL, quantity)
        stop_price = price * (1 - STOP_LOSS_PERCENT / 100)
        take_price = price * (1 + TAKE_PROFIT_PERCENT / 100)
    elif direction == 'sell':
        order = exchange.create_market_sell_order(SYMBOL, quantity)
        stop_price = price * (1 + STOP_LOSS_PERCENT / 100)
        take_price = price * (1 - TAKE_PROFIT_PERCENT / 100)

    print(f"{direction.upper()} 주문 체결! 손절가: {stop_price:.2f}, 익절가: {take_price:.2f}")

def run_bot():
    while True:
        try:
            df_signal = fetch_ohlcv(exchange, SYMBOL, timeframe=TIMEFRAME_SIGNAL)
            signal = generate_signal(df_signal)

            if signal:
                df_entry = fetch_ohlcv(exchange, SYMBOL, timeframe=TIMEFRAME_ENTRY)
                entry_price = df_entry.iloc[-1]['close']
                usdt = get_balance()
                qty = calculate_position_size(usdt) / entry_price

                place_order(signal, entry_price, qty)
                print(f"{signal.upper()} 진입 at {entry_price}, 수량: {qty}")
            
            time.sleep(60)

        except Exception as e:
            print("에러 발생:", str(e))
            time.sleep(60)

# ✅ 자동매매 루프를 백그라운드에서 실행
threading.Thread(target=run_bot).start()

# ✅ Render가 포트를 감지할 수 있게 Flask 실행
app = Flask(__name__)

@app.route('/')
def index():
    return '✅ 자동매매 봇 실행 중입니다 (Render Flask)'

# ✅ 포트 반드시 열기 (10000 또는 8080 등)
app.run(host='0.0.0.0', port=10000)

