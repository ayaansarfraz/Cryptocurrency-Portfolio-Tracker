import requests
import json

class CryptocurrencyPortfolioTracker:

    def __init__(self):
        self.portfolio = {}

    def add_to_portfolio(self, coin_id, amount):
        self.portfolio[coin_id] = amount

    def remove_from_portfolio(self, coin_id):
        if coin_id in self.portfolio:
            del self.portfolio[coin_id]

    def fetch_coin_data(self, coin_id):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        data = json.loads(response.text)
        return data[coin_id]['usd']

    def display_portfolio(self):
        total_value = 0
        print("---- Portfolio ----")
        for coin_id, amount in self.portfolio.items():
            current_price = self.fetch_coin_data(coin_id)
            coin_value = current_price * amount
            total_value += coin_value
            print(f"{coin_id}: {amount} coins, Value: ${coin_value:.2f}")
        print("-------------------")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

if __name__ == "__main__":
    tracker = CryptocurrencyPortfolioTracker()

    # Sample: Add some coins to the portfolio
    tracker.add_to_portfolio("bitcoin", 0.5)
    tracker.add_to_portfolio("ethereum", 2)

    # Display the portfolio
    tracker.display_portfolio()
