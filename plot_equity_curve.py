import pandas as pd
import plotly.graph_objects as go
import json

# Load the backtest results
with open('test_files/example1.json', 'r') as f:
    results = json.load(f)

## Extract the strategy name dynamically
strategy_name = list(results['strategy'].keys())[0]
trades = pd.DataFrame(results['strategy'][strategy_name]['trades'])

# Convert trade dates to datetime
trades['open_date'] = pd.to_datetime(trades['open_date'])
trades['close_date'] = pd.to_datetime(trades['close_date'])

# Calculate the equity curve
trades['profit'] = trades['profit_abs'].cumsum()
trades['date'] = trades['close_date']

# Aggregate the equity curve by day
daily_equity = trades.resample('D', on='date').last().ffill()

# Extract OHLC price data from the trades
price_data = []
for trade in results['strategy'][strategy_name]['trades']:
    price_data.append({
        'date': trade['open_date'],
        'open': trade['open_rate'],
        'high': trade['max_rate'],
        'low': trade['min_rate'],
        'close': trade['close_rate']
    })

price_df = pd.DataFrame(price_data)
price_df['date'] = pd.to_datetime(price_df['date'])

# Ensure that the date ranges in price_df and daily_equity match
min_date = min(price_df['date'].min(), daily_equity.index.min())
max_date = max(price_df['date'].max(), daily_equity.index.max())

price_df = price_df[(price_df['date'] >= min_date) & (price_df['date'] <= max_date)]
daily_equity = daily_equity[(daily_equity.index >= min_date) & (daily_equity.index <= max_date)]

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=price_df['date'],
                                     open=price_df['open'],
                                     high=price_df['high'],
                                     low=price_df['low'],
                                     close=price_df['close'],
                                     name='Price')])

# Add daily equity curve to the plot
fig.add_trace(go.Scatter(x=daily_equity.index, y=daily_equity['profit'], mode='lines', name='Equity Curve'))

# Update layout
fig.update_layout(title='Daily Performance with Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price / Equity',
                  xaxis_rangeslider_visible=False)

# Show the plot
fig.show()