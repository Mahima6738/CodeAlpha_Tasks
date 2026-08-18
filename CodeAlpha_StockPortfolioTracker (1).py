# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}
total_investment = 0

print("***** Stock Portfolio Tracker *****")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available in our price list.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = quantity

# Calculate total investment
print("\n****** Portfolio Summary ******")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value

    print(f"{stock}: {quantity} shares × {price} Rs. = {value} Rs.")

print("*************************************\n")
print(f"Total Investment: {total_investment} Rs.")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("***** Stock Portfolio *****\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        file.write(f"{stock}: {quantity} shares × ${price} = ${value}\n")

    file.write("*******************************\n")
    file.write(f"Total Investment: {total_investment} Rs.\n")

print("\nPortfolio saved to portfolio.txt")