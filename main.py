import requests  
import json

# Create API request
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=YOUR-API-KEY")

# Use JSON to parse data
api = json.loads(api_request.content)

print("--------------------")
print("--------------------")

# Create a dictionary to store each coin information.
coins = [
  {
    "symbol":"BTC",
    "current_amount": 5,
    "price_per_coin": 43025
  },
  {
    "symbol":"ETH",
    "current_amount": 10,
    "price_per_coin": 3322
  },
  {
    "symbol":"BNB",
    "current_amount": 17,
    "price_per_coin": 496
  },
  {
    "symbol":"USDT",
    "current_amount": 20,
    "price_per_coin": 1
  },
  {
    "symbol":"ADA",
    "current_amount": 25,
    "price_per_coin": 2
  },
  {
    "symbol":"SOL",
    "current_amount": 7,
    "price_per_coin": 149
  },
  {
    "symbol":"USDC",
    "current_amount": 15,
    "price_per_coin": 1
  },
  {
    "symbol":"XRP",
    "current_amount": 25,
    "price_per_coin": 1
  },
  {
    "symbol":"LUNA",
    "current_amount": 35,
    "price_per_coin": 86
  },
  {
    "symbol":"DOT",
    "current_amount": 31,
    "price_per_coin": 28
  },
]

# Total profit and loss.
total_profit_loss = 0

# Use a for loop to print the 10 coins on our API request.
for i in range(0,10):
  for coin in coins:
    if api["data"][i]["symbol"] == coin["symbol"]:
      # Total paid per coin.
      total_paid = coin["current_amount"] * coin["price_per_coin"] 
      # Current value.
      current_value = coin["current_amount"] * api["data"][i]["quote"]["USD"]["price"]
      # Calculate profit and loss per coin.
      profit_loss_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"] 
      # Calculate total profit and loss per coin.
      total_profit_loss_per_coin = profit_loss_per_coin * coin["current_amount"]
      total_profit_loss = total_profit_loss + total_profit_loss_per_coin
      
      print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
      print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
      print("Coins Owned:", coin["current_amount"])
      print("Total Amount Paid:", "${0:.2f}".format(total_paid))
      print("Current Value:", "${0:.2f}".format(current_value))
      print("Profit Loss Per Coin:", "$ {0:.2f}".format(profit_loss_per_coin))
      print("Total Profit Loss With Coin:", "$ {0:.2f}".format(total_profit_loss_per_coin))
      print("--------------------")
        
# Total profit loss of the portfolio.
print("The Total Profit/Loss of this Portfolio Is: ", "${0:.2f}".format(total_profit_loss))
