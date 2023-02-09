from datetime import datetime

date1 = datetime.strptime("2022.01.01", "%Y.%m.%d")
date2 = datetime.strptime("2022-12-31", "%Y.%m.%d")

if date1 < date2:
    print("Date1 is earlier than Date2")
else:
    print("Date2 is earlier than Date1")
