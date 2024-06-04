import random

def generate_exam_schedule(num_exams, disciplines):
    days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
    exam_hours = [9 + i/2 for i in range(10)]
    tickets = list(range(1, 21))

    for _ in range(num_exams):
        discipline = random.choice(disciplines)
        disciplines.remove(discipline)

        day = random.choice(days_of_week)
        exam_hours_copy = exam_hours.copy()
        hour = random.choice(exam_hours_copy)
        exam_hours_copy.remove(hour)

        ticket = random.choice(tickets)
        tickets.remove(ticket)

        print(f'Экзамен по дисциплине «{discipline}» состоится в {day} время {hour:.1f}. Ваш счастливый билет №{ticket}.')

def main():
    num_exams = int(input("Введите количество экзаменов: "))
    disciplines = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")

    generate_exam_schedule(num_exams, disciplines)

if __name__ == "__main__":
    main()
