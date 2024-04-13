import sys
import requests

def main():

    if len(sys.argv) != 2:
        print("Пропущен аргумент командной строки")
        sys.exit(1)


    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        print("Аргумент командной строки не число")
        sys.exit(1)


    bitcoin_price = get_bitcoin_price()

    total_cost = bitcoins_to_buy * bitcoin_price

    
    print(f"${total_cost:,.4f}")


def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data['bpi']['USD']['rate_float']
        return bitcoin_price
    except requests.RequestException as error:
        print("Ошибка при получении данных: ", error)
        sys.exit(1)

if __name__ == '__main__':
    main()
