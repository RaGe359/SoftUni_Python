init_hour = int(input())
init_minutes = int(input())

total_time_min = (init_hour * 60) + init_minutes + 15

hour = total_time_min // 60
minutes = total_time_min % 60

if hour > 23:
    hour = 0

print(f'{hour}:{minutes:02}')