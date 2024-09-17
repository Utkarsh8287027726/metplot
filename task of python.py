
from datetime import datetime
birthdate = datetime(2001 , 12 ,21)
today = datetime.now()
age_in_days = (today - birthdate).days
print(f"you are {age_in_days} days old")


