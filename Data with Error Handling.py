import yfinance as yf

def fetch_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print("Error fetching stock data:", e)
        return None

# Example usage:
symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"
stock_data = fetch_stock_data(symbol, start_date, end_date)
if stock_data is not None:
    print("Stock data:")
    print(stock_data.head())
