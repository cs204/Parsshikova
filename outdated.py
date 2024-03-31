import re

def get_month_number(month_name):
    months = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12"
    }
    return months.get(month_name.lower())

def convert_date(input_date):
    date_pattern = re.compile(r"(\d{1,2})[. ](\d{1,2})[. ](\d{4})|(\d{1,2}) ([а-я]+) (\d{4})")

    while True:
        match = date_pattern.match(input_date)

        if match:
            day = match.group(1) or match.group(4)
            month = match.group(2) or get_month_number(match.group(5))
            year = match.group(3) or match.group(6)

            if len(day) == 1:
                day = "0" + day
            if len(month) == 1:
                month = "0" + month

            return f"{year}-{month}-{day}"
        else:
            input_date = input("Дата: ")

if __name__ == "__main__":
    input_date = input("Дата: ")
    iso_date = convert_date(input_date)
    print(iso_date)
