from datetime import datetime, timedelta
import random
import re

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta = today - date
        return delta.days
    except ValueError:
        print("Невірний формат дати. Використовуйте РРРР-ММ-ДД.")

# Приклади використання
get_days_from_today("2025-12-31")
get_days_from_today("2023-10-05")
get_days_from_today("2023-02-30")  # Неіснуюча дата
get_days_from_today("2023/10/05")  # Невірний формат


def get_numbers_ticket(min, max, quantity):
    numbers = []
    if 1 <= min <= quantity <= max <= 1000:
        numbers = random.sample(range(min, max +1), quantity)
    return sorted(numbers)

print(get_numbers_ticket(1, 49, 6))

def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d]", "", phone_number)
    if phone_number.startswith("0"):
        phone_number = "+38" + phone_number
    elif phone_number.startswith("380"):
        phone_number = "+" + phone_number
    elif phone_number.startswith("80"):
        phone_number = "+3" + phone_number
    elif len(phone_number) == 9:
        phone_number = "+380" + phone_number
    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "1234567890 "
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

def get_upcoming_birthdays(users):
        today = datetime.today().date()
        upcoming_birthdays = []

        for user in users:
            try:
                birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                return "Некоректний формат дати в даних користувача."

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append({
                    "name": user["name"],
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                    })

        return upcoming_birthdays
    
# Приклад використання

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Emily Davis", "birthday": "1975.02.01"},
    {"name": "Michael Brown", "birthday": "2000.02.03"},
    {"name": "Jessica Wilson", "birthday": "1995.02.05"},
    {"name": "Daniel Garcia", "birthday": "1988.10.19"},
    {"name": "Sarah Martinez", "birthday": "1992.10.18"},
    {"name": "David Anderson", "birthday": "1983.10.17"},
    {"name": "James Taylor", "birthday": "2001.10.15"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

noncorrect_users = [
    {"name": "Invalid Date", "birthday": "1985-01-23"},
    {"name": "Another Invalid", "birthday": "1990/01/27"}
]

upcoming_birthdays = get_upcoming_birthdays(noncorrect_users)
print("Список привітань на цьому тижні (з некоректними даними):", upcoming_birthdays)
  