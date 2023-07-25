usd_to_uah = 36.9
uah_to_usd = 37.10
eur_to_uah = 40.26
usd_to_eur = 0.92


def converter(amount, source_currency, target_currency):
    if source_currency == "USD" and target_currency == "UAH":
        return amount * usd_to_uah
    elif source_currency == "EUR" and target_currency == "UAH":
        return amount * eur_to_uah
    elif source_currency == "USD" and target_currency == "EUR":
        return amount * usd_to_eur
    elif source_currency == "EUR" and target_currency == "USD":
        return amount / usd_to_eur
    elif source_currency == "UAH" and target_currency == "USD":
        return amount / uah_to_usd
    elif source_currency == "UAH" and target_currency == "EUR":
        return amount / eur_to_uah
    else:
        return None


if __name__ == '__main__':
    # Зчитування вхідних даних від користувача
    amount = float(input("Введіть суму: "))
    source_currency = input("Введіть вихідну валюту (наприклад, USD, EUR, UAH): ")
    target_currency = input("Введіть цільову валюту (наприклад, USD, EUR, UAH): ")

    result = converter(amount, source_currency, target_currency)

    result2 = converter(100, 'USD', 'UAH')
    print(f'my result2: {result2}')

    if result:
        print("Сума після конвертації:", result, target_currency)
    else:
        print("Конвертація не підтримується")
