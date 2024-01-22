from sys import stdin

def dayOfWeek(day, month, year):
	if month < 3:
		month += 12
		year -= 1
	q = day
	m = month
	K = year % 100
	J = year // 100
	h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7
	daysOfWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	return daysOfWeek[h]

def takeInput() :

	day_month_year = list(map(int,stdin.readline().strip().split(" ")))
	day = day_month_year[0]
	month = day_month_year[1]
	year = day_month_year[2]

	return day, month, year

t = int(input().strip())
for i in range(t) :

	day, month, year = takeInput()
	print(dayOfWeek(day, month, year))

