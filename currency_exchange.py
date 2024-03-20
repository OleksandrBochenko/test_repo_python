rate_buy_usd = 38.8
rate_sell_usd = 39.1
rate_buy_eur = 42.9
rate_sell_eur = 43.1
amount = float(input('Enter your amount: '))
currency_to_get = input('What currency you want to get USD/EUR/UAH: ')
currency = input('What currency you bring USD/EUR/UAH: ')
if currency_to_get == 'USD' and currency == 'UAH':
    result = amount * rate_buy_usd
elif currency_to_get == 'UAH' and currency == 'USD':
    result = amount / rate_sell_usd
elif currency_to_get == 'EUR' and currency == 'UAH':
    result = amount / rate_buy_eur
elif currency_to_get == 'UAH' and currency == 'EUR':
    result = amount * rate_sell_eur
else:
    result = 'Invalid currency'
print(f'My result is:{result} {currency}')
