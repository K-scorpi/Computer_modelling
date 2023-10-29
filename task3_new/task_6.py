from datetime import*


d = input()


def f(d):
    date1=date.today()
    date2=datetime.strptime(d, '%d.%m.%Y')
    d1=date(date1.year, date1.month, date1.day)
    d2=date(date2.year, date2.month, date2.day)
    print(-((d2-d1).days))

f(d)
