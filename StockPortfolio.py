
print("===== STOCK PORTFOLIO TRACKER =====")

# Step 1: Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

# Step 2: Get number of stocks
n = int(input("How many stocks do you want to enter? "))

# Step 3: Initialize total investment
total_investment = 0

# Store report details
report = "STOCK PORTFOLIO REPORT\n"
report += "----------------------\n"

# Step 4: Repeat for each stock
for i in range(n):

    stock = input("Enter stock name: ").upper()

    # Step 5: Check stock availability
    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        # Step 6: Validate quantity
        if quantity > 0:

            price = stock_prices[stock]

            investment = price * quantity

            total_investment = total_investment + investment

            print("Stock:", stock)
            print("Price:", price)
            print("Quantity:", quantity)
            print("Investment:", investment)

            report += "Stock: " + stock + "\n"
            report += "Price: " + str(price) + "\n"
            report += "Quantity: " + str(quantity) + "\n"
            report += "Investment: " + str(investment) + "\n\n"

        else:
            print("Invalid quantity!")

            report += "Invalid quantity for " + stock + "\n"

    else:
        print("Stock not found!")

        report += "Stock not found: " + stock + "\n"

# Step 7: Display grand total
print("----------------------")
print("Total Investment:", total_investment)

report += "----------------------\n"
report += "Total Investment: " + str(total_investment)

# Step 8: Save report in text file
file = open("stock_report.txt", "w")
file.write(report)
file.close()

print("Report saved successfully!")
