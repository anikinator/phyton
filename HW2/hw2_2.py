# url http://coolcode.ru/primeryi-resheniya-zadach-iz-knigi-m-e-abramyan-1000-zadach-po-programmirovaniyu-if/
# https://support.microsoft.com/ru-kz/help/214019/method-to-determine-whether-a-year-is-a-leap-year
# Дан номер года (положительное целое число). 
# Определить количество дней в этом году, учитывая, 
# что обычный год насчитывает 365 дней, а високосный — 366 дней.
# Високосным считается год, делящийся на 4, за исключением тех годов,
# которые делятся на 100 и не делятся на 400 (например, годы 300, 1300
# и 1900 не являются високосными, а 1200 и 2000 — являются).

chk_year = int(input("Enter the year: "))

if chk_year % 4 == 0:
    if chk_year % 100 == 0 and chk_year % 400 != 0:
        print("Your year has 366 days")

    else:
        print("Your year has 365 days")