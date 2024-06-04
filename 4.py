from datetime import datetime, timedelta

def find_lucky_exam_dates(start_date, n, num_dates):
    exam_dates = []
    current_date = datetime.strptime(start_date, "%Y/%m/%d")

    while len(exam_dates) < num_dates:
        # Проверяем, что номер дня не кратен четырем и это не понедельник
        if current_date.day % 4 != 0 and current_date.weekday() != 0:
            exam_dates.append(current_date)
        # Переходим к следующему n-му дню
        current_date += timedelta(days=n)

    return exam_dates

def main():
    try:
        start_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
        n = int(input("Введите число n: "))
        num_dates = 3  # Количество подходящих дат для вывода

        exam_dates = find_lucky_exam_dates(start_date, n, num_dates)

        print("Подходящие даты для экзамена:")
        for date in exam_dates:
            formatted_date = date.strftime("%d %B, %A")
            print(formatted_date)

    except ValueError:
        print("Ошибка: Проверьте правильность ввода даты и числа n.")

if __name__ == "__main__":
    main()
