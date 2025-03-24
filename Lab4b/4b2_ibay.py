def convert_currency(amount, currency):
    rates = {
        "EUR": 0.92,
        "GBP": 0.78,
        "JPY": 131.1995,
        "AUD": 1.439774,
        "CHF": 0.91,
        "CAD": 1.342308,
        "PHP": 54.81473
    }
    
    if currency in rates:
        return amount * rates[currency]
    return None

amount = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

converted_amount = convert_currency(amount, currency)

if converted_amount is not None:
    print(f"\nDollar: {amount} USD")
    print(f"{currency}: {converted_amount}")
else:
    print("Invalid currency code.")
