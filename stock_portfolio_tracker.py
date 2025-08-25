def stock_portfolio_tracker():
    # Step 1: Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 135,
        "MSFT": 300
    }
    
    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks and prices:", stock_prices)
    print("Enter stock name and quantity (type 'done' to finish).\n")
    
    portfolio = {}  # Store stock investments
    total_value = 0
    
    # Step 2: User input loop
    while True:
        stock = input("Enter stock symbol (or 'done'): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not available. Try again.")
            continue
        
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue
        
        investment = stock_prices[stock] * qty
        portfolio[stock] = portfolio.get(stock, 0) + investment
        total_value += investment
        print(f"✅ Added {qty} shares of {stock} worth ${investment}\n")
    
    # Step 3: Display results
    print("\n📊 Your Portfolio Summary:")
    for stock, value in portfolio.items():
        print(f"{stock}: ${value}")
    print(f"\n💰 Total Portfolio Value: ${total_value}")
    
    # Step 4: Save to file (optional)
    save_choice = input("\nDo you want to save portfolio to file? (yes/no): ").lower()
    if save_choice == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary:\n")
            for stock, value in portfolio.items():
                f.write(f"{stock}: ${value}\n")
            f.write(f"\nTotal Portfolio Value: ${total_value}\n")
        print("📂 Portfolio saved to 'portfolio.txt'.")

# Run the tracker
stock_portfolio_tracker()
