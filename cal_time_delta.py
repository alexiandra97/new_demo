from datetime import datetime, timedelta

date = input("Unesi datum ('DD.MM.YYYY.'): ")
date = datetime.strptime(date, "%d.%m.%Y.")
date = datetime.strftime(date, "%d/%m/%Y")
date = datetime.strptime(date, "%d/%m/%Y")
born_date = date + timedelta(115)

now_date = datetime.now()
only_date = now_date.date()
only_date = datetime.strftime(only_date, "%d/%m/%Y")
days = datetime.strptime(only_date, "%d/%m/%Y") - date
print(days)
print(born_date)