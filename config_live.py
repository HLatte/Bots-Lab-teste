# Name of the file (without .py extension!) that contains the bot
bot_name = 'bots.bot_template'

# Datasource is poloniex or cryptocompare
datasource = 'cryptocompare'

revenyou_api_url = 'https://youhexpaper.revenyou.io/api/signal/v1/signal'

# Data settings real time data poloniex
data_settings_poloniex = {
    'pair': 'BTC_ETH',  # Use ETH pricing data on the BTC market
    'bot_function_interval': 5000, # the bot function is called every 5000 miliseconds (5 seconds)
    'max_length_ticker_data_array': 10, # the bot function receives a maximum of 20 ticker data at a time (the most recent ones)
    'currency_pair_id': 148 # id of BTC_ETH, see https://docs.poloniex.com/?shell#currencies
}

# Data settings real time data cryptocompare
data_settings_cryptocompare = {
    'pair': ['2~Coinbase~BTC~USD'],  # Use Ticker USD pricing data on the BTC market, see https://min-api.cryptocompare.com/documentation/websockets
    'max_length_ticker_data_array': 12, # the bot function receives a maximum of 20 ticker data at a time (the most recent ones)
    'bot_function_interval': 5000, # the bot function is called every 1800 seconds (half an hour)
    'api_key': 'a19cbe2b932ffe8e1b74e29daa146c50608f19767a624d9de685744bff9afd72' # for authentication, see https://www.cryptocompare.com/coins/guides/how-to-use-our-api/
}

# Data settings real time data binance
data_settings_binance = {
    'pair': 'ETHBTC',  # Use ETH pricing data on the BTC market
    'max_length_ticker_data_array': 15, # the bot function receives a maximum of 20 ticker data at a time (the most recent ones)
    'bot_function_interval': 5000 # the bot function is called every 5000 miliseconds (5 seconds)
}

buy_signal_settings = {
    'signal_provider': 'RSIBOT 2',
    'signal_provider_key': 'kyyxrhI2EWLOK2Bj',
    'exchange': datasource,
    'symbol': 'ETHBTC', # Must be in line with the data settings object pair value!  
    'price_limit': '100', # Buy BTC with a price limit of 100 ETH
    'buy_ttl_sec': 1800, # Time (in seconds) for buy order to live
    'take_profit_price_percentage_60': '5', # Take 60% profit when price of BTC goes up with 5%
    'take_profit_price_percentage_40': '10', # Take 40% profit when price of BTC goes up with 10%
    'stop_loss_price_percentage': '5', # Close position (stop loss) when price of BTC  goes down with 5%
    'panic_sell_price_percentage': '20',
    "panic_sell_price_deviation_percentage": '2'
}
