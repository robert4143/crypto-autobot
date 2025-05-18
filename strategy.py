# strategy.py

import ccxt
import ta
import pandas as pd
from config import *

def fetch_ohlcv(exchange, symbol, timeframe='15m', limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['ema20'] = ta.trend.EMAIndicator(df['close'], window=20).ema_indicator()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    return df

def generate_signal(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    # 매수 시나리오
    if last['rsi'] < 30 and last['close'] > last['ema20'] and prev['rsi'] < last['rsi']:
        return 'buy'
    
    # 매도 시나리오
    if last['rsi'] > 70 and last['close'] < last['ema20'] and prev['rsi'] > last['rsi']:
        return 'sell'

    return None
