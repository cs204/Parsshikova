def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    # Удаляем 'ft' из строки и преобразуем в число
    feet = float(v[:-2])

    # Переводим футы в метры
    meters = feet * 0.3048

    return meters

main()
