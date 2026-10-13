from datetime import datetime

date1 = input("Enter the first date (DD-MM-YYYY): ")
date2 = input("Enter the second date (DD-MM-YYYY): ")
d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")
difference = abs((d2 - d1).days)
print("Number of days between two dates:", difference)