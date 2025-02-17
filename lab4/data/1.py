from datetime import datetime, timedelta

current_date = datetime.now()
subs =  current_date - timedelta(days = 5)
print(current_date)
print(subs)
