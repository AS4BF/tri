from datetime import datetime, timedelta

def exam_date(days_until_exam):

    current_date = datetime.now()
    exam_date = current_date + timedelta(days=days_until_exam)
    exam_day = exam_date.strftime("%d")
    exam_month = exam_date.strftime("%m")

    return exam_day, exam_month

def main():
    try:
        days_until_exam = int(input("Введите количество дней до экзамена: "))
        exam_day, exam_month = exam_date(days_until_exam)
        print(f"Экзамен состоится {exam_day}.{exam_month}")
    except ValueError:
        print("Ошибка: Введите корректное количество дней.")

if __name__ == "__main__":
    main()
