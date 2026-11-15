
PACKAGE = 10
PRICE_PER_GB = 500
repeat_answer = "да"

def calculate_payment(excess,price_per_gb):
  """Расчет превышения"""
  payment = excess * price_per_gb
  return payment

def calculate_package(total, package):
  """Расчет остатка пакетов"""
  if total <= package:
    remaining = package - total
    excess = 0
  else:
    excess = total - package
    remaining = 0
  return remaining, excess

def calculate_total(consumption, days):
  """Общий расход"""
  total = consumption * days
  return total

while repeat_answer == "да":
  daily_total = 0
  name = input("ФИО: ").strip().title()
  consumption = float(input("Ежедневный расход (ГБ): "))
  days = int(input("Количество дней: "))

  while days < 1 or days > 10:
    print("Ошибка! Количество дней должно быть от 1 до 10.")
    days = int(input("Количество дней: "))

  total = calculate_total(consumption, days)
  usage_percent = total / PACKAGE * 100

  remaining, excess = calculate_package(total, PACKAGE)

  payment = calculate_payment(excess, PRICE_PER_GB)

  if total < 8:
    print("Статус: Запас достаточный")
  elif 8 <= total <= 10:
    print("Статус: Пакет заканчивается")
  else:
    print("Статус: Пакет превышен")

  print(f"Имя: {name}\nОбщий расход: {total} ГБ\nИспользование пакета: {usage_percent:.1f}%\nДоплата: {payment} тг\nОстаток пакета: {remaining} ГБ")
  if excess != 0:
    print(f"Превышение: {excess}\n")

  for i in range(days):
    daily_total += consumption
    print(f"День {i + 1}: {daily_total} ГБ")

  repeat_answer = input("Хотите выполнить новый расчёт? (да/нет): ").strip().lower()

print("Программа завершена.")
