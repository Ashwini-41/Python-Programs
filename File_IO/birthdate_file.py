import random
from datetime import datetime

birthdates = [datetime.strptime(f"{random.randint(1, 12)}-{random.randint(1, 28)}-{random.choice([1992, 1993])}", "%m-%d-%Y")
              for _ in range(50)]

same_month_birthdays = {}
for date in birthdates:
    month = date.strftime("%B")
    if month not in same_month_birthdays:
        same_month_birthdays[month] = []
    same_month_birthdays[month].append(date.strftime("%m-%d-%Y"))

with open("File_IO\Birthdays.txt", "w") as file:
    for month, dates in same_month_birthdays.items():
        file.write(f"{month}:\n")
        file.write("\n".join(dates) + "\n\n")

print("Birthdates have been written to 'Birthdays.txt'.")
