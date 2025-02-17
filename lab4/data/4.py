from datetime import datetime

date1_str = input()
date2_str = input()

date1_parts = list(map(int, date1_str.split())) #2016 12 12 10 30 30
date2_parts = list(map(int, date2_str.split())) #2016 12 13 10 30 30

date1 = datetime(*date1_parts)  
date2 = datetime(*date2_parts)


difference_seconds = abs((date2 - date1).total_seconds())


print("Difference", int(difference_seconds))

