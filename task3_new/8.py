print("Введите необходимую сумму дистанций")
need_distance = int(input())
start = 10
finish = 20
col_days = 1
all_distance = 10
#Функция считает расстояние, которое пробежал за день
def run_in_day(start, days):
    start *=1.1
    days+=1
    if start<=finish:
        return(run_in_day(start, days))

    return(days)
def run_sum(start, days):
    global all_distance, need_distance
    start *= 1.1
    days += 1
    all_distance += start
    if all_distance <= need_distance:
        return (run_sum(start, days))

    return (days)

print("Через ",run_in_day(start, col_days)," лыжник пробежит 20км за одну пробежку")
print("Через ",run_sum(start, col_days), f"дней лыжник пробежит {need_distance} км в сумме")
