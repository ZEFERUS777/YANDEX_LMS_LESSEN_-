happy_hours = list(map(int, input().strip().split()))
happy_minutes = list(map(int, input().strip().split()))


def digit_sum(n):
    return sum(int(digit) for digit in str(n).zfill(2))


lucky_moments = []

for hour in happy_hours:
    for minute in happy_minutes:
        if digit_sum(hour) != digit_sum(minute):
            lucky_moments.append(f"{hour:02}:{minute:02}")

lucky_moments.sort()

for moment in lucky_moments:
    print(moment)