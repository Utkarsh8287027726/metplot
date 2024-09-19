# currency calulator
def currency_converter(amount, from_currency, to_currency, exchange_rate):
    return amount * exchange_rate

exchange_rates = {
    'USD': {
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0
    },
    'EUR': {
        'USD': 1.18,
        'GBP': 0.88,
        'JPY': 129.0
    },
    'GBP': {
        'USD': 1.33,
        'EUR': 1.14,
        'JPY': 147.0
    },
    'JPY': {
        'USD': 0.0091,
        'EUR': 0.0078,
        'GBP': 0.0068
    }
}


print("Available currencies: USD, EUR, GBP, JPY")
from_currency = input("Enter the currency you want to convert from: ").upper()
to_currency = input("Enter the currency you want to convert to: ").upper()
amount = float(input(f"Enter the amount in {from_currency}: "))

try:
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        exchange_rate = exchange_rates[from_currency][to_currency]
        converted_amount = currency_converter(amount, from_currency, to_currency, exchange_rate)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion rate not available.")
except ValueError:
    print("Please enter a valid amount.")
